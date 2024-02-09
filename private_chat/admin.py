from django.contrib import admin

from .models import PrivateChat, PrivateMessage


class MessageInline(admin.StackedInline):
    model = PrivateMessage
    extra = 1

@admin.register(PrivateChat)
class AdminChat(admin.ModelAdmin):
    list_display = ("id",)
    inlines = (MessageInline,)