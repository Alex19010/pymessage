from django.db import models
from django.contrib.auth.models import AbstractUser

from .utils import set_random_username


class User(AbstractUser):
    username = models.CharField(verbose_name = "Username", max_length = 100, unique = True)
    email = models.EmailField(verbose_name = "Email", unique = True)
    avatar = models.ImageField(verbose_name = "Avatar", upload_to = "image/", default = "defaults/avatar.jpg", null = True, blank = True)
    first_name = models.CharField(verbose_name = "First name", max_length = 100)
    last_name = models.CharField(verbose_name = "Last name", max_length = 100, null = True, blank = True)
    date_of_birth = models.DateField(verbose_name = "Date of birth", null = True, blank = True)
    status = models.CharField(verbose_name = "Status", max_length = 250, null = True, blank = True)
    address = models.CharField(verbose_name = "Address", max_length = 250, null = True, blank = True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs) -> None: #Iterable[str] | None = ...:
        self.username = set_random_username()
        return super().save(*args, **kwargs)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".title()