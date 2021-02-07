from app import app,db
from flask import Flask, render_template,request,url_for,redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy
from models import Book,User
from flask_login import UserMixin, LoginManager, login_required, login_user, current_user,logout_user
import forms
import sys


login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/',methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        # print(current_user.username, file=sys.stdout)
        return render_template('index.html', current_user = current_user)
    return render_template('index.html')

@app.route('/books',methods=["GET","POST"])
def books():
    # BOOKS_PER_PAGE = 5
    # page = request.args.get('page', 1, type=int)
    # books = Book.query.paginate(page,BOOKS_PER_PAGE,False)
    # next_url = url_for('books', page=books.next_num) \
    # if books.has_next else None
    # prev_url = url_for('books', page=books.prev_num) \
    # if books.has_prev else None
    books = Book.query.filter(Book.username=="Georent").all()
    return render_template('books.html',book_list = books)



@app.route('/add_book',methods=["GET","POST"])
@login_required
def add_book():
    if current_user.is_authenticated:
        bookform = forms.BookForm()
        if bookform.validate_on_submit():
            new_book = Book(title = bookform.title.data, author = bookform.author.data, rating = int(bookform.rating.data), genre = (bookform.genre.data),username = current_user.username,review=(bookform.review.data))
            db.session.add(new_book)
            db.session.commit()
            flash('You successfully added a book','error')
            return redirect(url_for("user_books", _external=True, _scheme='http'))
        return render_template('add_book.html',template_form = bookform)
    else:
        flash('You have to be logged in to view this option','error')
        return render_template('index.html')


@app.route('/user/books',methods=["GET","POST"])
@login_required
def user_books():
    # BOOKS_PER_PAGE = 5
    # page = request.args.get('page', 1, type=int)
    # books = Book.query.paginate(page,BOOKS_PER_PAGE,False)
    # next_url = url_for('books', page=books.next_num) \
    # if books.has_next else None
    # prev_url = url_for('books', page=books.prev_num) \
    # if books.has_prev else None
    books = Book.query.filter(Book.username == current_user.username).all()
    return render_template('user_books.html',book_list = books)

@app.route('/book/<int:book_id>')
def book(book_id):
    book = Book.query.get(book_id)
    return render_template('book.html',book = book)

@app.route('/user/delete/<int:book_id>')
@login_required
def delete(book_id):
    db.session.delete(Book.query.get(book_id))
    db.session.commit()
    flash('You have successfully removed the book!','error')
    return redirect(url_for('user_books', _external=True, _scheme='http'))

# @app.route('/update/<int:book_id>',methods=["GET","POST"])
# def update(book_id):
#     bookform = forms.BookForm()
#     book = Book.query.get(book_id)
#     if bookform.validate_on_submit():
#         book.title = bookform.title.data
#         book.author = bookform.author.data
#         db.session.commit()      
#     return render_template('book_update.html',template_form = bookform,book = book)

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
            flash('You were successfully logged in','error')
            return redirect(next_page) if next_page else redirect(url_for('index', _external=True, _scheme='http'))
        else:
            return redirect(url_for('login', _external=True, _scheme='http'))
    return render_template('login.html', template_form=userform)
   

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were successfully logged out','error')
    return redirect(url_for('index'))


@app.route("/admin")
@login_required
def admin():
    if current_user.is_authenticated and current_user.is_admin==True:
        books = Book.query.all()
        users = User.query.all()
        total_books = len(books)
        total_users = len(users)
        horror_books = len(Book.query.filter(Book.genre == "Horror").all())
        romance_books = len(Book.query.filter(Book.genre == "Romance").all())
        mystery_books = len(Book.query.filter(Book.genre == "Mystery").all())
        literature_books = len(Book.query.filter(Book.genre == "Literature").all())
        fantasy_books = len(Book.query.filter(Book.genre == "Fantasy").all())
        graphic_novel_books = len(Book.query.filter(Book.genre == "Graphic Novel").all())
        terrible_books = len(Book.query.filter(Book.rating == 1).all())
        poor_books = len(Book.query.filter(Book.rating == 2).all())
        decent_books = len(Book.query.filter(Book.rating == 3).all())
        very_good_books = len(Book.query.filter(Book.rating == 4).all())
        amazing_books = len(Book.query.filter(Book.rating== 5).all())

        return render_template('admin.html',total_books=total_books,total_users = total_users,horror_books = horror_books,romance_books=romance_books,
        mystery_books = mystery_books, literature_books = literature_books, fantasy_books = fantasy_books,garphic_novel_books = graphic_novel_books,
        poor_books = poor_books,terrible_books=terrible_books,decent_books=decent_books,very_good_books=very_good_books,amazing_books=amazing_books)

@app.route("/admin/books")
@login_required
def admin_books():
    if current_user.is_authenticated and current_user.is_admin==True:
        book_list = Book.query.all()
        return render_template('admin_books.html',book_list = book_list)

@app.route("/admin/books/<int:book_id>",methods=["GET","POST"])
@login_required
def admin_update(book_id):
    if current_user.is_authenticated and current_user.is_admin==True:
        bookform = forms.UpdateBookForm()
        book = Book.query.get(book_id)
        if bookform.validate_on_submit():
            book.title = bookform.title.data
            book.author = bookform.author.data
            book.review = bookform.review.data
            book.rating = int(bookform.rating.data)
            db.session.commit()      
        return render_template('book_update.html',template_form = bookform,book = book)

