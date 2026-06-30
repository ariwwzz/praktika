from sqlalchemy.orm import Session
from . import models

def create_category(db: Session, title: str):
    new_category = models.Category(title=title)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def get_categories(db: Session):
    return db.query(models.Category).all()

def get_category_by_id(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def create_book(db: Session, title: str, description: str, price: float, category_id: int, url: str = ""):
    new_book = models.Book(
        title=title,
        description=description,
        price=price,
        url=url,
        category_id=category_id
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def get_books(db: Session):
    return db.query(models.Book).all()

def get_books_by_category(db: Session, category_id: int):
    return db.query(models.Book).filter(models.Book.category_id == category_id).all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()










    #UPDATE для категорий
def update_category(db, category_id, new_title):
    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if category:
        category.title = new_title
        db.commit()
        db.refresh(category)
    return category

#DELETE для категорий
def delete_category(db, category_id):
    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if category:
        db.delete(category)
        db.commit()
    return category

#UPDATE для книг
def update_book(db, book_id, title, description, price, category_id):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book:
        book.title = title
        book.description = description
        book.price = price
        book.category_id = category_id
        db.commit()
        db.refresh(book)
    return book

#DELETE для книг
def delete_book(db, book_id):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
    return book