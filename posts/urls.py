from django.urls import path

from . import views


urlpatterns = [
    path('', views.friends_posts, name='home'),
    path('my_posts', views.my_posts, name='my_posts'),
    path('like/<int:post_id>/', views.add_remove_like, name='like_post'),
    path('create_new_post/', views.create_post, name='create_new_post'),
    path('comments/<int:post_id>/', views.comments_view, name='comments'),
    path('comments/create/<int:post_id>/', views.create_comment_view, name='create_comment'),
]
