import datetime
from sqlalchemy import Column, Integer, DateTime
from app import db

class Report(db.Model):
    __tablename__ = 'reports'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String())
    badge_number = db.Column(db.String())
    officer_name = db.Column(db.String())
    parties = db.Column(db.String())
    city = db.Column(db.String())
    state = db.Column(db.String())
    zip_code = db.Column(db.String())
    created_date = Column(db.String())
    image = Column(db.Text())

    def __init__(self,
                 description,
                 city,
                 state,
                 zip_code,
                 officer_name,
                 created_date,
                 badge_number,
                 parties,
                 image):
        self.description = description
        self.badge_number = badge_number
        self.officer_name = officer_name
        self.parties = parties
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.created_date = created_date
        self.image = image

    def __repr__(self):
        return 'id: {}'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'description': self.description,
            'badge_number': self.badge_number,
            'officer_name': self.officer_name,
            'parties': self.parties,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'created_date': self.created_date,
            'image': self.image
        }
