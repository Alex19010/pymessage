from django.urls import path

from . import views


urlpatterns = [
    path('private_chat/', views.chat_view, name='private_chat'),
]