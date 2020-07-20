from django.shortcuts import render, get_object_or_404
from .models import Course
from enrolls.models import Enroll
from enrolls.forms import EnrollForm
import json
from django.http import HttpResponse, JsonResponse

# Create your views here.

def index (request): 
    print("VIEW METHOD index")
    courses = Course.objects.all()
    if request.method == "POST" and request.is_ajax():
        print("METHOD POST AJAX")
        form = EnrollForm(request.POST)
        #print(form.cleaned_data)
        if form.is_valid(): 
            print("METHOD IS VALID")
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
            enroll.save()
            return HttpResponse("success")
        else : 
            if form.errors : 
                message = form.errors
                response = JsonResponse({'status':'false','message': message}, status=409 )
                return response


def ajax(request): 
    print(request)
    print("AJAX METHOD")
    if request.method == "POST":
        print("METHOD POST AJAX")
        #form = EnrollForm(request.POST)
        if form.is_valid(): 
            print("METHOD IS VALID")
            """ context = {
                'courses' : courses, 
                'form' : form
            } """
            print(form.cleaned_data)
            return HttpResponse("success")
        else : 
            print("METHOD IS INVALID")
            """ context = {
                'courses' : courses, 
                'form' : form
            } """
            return HttpResponse("Error") 
    #else: 
        """ form = EnrollForm()
        context = {
            'courses' : courses, 
            'form' : form
        } """
        #print(context)
    #return render(request,'courses/courses.html', context)