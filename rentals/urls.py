from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='rentals'), 
    path('add/<int:car_id>', views.add, name='add'), 
]