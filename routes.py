from app import app,db
from flask import Flask, render_template,request,url_for,redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy
from models import Book,User
from flask_login import UserMixin, LoginManager, login_required, login_user, current_user
import forms


login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    if current_user:
        return render_template('index.html', current_user = current_user)
    else:
        return render_template('index.html')

@app.route('/books',methods=["GET","POST"])
def books():
    BOOKS_PER_PAGE = 5
    page = request.args.get('page', 1, type=int)
    books = Book.query.paginate(page,BOOKS_PER_PAGE,False)
    next_url = url_for('books', page=books.next_num) \
        if books.has_next else None
    prev_url = url_for('books', page=books.prev_num) \
        if books.has_prev else None
    return render_template('books.html',book_list = books.items,next_url = next_url, prev_url = prev_url)

@app.route('/add_book',methods=["GET","POST"])
def add_book():
    bookform = forms.BookForm()
    if bookform.validate_on_submit():
        new_book = Book(title = bookform.title.data, author = bookform.author.data, rating = int(bookform.rating.data), genre = (bookform.genre.data))
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

@app.route('/register',methods=["GET","POST"])
def register():
    userform = forms.UserForm()
    if userform.validate_on_submit():
        new_user = User(username=userform.username.data,email=userform.email.data)
        new_user.encode_password(userform.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("index", _external=True, _scheme='http'))
    return render_template ('register.html',template_form = userform)

@app.route('/login',methods=["GET","POST"])
def login():
    userform = forms.LogInForm()
    if userform.validate_on_submit():
        user = User.query.filter_by(email = userform.email.data).first()
        if user and user.decode_password(userform.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index', _external=True, _scheme='http'))
        else:
            return redirect(url_for('login', _external=True, _scheme='http'))
    return render_template('login.html', template_form=userform)
   