from django.urls import path

from . import views


urlpatterns = [
    path('group_chat/', views.chat_view, name='group_chat'),
]