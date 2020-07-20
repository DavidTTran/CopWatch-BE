# CopWatch-BE

# Setup

### Clone down the repo
`$ git clone git@github.com:DavidTTran/CopWatch-BE.git`
`$ cd CopWatch-BE`

### Setup virtual environment
`$ virtualenv venv`
`$ source venv/bin/activate`

### Install Flask
Within your virtual environment
`$ pip install Flask`
`$ pip install flask_sqlalchemy

### Setup Database and necessary libraries
`$ psql`
`$ CREATE DATABASE copwatch`
`$ \q`

`$ pip install flask_sqlalchemy`
`$ pip install flask_script`
`$ pip install flask_migrate`
`$ pip install psycopg2-binary`

### Running migrations
`$ python manage.py db init`
`$ python manage.py db migrate`
`$ python manage.py db upgrade`

### Run server locally
`$ python manage.py runserver`
