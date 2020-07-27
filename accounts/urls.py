from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'), 
    path('register', views.register, name='register'), 
    path('dashboard', views.dashboard, name='dashboard'), 
    path('logout', views.user_logout, name='logout'), 
    path('profile', views.profile, name='profile'), 
    path('delete_profile', views.delete_profile, name='delete_profile'), 
    path('change_password', views.change_password, name='change_password'), 
]