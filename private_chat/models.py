from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class PrivateChat(models.Model):
    members = models.ManyToManyField(User, related_name='private_chats')

    class Meta:
        verbose_name = 'Private chat'
        verbose_name_plural = 'Private chats'


class PrivateMessage(models.Model):
    chat = models.ForeignKey(PrivateChat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Message')
    timestamp = models.DateTimeField(verbose_name='Time', auto_now_add=True)

    class Meta:
        verbose_name = 'Private message'
        verbose_name_plural = 'Private messages'
