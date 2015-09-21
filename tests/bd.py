import peewee
from peewee import MySQLDatabase, Model

db = MySQLDatabase('mestrado', user='mestrado',passwd='mestrado')

def before_request_handler():
    db.connect()

def after_request_handler():
    db.close()

class Book(Model):
    author = peewee.CharField()
    title = peewee.TextField()

    class Meta:
        database = db

Book.create_table()
book = Book(author="me", title='Peewee is cool')
book.save()
for book in Book.filter(author="me"):
    print book.title