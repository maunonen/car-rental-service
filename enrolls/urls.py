from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='enrolls'), 
    #path('<int:enroll_id>', views.enroll, name='enroll'), 
]