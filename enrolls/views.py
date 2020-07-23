from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from .models import Enroll

# Create your views here.

@login_required(login_url='/accounts/login')
def index (request): 
    user = request.user
    #enrolls = Enroll.objects.all()
    enrolls = Enroll.objects.filter(user=user)
    context = {
        'enrolls' : enrolls
    }
    return render(request,'enrolls/enrolls.html', context)

    