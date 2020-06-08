  
## activate virtual env 
    470  mkdir btre_project
    471  ls
    472  cd btre_project/
    473  ls
## list of packages 
    474  pip3 freeze
  ## create virtual env
    475  python3 -m venv ./venv
    476  ls -la
    477  pwd
## activate vir env
    478  source ./venv/bin/activate
## deactivate venv 
    504  deactivate     

## install Django 
    486  python -m pip install Django

## Create project 
    490  django-admin start startprojectdeac lds .

## run http server 
    503  python manage.py runserver

## Create new app
    493  python manage.py startapp pages

## add new app to settings.app INSTALLED_APPS 'pages.apps.PagesConfig'

## add new url to urls.py on the root foldet of project 
    path('', include('pages.urls')), 
  
## create urls.py and add new url to urls.py on Pages App path('', views.index, name='index')
      

## add new method to def views.py 
    index(request):
      return HttpResponse('<h1>Hello world</h1>')

## Put all static content (css, html, js, img) in btre folder 

## collect main static content from project to static folder on the root project 
    507  python manage.py collectstatic

## add /static folder to .gitignore

# install drivers for postgres on django venv 
    514  pip install psycopg2
    515  pip install psycopg2-binary

# run migration 
    518  python manage.py migrate

# Make migration files 
    521  python manage.py makemigrations 
    # in case of error install Pillow
      522  pip install Pillow
## pylint for django 
    545  pip install pylint-django