from app import app,db
from models import Book

b1 = Book(id=1,title = 'The Lord Of The Rings',author='J.R.R. Tolkien',rating=5, genre='Fantasy')
b2 = Book(id=2,title='A Game Of Thrones', author='G.R.R. Martin',rating=5, genre='Fantasy')
b3 = Book (id=3, title='Elantris', author = 'Brandon Sanderson',rating=5, genre ='Fantasy')
b4 = Book (id=4, title = "Salem's Lot", author = 'Stephen King',rating=5, genre='Horror')

db.session.add(b1)
db.session.add(b2)
db.session.add(b3)
db.session.add(b4)
db.session.commit()
