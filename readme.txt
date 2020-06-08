  
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


Deploy to heroku 

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
16. Set local nev to heroku 



