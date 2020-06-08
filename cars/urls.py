from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='cars'), 
    path('<int:car_id>', views.car, name='car'), 
]