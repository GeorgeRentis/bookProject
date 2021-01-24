from flask import Flask, render_template,request,url_for,redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy
import forms


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecret'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

db = SQLAlchemy(app)
from models import Book


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books',methods=["GET","POST"])
def books():
    return render_template('books.html',book_list = Book.query.all())

@app.route('/add_book',methods=["GET","POST"])
def add_book():
    bookform = forms.BookForm()
    if bookform.validate_on_submit():
        new_book = Book(title = bookform.title.data, author = bookform.author.data, rating = int(bookform.rating.data))
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("books", _external=True, _scheme='http'))
    return render_template('add_book.html',template_form = bookform)

@app.route('/book/<int:book_id>')
def book(book_id):
    book = Book.query.get(book_id)
    return render_template('book.html',book = book)

@app.route('/delete/<int:book_id>')
def delete(book_id):
    db.session.delete(Book.query.get(book_id))
    db.session.commit()
    return render_template('books.html',book_list = Book.query.all())

@app.route('/update/<int:book_id>',methods=["GET","POST"])
def update(book_id):
    bookform = forms.BookForm()
    book = Book.query.get(book_id)
    if bookform.validate_on_submit():
        book.title = bookform.title.data
        book.author = bookform.author.data
        db.session.commit()
        
    return render_template('book_update.html',template_form = bookform,book = book)