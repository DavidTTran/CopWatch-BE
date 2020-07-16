## Setup
### Install python

`$ brew install python`

### Setting up virtual environment

`$ git clone git@github.com:DavidTTran/CopWatch-BE.git`

`$ cd CopWatch-BE`

`$ python3 -m pip install virtualenv`

`$ virtualenv venv -p python3`

`$ source venv/bin/activate` Make sure that your CLI has `(venv)` prepending your file location

`$ pip install django`

### Setting up database

`$ psql`

`$ CREATE DATABASE copwatch;`

`$ \du` Make sure you have a superuser named `postgres`

`$ \q` To exit psql

### Running server locally

`$ cd /CopWatch-BE` (Root directory)

`$ source venv/bin/activate` so that your CLI has `(venv)` before your file location

`$ python manage.py runserver`

Visit `localhost:8000`

### You may need to install django_heroku

`$ pip install django_heroku`

### To deactivate the virtual environment (if your CLI has `(venv)` in front)
`$ deactivate`
