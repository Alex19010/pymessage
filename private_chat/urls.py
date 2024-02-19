from django.urls import path

from . import views


urlpatterns = [
    path('private_chat/', views.chat_view, name='private_chat'),
    path('private_chat/<int:chat_id>/', views.chat_one_view, name='one_private_chat'),

    path('private_chat/save/<int:chat_id>/', views.save_message_view, name='save_message'),
]
