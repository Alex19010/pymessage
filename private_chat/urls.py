from django.urls import path

from . import views


urlpatterns = [
    path('', views.chat_view, name='private_chat'),
    path('test/<int:user_id>', views.create_priv_chat, name='one_private_chat_new'),
    path('<int:chat_id>/', views.chat_one_view, name='one_private_chat'),


    path('save/<int:chat_id>/', views.save_message_priv_view, name='save_message_priv'),
]
