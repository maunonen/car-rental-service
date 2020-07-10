from django.shortcuts import render
from .models import Course
from enrolls.forms import EnrollForm


# Create your views here.

def index (request): 
    courses = Course.objects.all()
    form = EnrollForm()
    context = {
        'courses' : courses, 
        'forms' : form
    }
    return render(request,'courses/courses.html', context)

def course (request, course_id): 
    return render(request, 'courses/course.html')