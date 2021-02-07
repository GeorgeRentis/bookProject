from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField,validators,PasswordField,TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo

# In this file we are going to create the forms that the application will be using.

class BookForm(FlaskForm):
    title = StringField("Book Title",validators=[DataRequired()])
    author = StringField("Book Author",validators=[DataRequired()])
    rating =  SelectField("Book Rating",choices=[(1,'Terrible'),(2,'Poor'),(3,'Decent'),(4,'Very Good'),(5,'Amazing')])
    genre =  SelectField("Book Genre",choices=[('Fantasy','Fantasy'),('Horror','Horror'),('Mystery','Mystery'),
    ('Romance','Romance'),('Literature','Literature'),('Graphic Novel','Graphic Novel')])
    review = TextAreaField("Your Review (Max 120 characters)",validators=[DataRequired()])
    submit = SubmitField("Add Book")

class UserForm(FlaskForm):
    username = StringField("Username",validators=[DataRequired()])
    email = StringField("Email Address",validators = [DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired()])
    password2 = PasswordField("Repeat Password",validators = [DataRequired(),EqualTo('password')])
    submit = SubmitField("Add User")

class LogInForm(FlaskForm):
    email = StringField("Email Address",validators = [DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField("Log In")

class UpdateBookForm(FlaskForm):
    title = StringField("Book Title",validators=[DataRequired()])
    author = StringField("Book Author",validators=[DataRequired()])
    rating =  SelectField("Book Rating",choices=[(1,'Terrible'),(2,'Poor'),(3,'Decent'),(4,'Very Good'),(5,'Amazing')])
    genre =  SelectField("Book Genre",choices=[('Fantasy','Fantasy'),('Horror','Horror'),('Mystery','Mystery'),
    ('Romance','Romance'),('Literature','Literature'),('Graphic Novel',"Graphic Novel")])
    review = TextAreaField("Your Review (Max 120 characters)",validators=[DataRequired()])
    submit = SubmitField("Update")