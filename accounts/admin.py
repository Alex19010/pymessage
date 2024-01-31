from django.contrib import admin

from .models import User


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name")
    list_display_links = list_display
