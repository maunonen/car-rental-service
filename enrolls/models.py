from django.db import models
from courses.models import *

# Create your models here.

class Enroll(models.Model): 
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING) 
    first_name = models.CharField( max_length=50)    
    last_name = models.CharField(max_length=50, default='John')    
    email = models.EmailField( max_length=254)   
    phone_number = models.CharField( max_length=20)
    
    def __str__(self):
        return self.title + self.last_name + self.first_name
    