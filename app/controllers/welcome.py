from app import app, db
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

class WelcomeRoutes:
    @app.route("/")
    def hello_world():
        return "Hello World!"
