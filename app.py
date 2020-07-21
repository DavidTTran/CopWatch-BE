from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Report

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/v1/reports")
def test():
    return "endpoint successful"

@app.route("/details")
def get_book_details():
    author=request.args.get('author')
    published=request.args.get('published')
    return "Author : {}, Published: {}".format(author,published)

if __name__ == '__main__':
    app.run()
