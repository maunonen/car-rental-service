from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _ , activate
from django.utils import translation

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    #user_language = 'ru'
    #translation.activate( user_language)
    #print(request)
    #print(translation.LANGUAGE_SESSION_KEY) 
    #request.session['test'] = 'test'
    #request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    context = { 
        'hello' : _('Hello') 
    }
    return render(request, 'pages/about.html', context )

def contact(request):
    return render(request, 'pages/contact.html')

def news(request):
    return render(request, 'pages/news.html')

def services(request):
    return render(request, 'pages/services.html')