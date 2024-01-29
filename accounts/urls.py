from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('support/', views.support, name='support'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('register_in/', views.register_in, name='register_in'),
    path('register_up/', views.register_up, name='register_up'),

    # path('test/', views.test)
]