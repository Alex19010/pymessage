from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class GroupChat(models.Model):
    members = models.ManyToManyField(User, related_name='group_chats')
    name = models.CharField(verbose_name='Name' ,max_length=150)
    avatar = models.ImageField(verbose_name = "Avatar", upload_to = "image/", default = "defaults/default_group.png", null = True, blank = True)

    class Meta:
        verbose_name = 'Group chat'
        verbose_name_plural = 'Group chats'

    @property
    def short_name(self):
        return f"{self.name[:5]}..."


class GroupMessage(models.Model):
    chat = models.ForeignKey(GroupChat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Message')
    timestamp = models.DateTimeField(verbose_name='Time', auto_now_add=True)

    class Meta:
        verbose_name = 'Group message'
        verbose_name_plural = 'Group messages'
