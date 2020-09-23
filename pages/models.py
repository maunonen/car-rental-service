from django.db import models
from datetime import datetime
#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _
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

class Page (models.Model):
    class PagesName (models.TextChoices):
        DEFAULT = '', _('Sivuston nimi')
        ABOUT = 'AB', _('About')
        NEWS = 'NW', _('News')
        CARLIST = 'CL', _('Car List')
        CONDITIONS = 'CN', _('CONDITION')
        PRIVACY = 'PC', _('PRIVACY')
        SERVICES = 'SV', _('SERVICES')
        PAYMENTS = 'PM', _('PAYMENTS')
        FAQ = 'FQ', _('FAQ')
    
    class PagesLang (models.TextChoices):
        DEFAULT = '', _('Sivuston nimi')
        FINISH = 'fi', _('Suomi')
        RUSSIAN = 'ru', _('Venäjä')
        ENGLISH = 'en', _('Englanti')
        ESTONIAN = 'es', _('Viro')
    

    page_name = models.CharField(max_length=20, choices=PagesName.choices, default=PagesName.DEFAULT)
    page_lang = models.CharField(max_length=20, choices=PagesLang.choices, default=PagesLang.DEFAULT)
    name = models.CharField(max_length=50)
    is_published = models.BooleanField(default=True)
    news_date = models.DateTimeField(default=datetime.now, blank=True)
    #content = RichTextField(blank=True, null=True)
    content = RichTextUploadingField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields= ['page_name','page_lang'], name='unique_translations'),
        ]
    
    def __str__(self):
        return   self.page_lang + ' - '+ self.name  