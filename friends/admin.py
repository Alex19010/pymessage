from django.contrib import admin

from .models import Friend, Application


@admin.register(Friend)
class AdminFriend(admin.ModelAdmin):
    list_display = ("id", 'user', 'friend')
    list_display_links = list_display


@admin.register(Application)
class AdminApplication(admin.ModelAdmin):
    list_display = ('id', 'user', 'friend')
    list_display_links = list_display
