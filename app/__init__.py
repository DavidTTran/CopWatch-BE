import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

def _cors_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

from app.models.report import Report
from app.controllers.reports import ReportRoutes
from app.controllers.welcome import WelcomeRoutes

if __name__ == '__main__':
    app.run()
