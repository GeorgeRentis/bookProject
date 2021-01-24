from app import app,db
from flask_login import UserMixin
from datetime import datetime

# In this file we are going to create the models and their fields that the application will be using.

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(40),index=True,unique=True)
    author = db.Column(db.String(40),index=True,unique = False)
    rating = db.Column(db.Integer, index = True,unique = False)
    genre = db.Column(db.Integer, index= True, unique = False)
    
    def __repr__(self):
        return "{} by {}".format(self.title,self.author)

# This is the User Model that will be used for the application.

class User(UserMixin,db.Model,):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120),index=True,unique=True)
    email = db.Column(db.String(120),index=True,unique=True)
    password_hash = db.Column(db.String(120))
    joined_at = db.Column(db.DateTime(),index=True,default = datetime.utcnow)

    def __repr__(self):
        return "Welcome {}!".format(self.username)