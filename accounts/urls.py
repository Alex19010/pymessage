from django.urls import path

from . import views


urlpatterns = [
    # path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register_in/', views.register_in, name='register_in'),
    path('register_up/', views.register_up, name='register_up'),
    path('logout/', views.logout_view, name='logout'),

    # path('test/', views.test)
]