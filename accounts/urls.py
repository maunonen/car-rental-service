from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'), 
    path('register', views.register, name='register'), 
    path('dashboard', views.dashboard, name='dashboard'), 
    path('logout', views.user_logout, name='logout'), 
    path('profile', views.profile, name='profile'), 
    path('delete/<int:user_id>', views.delete, name='delete_profile'), 
    path('change/<int:user_id>', views.changePassword, name='change_password'), 
]