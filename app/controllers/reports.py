from app import app, db
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from app.models.report import Report

class ReportRoutes:
    @app.route("/api/v1/reports")
    def all_reports():
        try:
            reports = Report.query.all()
            return jsonify([e.serialize() for e in reports])
        except Exception as e:
            return(str(e))

    @app.route("/api/v1/reports/new")
    def new_report():
        return "successful connection"
