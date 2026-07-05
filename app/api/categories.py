from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.db import SessionLocal
from app.db import crud
from app.schemas import CategoryCreate, CategoryUpdate, CategoryResponse

router = APIRouter(prefix="/categories", tags=["Categories"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)

@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = crud.get_category_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return category

@router.post("/", response_model=CategoryResponse, status_code=201)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category.title)

@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(category_id: int, category: CategoryUpdate, db: Session = Depends(get_db)):
    
    updated = crud.update_category(db, category_id, category.title)
    if not updated:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return updated

@router.delete("/{category_id}", status_code=204)
def delete_category(category_id: int, db: Session = Depends(get_db)):
   
    deleted = crud.delete_category(db, category_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return None