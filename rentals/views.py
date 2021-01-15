from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext as _ 
from django.contrib import messages
from .forms import RentalForm
from datetime import date, datetime



from .models import Rental, Option, Specification
from cars.models import *
from django.contrib.auth.decorators import login_required

#import for mail notification 
from django.core.mail import send_mail, BadHeaderError
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


# Create your views here.

def calcSummary(car, rental_start, rental_end): 
   
  """ count rental sum  """
  """ get rental interval  """ 
  rental_start_date = datetime.strptime(rental_start, '%Y-%m-%d')
  rental_end_date = datetime.strptime(rental_end, '%Y-%m-%d')
  interval = (rental_end_date - rental_start_date).days
  
  """ get rental price from car table  """
  # if interval > 7 total_price = interval * week price 
  if interval > 7  and interval < 30 : 
      rental_price = car.price_week 
  # if interval < 7 total_price = interval * day price 
  elif interval <= 7: 
      rental_price = car.price_day
  # if interval > 30 total_price = interval * month_price 
  elif interval >= 30: 
      rental_price = car.price_month
  # count rental_price 
  if rental_price and interval: 
      rental_sum = interval * rental_price
  else : 
      rental_sum = None
  return rental_sum

@login_required(login_url='/accounts/login')
def index (request): 
    user = request.user
    rentals = Rental.objects.filter(user=user)
    context = {     
        'rentals' : rentals
    }
    return render(request, 'rentals/rentals.html', context )

def add(request, car_id, rental_start, rental_end):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST' or None: 
        print('Create form')
        form = RentalForm(request.POST)
        print('Validate form')
        if form.is_valid():
            #rental_start = form.cleaned_data.get('rental_start')
            #rental_end = form.cleaned_data.get('rental_end')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')
            usage_place = form.cleaned_data.get('usage_place')
            pickup_location = form.cleaned_data.get('pickup_location')
            town = form.cleaned_data.get('town')
            address = form.cleaned_data.get('address')
            postal_code = form.cleaned_data.get('postal_code')
            comments = form.cleaned_data.get('comments')
            conditions = form.cleaned_data.get('conditions')
            print('Save to model')
            rental_sum = calcSummary(car, rental_start, rental_end )
            rental = Rental(
                car = car, 
                rental_start = rental_start, 
                rental_end = rental_end, 
                first_name = first_name,  
                last_name = last_name,  
                email = email, 
                phone_number = phone_number, 
                usage_place = usage_place, 
                pickup_location = pickup_location, 
                town = town, 
                address = address, 
                postal_code = postal_code, 
                comments = comments, 
                rental_sum = rental_sum, 
                condition_approved = conditions
            )
            if request.user.is_authenticated:
                rental.user = request.user
            rental.save()
            
            """ create List of option from POST REQUEST """
            options = request.POST.getlist('option')

            if options:
              """ get option object from DB """
              options = Option.objects.filter(pk__in=options)
              if options: 
                """ count interval in days """
                interval = (rental_end - rental_start).days

                """ create Specification for Rental """
                for option in options:
                  """ spec = Specification.objects.create(option_id=option, rental=rental) """
                  """ calculate sum of Rentals """
                  price = option.price * interval
                  """ create spicification object  """
                  spec = Specification.objects.create(option=option, rental=rental, price=price, day=interval)

            try:  
                context_client = {
                    'car' : car, 
                    'rental_start' : rental_start, 
                    'rental_end' : rental_end, 
                    'first_name' : first_name,  
                    'last_name' : last_name,  
                }
                # html message Version 
                html_message_client = render_to_string('email/client/new_rental.html', context=context_client)
                # txt message VVersion
                subject_client = f'Your have successfully rent a car: {car}!'
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
            except BadHeaderError:
                print(BadHeaderError)
            
            # send mail notification to admin
            try: 

                # link to template 
                context = {
                    'car' : car , 
                    'rental_start' : rental_start, 
                    'rental_end' : rental_end, 
                    'first_name' : first_name,  
                    'last_name' : last_name,  
                    'email' : email, 
                    'phone_number' : phone_number, 
                    'comments' : comments, 
                    'rental_sum': 123, 
                }
                html_message = render_to_string('email/admin/new_rental.html', context=context)
                # txt version of message
                subject = f'You have new order { first_name}, { last_name} in { car }'
                plain_message = strip_tags(html_message)
                #send notification to admin 
                mail.mail_admins(
                    subject, 
                    plain_message, 
                    fail_silently=False,
                    connection=None, 
                    html_message=html_message, 
                )
            except BadHeaderError :
                print(BadHeaderError)
            
            # form notification 
            messages.success(request, 'you have successfully rented car')
            return redirect('cars')
        else: 
          print('Form not valid')
          ## default language
          language = 'fi'
          ## check current language 
          if request.LANGUAGE_CODE: 
              language = request.LANGUAGE_CODE
          ## get content from database by page name and language
          try :
            """ get all available option by using language  """
            options = Option.objects.all().filter(language=language)
          # Object  not found  
          except ObjectDoesNotExist:
              options = ''
          if not options: 
            options = ''
          context = {
            'car' : car, 
            'form' : form, 
            'options' : options, 
            'rental_start' : rental_start, 
            'rental_end' : rental_end 
          }
          return render(request, 'rentals/rental.html', context)
    else: 
        ## default language
        language = 'fi'
        ## check current language 
        if request.LANGUAGE_CODE: 
            language = request.LANGUAGE_CODE
        ## get content from database by page name and language
        try :
          """ get all available option by using language  """
          """ options = Option.objects.all().filter(language__iexact=language) """
          options = Option.objects.all().filter(language=language)
        # Object  not found  
        except ObjectDoesNotExist:
            options = ''
        if not options: 
            options = ''

        if request.user.is_authenticated:
            user = request.user
            initial = {
                'rental_start' : rental_start,
                'rental_end' : rental_end,
                'usage_place' : 'Helsinki',
                'pickup_location' : 'Helsinki',
                'comments' : '', 
                'last_name' : user.last_name ,
                'first_name' : user.first_name ,
                'email' : user.email ,
                'phone_number' : user.userprofile.phone_number if user.userprofile.phone_number else '' ,
                'town' : user.userprofile.town if user.userprofile.town else '' ,
                'postal_code' : user.userprofile.postal_code if user.userprofile.postal_code else '' ,
                'address' : user.userprofile.address if user.userprofile.address else '' ,
                'conditions' : '', 
                'rental_sum' : '123', 
            }
            form = RentalForm(initial)
        else :
            form = RentalForm()
        rental_sum = calcSummary( car, rental_start, rental_end)
        context = {
          'car' : car, 
          'form' : form, 
          'options' : options, 
          'rental_start' : rental_start, 
          'rental_end' : rental_end, 
          'rental_sum' : rental_sum
        }
        return render(request, 'rentals/rental.html', context)
