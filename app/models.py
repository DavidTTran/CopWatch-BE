import datetime
from sqlalchemy import Column, Integer, DateTime
from app import db

class Report(db.Model):
    __tablename__ = 'reports'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String())
    city = db.Column(db.String())
    state = db.Column(db.String())
    zip_code = db.Column(db.String())
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, description, city, state, zip_code):
        self.description = description
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id,
            'description': self.description,
            'city': self.city,
            'state':self.state,
            'zip_code':self.zip_code
        }
