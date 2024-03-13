from django.urls import path

from . import views


urlpatterns = [
    path('', views.friends_view, name='friends'),
    path('add/<int:user_id>', views.add_friend, name='add_friend'),
    path('remove/<int:friend_id>', views.remove_friend, name='remove_friend'),
    path('applications/', views.applications_view, name='applications'),
    path('applications/accept/<int:application_id>', views.accept_application, name='accept_application'),
    path('applications/delete/<int:application_id>', views.delete_application, name='delete_application'),
]
