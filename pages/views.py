from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import gettext as _, activate
from django.utils import translation
from django.contrib import messages
from .models import Contact, News
from .forms import ContactForm

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    
    context = { 
        'hello' : _('Hello') 
    }
    return render(request, 'pages/about.html', context)

def contact(request):
    if request.method == 'POST' or None:
        form = ContactForm(request.POST)
        if form.is_valid(): 
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')
            message = form.cleaned_data.get('message')
            contact = Contact(name=name, email=email, phone_number=phone_number, message=message)
            contact.save()
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()
    return render(request, 'pages/contact.html', {'form' : form})
    
def news(request):
    news = News.objects.all()
    context = {
        'news' : news
    }
    return render(request, 'pages/news.html', context)

def services(request):
    return render(request, 'pages/services.html')