from django.contrib import admin

from .models import Post, Comment


@admin.register(Post)
class AdminUser(admin.ModelAdmin):
    list_display = ("id", "owner", "name")
    list_display_links = list_display


@admin.register(Comment)
class AdminUser(admin.ModelAdmin):
    list_display = ("id", "owner")
    list_display_links = list_display
