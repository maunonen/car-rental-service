from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import gettext as _, activate
from django.utils import translation
from django.contrib import messages

from django.core.mail import send_mail, BadHeaderError, mail_admins

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import Contact, News, Page
from .forms import ContactForm
from django.conf import settings

from pprint import pprint

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def payments(request):
    ## get all pages
    context = Page.objects.all()
    ## 1. default page name 
    pageName = 'PM'
    ##  2. default language
    pageLang = 'fi'

    ##  3. check current language 
    if request.LANGUAGE_CODE: 
        pageLang = request.LANGUAGE_CODE
    
    ## 4. get content from database by page name and language
    try :
        context = context.filter(page_name__iexact=pageName, page_lang__iexact=pageLang).get()
    # Object  not found  
    except ObjectDoesNotExist:
        context = ''
        
    # Multiply Object were found 
    except MultipleObjectsReturned: 
        context = ''
    
    if not context: 
        context = ''

    context = { 
        'context' : context
    }
    #return render(request, 'pages/conditions.html', context )
    return render(request, 'pages/payments.html', context )

def conditions(request):
    ## get all pages
    context = Page.objects.all()
    ## 1. default page name 
    pageName = 'CN'
    ##  2. default language
    pageLang = 'fi'

    ##  3. check current language 
    if request.LANGUAGE_CODE: 
        pageLang = request.LANGUAGE_CODE
    
    ## 4. get content from database by page name and language
    try :
        context = context.filter(page_name__iexact=pageName, page_lang__iexact=pageLang).get()
    # Object  not found  
    except ObjectDoesNotExist:
        context = ''
        
    # Multiply Object were found 
    except MultipleObjectsReturned: 
        context = ''
    
    if not context: 
        context = ''

    context = { 
        'context' : context
    }
    return render(request, 'pages/conditions.html', context )

def faq(request):
    ## get all pages
    context = Page.objects.all()
    ## 1. default page name 
    pageName = 'FQ'
    ##  2. default language
    pageLang = 'fi'

    ##  3. check current language 
    if request.LANGUAGE_CODE: 
        pageLang = request.LANGUAGE_CODE
    
    ## 4. get content from database by page name and language
    try :
        context = context.filter(page_name__iexact=pageName, page_lang__iexact=pageLang).get()
    # Object  not found  
    except ObjectDoesNotExist:
        context = ''
        
    # Multiply Object were found 
    except MultipleObjectsReturned: 
        context = ''
    
    if not context: 
        context = ''

    context = { 
        'context' : context
    }
    return render(request, 'pages/faq.html', context )

def privacy(request):
    ## get all pages
    context = Page.objects.all()
    ## 1. default page name 
    pageName = 'PC'
    ##  2. default language
    pageLang = 'fi'

    ##  3. check current language 
    if request.LANGUAGE_CODE: 
        pageLang = request.LANGUAGE_CODE
    
    ## 4. get content from database by page name and language
    try :
        context = context.filter(page_name__iexact=pageName, page_lang__iexact=pageLang).get()
    # Object  not found  
    except ObjectDoesNotExist:
        context = ''
        
    # Multiply Object were found 
    except MultipleObjectsReturned: 
        context = ''
    
    if not context: 
        context = ''

    context = { 
        'context' : context
    }
    return render(request, 'pages/privacyPolicy.html', context )

def about(request):
    
    ## get all pages
    context = Page.objects.all()
    ## 1. default page name 
    pageName = 'AB'
    ##  2. default language
    pageLang = 'fi'

    ##  3. check current language 
    if request.LANGUAGE_CODE: 
        pageLang = request.LANGUAGE_CODE
    
    ## 4. get content from database by page name and language
    try :
        context = context.filter(page_name__iexact=pageName, page_lang__iexact=pageLang).get()
    # Object  not found  
    except ObjectDoesNotExist:
        context = ''
        
    # Multiply Object were found 
    except MultipleObjectsReturned: 
        context = ''
    
    if not context: 
        context = ''

    context = { 
        'context' : context
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
            # send notification by email 
            if name and email and message: 
                # send notification to client
                try:  
                    context_client = {
                        'name' : name, 
                        'message' : message
                    }
                    # html message Version 
                    html_message_client = render_to_string('email/client/contact.html', context=context_client)
                    # txt message VVersion
                    subject_client = f'Thank you for your request, {name}!'
                    plain_message_client = strip_tags(html_message_client)
                    mail.send_mail(
                        subject_client, 
                        plain_message_client, 
                        # from
                        settings.DEFAULT_FROM_EMAIL, 
                        # recipients 
                        [email], 
                        html_message=html_message_client,  
                        fail_silently=False,
                    ) 
                    print('Success')
                except BadHeaderError:
                    print(BadHeaderError)

                # send notification to admins 
                try:  
                    context = {
                        'name' : name, 
                        'email' : email,    
                        'phone_number' : phone_number, 
                        'message' : message, 
                    }
                    # html message Version 
                    html_message = render_to_string('email/admin/contact.html', context=context)
                    # txt message VVersion
                    subject = f'New contact message from, {name}!'
                    plain_message = strip_tags(html_message)
                    #mail_admins(subject, message, fail_silently=False, connection=None, html_message=None)
                    mail.mail_admins(
                        subject, 
                        plain_message, 
                        fail_silently=False,
                        #connection=None, 
                        html_message=html_message, 
                    )
                    print('Success')
                except BadHeaderError:
                    print(BadHeaderError)
                    """ messages.error(request, 'Something went wrong')
                    form = ContactForm()
                    return render(request, 'pages/contact.html', {'form' : form}) """
            # save constact to datebase                            
            contact = Contact(name=name, email=email, phone_number=phone_number, message=message)
            contact.save()
            messages.success(request, 'Your contact request has been sent')
            return render(request, 'pages/contact.html', {'form' : form})
        else: 
            return render(request, 'pages/contact.html', {'form' : form})
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