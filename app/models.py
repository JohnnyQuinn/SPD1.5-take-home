from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    """User Model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(30), nullable=False)

# TODO: create Mood class model 
