from app import app,db

# In this file we are going to create the models and their fields that the application will be using.

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(40),index=True,unique=True)
    author = db.Column(db.String(40),index=True,unique = False)
    rating = db.Column(db.Integer, index = True,unique = False)
    
    def __repr__(self):
        return "{} by {}".format(self.title,self.author)