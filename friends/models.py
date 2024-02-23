from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Friend(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user')
    friend = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'friend')
    created = models.DateTimeField(verbose_name='Time', auto_now_add = True)

    class Meta:
        unique_together = ['user', 'friend']
        verbose_name = 'Friend'
        verbose_name_plural = 'Friends'

    def __str__(self):
        return f'{self.user} - {self.friend}'
