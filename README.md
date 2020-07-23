# CopWatch-BE

# Setup

### Clone down the repo
`$ git clone git@github.com:DavidTTran/CopWatch-BE.git`

`$ cd CopWatch-BE`

### Setup virtual environment
`$ virtualenv venv`

`$ source venv/bin/activate`

### Install Flask and necessary libraries
Within your virtual environment
`$ pip install Flask`

`$ pip install flask_sqlalchemy`

`$ pip install flask_script`

`$ pip install flask_migrate`

`$ pip install psycopg2-binary`

### Setup .env
`$ touch .env`

Append the following to your .env file
```
APP_SETTINGS="config.DevelopmentConfig"
DATABASE_URL="postgresql://localhost/copwatch"
```

### Setup Database and necessary libraries
`$ psql`

`$ CREATE DATABASE copwatch;`

`$ \q`

### Running migrations
`$ export APP_SETTINGS="config.DevelopmentConfig"`

`$ export DATABASE_URL="postgresql://localhost/copwatch"`

`$ python manage.py db init`

`$ python manage.py db migrate`

`$ python manage.py db upgrade`

### Run server locally
`$ python manage.py runserver`

Visit at `localhost:5000`

## Current Endpoints

`localhost:5000/api/v1/reports`

## Testing
`$ pip install pytest`

`$ pytest`
