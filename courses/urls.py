from django.urls import path
from . import views

""" app_name = 'courses' """

urlpatterns = [
    path('', views.index, name='courses'), 
    path('enroll/<int:course_id>', views.enroll, name='enroll'), 
    path('enrolls', views.course, name='enrolls'), 
    path('<int:course_id>', views.course, name='course'), 
]