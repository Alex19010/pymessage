from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('posts/like/<int:post_id>/', views.add_like, name='like_post'),
    path('posts/create_new_post/', views.create_post, name='create_new_post'),
]
