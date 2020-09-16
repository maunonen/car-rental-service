'/^(0[1-9]|[12]\d|3[01])(0[1-9]|1[0-2])([5-9]\d\+|\d\d-|[01]\dA)\d{3}[\dABCDEFHJKLMNPRSTUVWXY]$/' 

  ## activate virtual env 
    470  mkdir btre_project
    471  ls
    472  cd btre_project/
    473  ls
    474  pip3 freeze
  ## create virtual env
    475  python3 -m venv ./venv
    476  ls -la
    477  pwd
  ## activate vir env
    478  source ./venv/bin/activate

  switch to 

  ## install Django 
    486  python -m pip install Django

  ## Create project 
    490  django-admin start startproject btre .

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
    644  python manage.py collectstatic

  ## add /static folder to .gitignore

  # install drivers for postgres on django venv 
    514  pip install psycopg2
    515  pip install psycopg2-binary

  # run migration 
    518  python manage.py migrate

  # Make migration files 
    521  python manage.py makemigrations 
    
## Initial migration for app 
     624  python manage.py makemigrations courses
# in case of error install Pillow
      522  pip install Pillow
## pylint for django 
    545  pip install pylint-django


Deploy to hepythooku 

0. turn of debug mode in setting file

1. login to heroku 
2. Create .gitignore
3. install gunicorn 
    504  pip install gunicorn
4. Create requirements file 
    507  pip freeze > requirements.txt
5. Create git repositary
    git init 
6. Modify .gitignore
7. add file to local repositary and do commit 
    515  git add .
    517  git commit -m 'Initial commit'
8. Create heroku app 
    519  heroku create lds-project-django
9. Code to heroku 
    521  git push heroku master 
10. Track error 
    499  heroku logs --tail
11. Create Procfile in the root of project 
    touch Procfile
12. Specify wsgi file location in Procfile 
    web: gunicorn lds.wsgi
13. Commit changes and run heroku 
    504  git add .
    505  git commit -m 'Added Procfile'
    506  git push heroku master     
14. Generate secret token 
    python3
    >>> import secrets
    >>> secrets.token_hex(24)
    
15. Set to bash_profile 
16. Set local nev to heroku and modify setting file 
17. Add postgresql Database addons ot heroku 
    heroku addons:create heroku-postgresql:hobby-dev
18. Check used addons
    533  heroku addons  
19. Check Postgresql setting 
    heroku pg
20. Install heroku helper function for using Databases 
    537  pip install django-heroku 
21. Add import heroku module to setting.py file
    import django_heroku
    django_heroku.settings(locals())
22. Update requirements file
    540  pip freeze > requirements.txt
23. run migration on heroku 
    547  heroku run python  manage.py migrate
24. run bash terminal on heroku 
    549  heroku run bash 
35. create super user 
    python manage.py createsuperuser
36. show heroku release and rollback 
    555 heroku releases
    556 heroku rollback v10 

Django translation

1. Create po file for Language translation
    529  python manage.py makemessages -l ru -i venv
    537  python manage.py compilemessages --ignore venv

SASS 

  513  sass --watch lds/static/scss/style.scss lds/static/css/style.css 

