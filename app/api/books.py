from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.db import SessionLocal
from app.db import crud
from app.schemas import BookCreate, BookUpdate, BookResponse

router = APIRouter(prefix="/books", tags=["Books"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[BookResponse])
def get_books(
    category_id: Optional[int] = Query(None, description="Фильтр по категории"),
    db: Session = Depends(get_db)
):
    if category_id:
        return crud.get_books_by_category(db, category_id)
    return crud.get_books(db)

@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book

@router.post("/", response_model=BookResponse, status_code=201)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    category = crud.get_category_by_id(db, book.category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    
    return crud.create_book(
        db,
        title=book.title,
        description=book.description,
        price=book.price,
        category_id=book.category_id,
        url=book.url or ""
    )

@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    
    updated = crud.update_book(
        db,
        book_id,
        title=book.title,
        description=book.description,
        price=book.price,
        category_id=book.category_id,
        url=book.url  
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return updated

@router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    
    deleted = crud.delete_book(db, book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return None