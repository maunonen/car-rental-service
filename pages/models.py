from django.db import models
from datetime import datetime
# Create your models here.

class Contact (models.Model): 
    name = models.CharField( max_length=50)    
    email = models.EmailField( max_length=254)    
    phone_number = models.CharField( max_length=20)    
    message = models.TextField( max_length=1000)    
    ## default 
    def __str__(self):
        return self.name + self.phone_number + self.email

class News (models.Model): 
    title = models.CharField( max_length=50)    
    img_link = models.ImageField(upload_to='photos', blank=True)
    text = models.TextField(max_length=2000)
    is_published = models.BooleanField(default=True)
    news_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title