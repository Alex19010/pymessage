from django.contrib import admin

from .models import Post, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1


@admin.register(Post)
class AdminUser(admin.ModelAdmin):
    inlines = (CommentInline,)
    list_display = ("id", "owner", "name")
    list_display_links = list_display
    list_filter = ('owner', "name")
    search_fields = ('owner', "name")


# @admin.register(Comment)
# class AdminUser(admin.ModelAdmin):
#     list_display = ("id", "owner")
#     list_display_links = list_display
#     list_filter = ('owner',)
#     search_fields = ('owner',)
