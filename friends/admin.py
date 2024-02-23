from django.contrib import admin

from .models import Friend


@admin.register(Friend)
class AdminUser(admin.ModelAdmin):
    list_display = ("id",)
    list_display_links = list_display
