import os
from app import app, db, _cors_response
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from app.models.report import Report
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from werkzeug import secure_filename

engine = create_engine(os.environ['DATABASE_URL'])
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
                   created_date=json['created_date'])

        session.add(report)
        session.commit()

        return _cors_response(jsonify(report.serialize()))

    @app.route("/api/v1/uploader", methods=['POST'])
    def upload_file():
        file = request.files['file']
        saved_name = file.save(secure_filename(file.filename))
        return saved_name
