from app import app,db
from models import Book,User

b1 = Book(id=1,title = 'The Lord Of The Rings',author='J.R.R. Tolkien',rating=5, genre='Fantasy',username="Georent",
review = "The father of all fantasy novels, unmissable.")
b2 = Book(id=2,title='A Game Of Thrones', author='G.R.R. Martin',rating=5, genre='Fantasy', username ="Georent",
review = "You never know what to expect from this book.")
b3 = Book (id=3, title='Elantris', author = 'Brandon Sanderson',rating=4, genre ='Fantasy', username ="Georent",
review = "I don't remember much but it is a good book!")
b4 = Book (id=4, title = "Salem's Lot", author = 'Stephen King',rating=5, genre='Horror', username = "Georent",
review = "Best horror story out there not featuring a clown")
b5 = Book (id=5, title = "Cujo", author = 'Stephen King',rating=3, genre='Horror', username = "Georent",
review = "What a cute dog!")
b6 = Book (id=6, title = "The Stand", author = 'Stephen King',rating=4, genre='Horror', username = "Georent",
review = "A battle between good and evil")
b7 = Book (id=7, title = "The IT", author = 'Stephen King',rating=5, genre='Horror', username = "Georent",
review = "Just Read it!!")
b8 = Book (id=8, title = "Watchmen", author = 'Alan Moore',rating=5, genre='Graphic Novel', username = "Georent",
review = "Best Graphic Novel Ever!")

admin_user =  User(id=1,username="Georent",email="georent123@hotmail.com",is_admin=True)
admin_user.encode_password("admin_password")

test_user =  User(id=2,username="JonDoe",email="jondoe@example.com",is_admin=False)
test_user.encode_password("user_password")

db.session.add(b1)
db.session.add(b2)
db.session.add(b3)
db.session.add(b4)
db.session.add(b5)
db.session.add(b6)
db.session.add(b7)
db.session.add(b8)
db.session.add(admin_user)
db.session.add(test_user)
db.session.commit()
