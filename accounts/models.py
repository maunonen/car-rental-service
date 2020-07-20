from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserProfile (models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    phone_number = models.CharField(max_length=30, default='')
    town = models.CharField( max_length=50, default='' )    
    postal_code = models.CharField( max_length=10, default='')  
    address = models.CharField( max_length=200, default='' )    

    def __str__(self): 
        return self.user.username 

""" @receiver(post_save, sender=User)
def create_profile(sender, **kwargs): 
    if kwargs['created']:    
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
 """
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

""" post_save.connect(create_user_profile, sender=User )
post_save.connect(save_user_profile, sender=User ) """