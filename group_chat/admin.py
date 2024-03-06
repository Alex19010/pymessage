from django.contrib import admin
from .models import GroupChat, GroupMessage


class MessageInline(admin.StackedInline):
    model = GroupMessage
    extra = 1


@admin.register(GroupChat)
class AdminChat(admin.ModelAdmin):
    list_display = ("id", 'name')
    inlines = (MessageInline,)
    list_display_links = list_display
    list_filter = ('name',)
    search_fields = ('name',)
