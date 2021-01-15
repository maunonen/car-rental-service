from django.urls import path
from django.conf.urls import url, re_path
from . import views

urlpatterns = [
  path('', views.index, name='rentals'), 
  path('add/<int:car_id>/', views.add, name='add'),   
  path('add/<int:car_id>/<str:rental_start>/<str:rental_end>/', views.add, name='add'),   
]

""" path('test/<int:car_id>/<str:rental_start>/<str:rental_end>/', views.test, name='test'),    """
""" url(r'^$', views.index),   """
""" re_path(r'^test/<int:param1>/$', views.test, 'test'), """