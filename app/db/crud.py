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