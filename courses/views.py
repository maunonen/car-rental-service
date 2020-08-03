from django.shortcuts import render, get_object_or_404
from .models import Course
from enrolls.models import Enroll
from enrolls.forms import EnrollForm
import json
from django.http import HttpResponse, JsonResponse

# mail notification 
from django.core.mail import send_mail, BadHeaderError
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

# Create your views here.

def index (request): 
    courses = Course.objects.all()
    if request.method == "POST" and request.is_ajax():
        print("METHOD POST AJAX")
        form = EnrollForm(request.POST)
        #print(form.cleaned_data)
        if form.is_valid(): 
            context = {
                'courses' : courses, 
                'form' : form
            }
            print(form.cleaned_data)
            return HttpResponse("success")
        else : 
            print("METHOD IS INVALID")
            print(form)
            context = {
                'courses' : courses, 
                'form' : form
            }
            return HttpResponse("Error") 
    else: 
        form = EnrollForm()
        context = {
            'courses' : courses, 
            'form' : form
        }
        print(context)
    return render(request,'courses/courses.html', context)

def course (request, course_id): 
    return render(request, 'courses/course.html')


def enroll(request, course_id):     
    course = get_object_or_404(Course, id=course_id)
    if not course : 
        message = { 'course id' : 'Course not found'}
        response = JsonResponse({'status':'false','message': message}, status=409 )
        return response
    if request.method == "POST" and request.is_ajax():
        form = EnrollForm(request.POST)
        if form.is_valid(): 
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')
            enroll = Enroll(
                first_name = first_name, 
                last_name = last_name, 
                email = email, 
                phone_number = phone_number, 
                course = course
            )
            if request.user.is_authenticated: 
                enroll.user = request.user
            enroll.save()
            
            # send mail notification to client 
            try:  
                context_client = {
                    'first_name' : first_name, 
                    'last_name' : last_name, 
                    'course' : course
                }
                # html message Version 
                html_message_client = render_to_string('email/client/new_enroll.html', context=context_client)
                # txt message VVersion
                subject_client = f'You have been successfully enrolled to the course: { course }!'
                plain_message_client = strip_tags(html_message_client)
                # send mail 
                mail.send_mail(
                    subject_client, 
                    plain_message_client, 
                    # from
                    settings.DEFAULT_FROM_EMAIL, 
                    # to recipients 
                    [email], 
                    html_message=html_message_client,
                    fail_silently=False,
                )
                print('Success Client')
            except BadHeaderError:
                print(BadHeaderError)
            
            # send  mail notification to admin 
            try: 
                # link to template 
                context = {
                    'first_name' : first_name, 
                    'last_name' : last_name, 
                    'phone_number' : phone_number, 
                    'course' : course
                }
                html_message = render_to_string('email/admin/new_enroll.html', context=context)
                # txt version of message
                subject = f'You have new participent { first_name}, { last_name} in { course}'
                plain_message = strip_tags(html_message)
                mail.mail_admins(
                    subject, 
                    plain_message, 
                    fail_silently=False,
                    connection=None, 
                    html_message=html_message, 
                )
            except BadHeaderError :
                print(BadHeaderError)

            return HttpResponse("success")
        else : 
            if form.errors : 
                message = form.errors
                response = JsonResponse({'status':'false','message': message}, status=409 )
                return response


