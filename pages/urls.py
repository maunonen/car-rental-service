from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('about', views.about, name='about'), 
    path('news', views.news, name='news'), 
    path('contact', views.contact, name='contact'), 
    path('services', views.services, name='services'), 
    path('privacy', views.privacy, name='privacy'), 
    path('faq', views.faq, name='faq'), 
    path('payments', views.payments, name='payments'), 
    path('conditions', views.conditions, name='conditions'), 
]