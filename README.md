## Setup
### Install python

`$ brew install python`

### Python/Django require a virtual environment to be setup

`$ python3 -m pip install virtualenv`

`$ virtualenv venv -p python3`

`$ source venv/bin/activate`

`$ pip install django`

### Setting up database

`$ psql`

`$ CREATE DATABASE copwatch;`

`$ \du` Make sure you have a superuser named `postgres`

### Running server locally

`$ cd CopWatchBE`

`$ source venv/bin/activate` so that your CLI has `(venv)` before your file location

`$ python manage.py runserver`

Visit `localhost:8000`

### To deactivate the virtual environment (if your CLI has `venv` in front)
`$ deactivate`
