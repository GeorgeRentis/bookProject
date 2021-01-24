from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField,validators

# In this file we are going to create the forms that the application will be using.

class BookForm(FlaskForm):
    title = StringField("Book Title",[validators.DataRequired()])
    author = StringField("Book Author",[validators.DataRequired()])
    rating =  SelectField("Book Rating",choices=[(1,'Terrible'),(2,'Poor'),(3,'Decent'),(4,'Very Good'),(5,'Amazing')])
    genre =  SelectField("Book Genre",choices=[('Fantasy','Fantasy'),('Horror','Horror'),('Mystery','Mystery'),
    ('Romance','Romance'),('Literature','Literature')])

    submit = SubmitField("Add Book")