from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'), 
    url(r'^about/$', views.about, name='about'), 
    url(r'^news/$', views.news, name='news'), 
    url(r'^contact/$', views.contact, name='contact'), 
    url(r'^services/$', views.services, name='services'), 
    url(r'^privacy/$', views.privacy, name='privacy'), 
    url(r'^faq/$', views.faq, name='faq'), 
    url(r'^payments/$', views.payments, name='payments'), 
    url(r'^conditions/$', views.conditions, name='conditions'), 
]

""" path('', views.index, name='index'),  """