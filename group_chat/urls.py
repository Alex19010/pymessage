from django.urls import path

from . import views


urlpatterns = [
    path('', views.chat_view, name='group_chat'),
    path('<int:chat_id>/', views.chat_one_view, name='one_group_chat'),

    path('save/<int:chat_id>/', views.save_message_view, name='save_message'),
    path('invite/<str:code>', views.add_to_group_by_invite_link, name='add_to_group'),
    path('create_group_chat/', views.create_group_chat, name='create_group_chat'),
    path('update_group_chat/<int:chat_id>/', views.update_group_chat, name='update_group_chat'),
]
