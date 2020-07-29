# CopWatch-BE
[Front-end Repo](https://github.com/oliviacweb/CopWatch-FE)

[Back-end Repo](https://github.com/DavidTTran/CopWatch-BE)

# Setup

### Clone down the repo
`$ git clone git@github.com:DavidTTran/CopWatch-BE.git`

`$ cd CopWatch-BE`

### Setup virtual environment
`$ virtualenv venv`

`$ source venv/bin/activate`

### Install Flask and necessary libraries
Within your virtual environment
`$ pip install -r requirements.txt`

### Setup .env
`$ touch .env`

Append the following to your .env file
Sign up for Cloudinary at https://cloudinary.com/
```
APP_SETTINGS="config.DevelopmentConfig"
DATABASE_URL="postgresql://localhost/copwatch"

CLOUDINARY_NAME=(your cloudinary app name)
CLOUDINARY_API=(your api key)
CLOUDINARY_SECRET=(your secret key)
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

# Current Endpoints

## Returns all of the reports in the Database sorted by most recent.
`localhost:5000/api/v1/reports`

## Creates a new report with information passed through the body in JSON
`localhost:5000/api/v1/reports/new`

#### Example of request body
```
{
  "description": "Example incident report",
  "parties": "James Family",
  "city": "Denver",
  "state": "Colorado",
  "zip_code": "80104",
  "badge_number": "12312-112",
  "officer_name": "O'Haris",
  "created_date": "Tue, Jul 21, 2020 6:19 PM",
  "image": "imagehost.example/123.jpg"
}
```

## Allows an image to be uploaded
 `localhost:5000/api/v1/upload`
 
#### Example of request body
```
{
  "image": { local image URI }
}
```

# Testing
`$ pip install pytest`

`$ pip install coverage`

### Without Coverage Report

`$ pytest`

### With Coverage Report

`$ coverage run -m pytest`

`$ coverage html --omit="*/venv*"`

`$ open htmlcov/index.html`

## Contributors
[David Tran](https://github.com/DavidTTran)

[Dave Pernitz](https://github.com/pernstrong)

[Ben Fox](https://github.com/benfox1216)

[Karl Nielsen](https://github.com/Karlfunhouse)

[Olivia Webster](https://github.com/oliviacweb)
