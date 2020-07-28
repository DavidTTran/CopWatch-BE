import os
from app import app, db, _cors_response
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from app.models.report import Report
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import cloudinary
import cloudinary.uploader
import cloudinary.api
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.environ.get('DATABASE_URL'))
Session = sessionmaker(bind=engine)
session = Session()

class ReportRoutes:

    @app.route("/api/v1/reports", methods=['GET'])
    def all_reports():
        reports = Report.query \
            .order_by(Report.created_date.desc()) \
            .all()

        return jsonify([e.serialize() for e in reports])

    @app.route("/api/v1/reports/new", methods=['POST'])
    def new_report():
        json = request.get_json()
        report = Report(description=json['description'],
                   zip_code=json['zip_code'],
                   city=json['city'],
                   state=json['state'],
                   officer_name=json['officer_name'],
                   badge_number=json['badge_number'],
                   parties=json['parties'],
                   created_date=json['created_date'],
                   image=json['image'])

        session.add(report)
        session.commit()

        return _cors_response(jsonify(report.serialize()))

    @app.route("/api/v1/upload", methods=['POST'])
    def upload_file():
        cloudinary.config(
            cloud_name = os.environ.get("CLOUDINARY_NAME"),
            api_key = os.environ.get("CLOUDINARY_API"),
            api_secret = os.environ.get("CLOUDINARY_SECRET")
            )

        json = request.get_json()
        image = cloudinary.uploader.upload(json['image'],
            folder = "copwatch",
            unique_filename = True)

        return _cors_response(response.text(image))
