from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='cars'), 
    path('private', views.private, name='private'), 
    path('business', views.business, name='business'), 
    path('van', views.van, name='van'), 
    path('<int:car_id>', views.car, name='car'), 
]