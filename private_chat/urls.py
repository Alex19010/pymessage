from django.urls import path

from . import views


urlpatterns = [
    path('private_chat/', views.private_chat, name='private_chat'),
]