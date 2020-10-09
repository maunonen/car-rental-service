from django.shortcuts import render
from django.conf.urls import (handler400, handler403, handler404, handler500)

def handler404(request, exception ):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)