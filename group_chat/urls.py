from django.urls import path

from . import views


urlpatterns = [
    path('group_chat/', views.chat_view, name='group_chat'),
    path('group_chat/<int:chat_id>/', views.chat_one_view, name='one_group_chat'),

    path('group_chat/save/<int:chat_id>/', views.save_message_view, name='save_message'),
]