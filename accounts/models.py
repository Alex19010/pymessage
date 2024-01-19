from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(verbose_name = "Username", max_length = 100, unique = True)
    email = models.EmailField(verbose_name = "Email", unique = True)
    avatar = models.ImageField(verbose_name = "Avatar", upload_to = "image/", default = "media/defaults/avatar.jpg", null = True, blank = True)
    first_name = models.CharField(verbose_name = "First name", max_length = 100)
    last_name = models.CharField(verbose_name = "Last name", max_length = 100, null = True, blank = True)
    date_of_birth = models.DateField(verbose_name = "Date of birth", null = True, blank = True)
    status = models.CharField(verbose_name = "Status", max_length = 250, null = True, blank = True)
    address = models.CharField(verbose_name = "Address", max_length = 250, null = True, blank = True)

    class Meta:
        verbose_name = "Name"
        verbose_name_plural = "Names"

    def __str__(self):
        return self.username
