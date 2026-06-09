from app.db.db import SessionLocal
from app.db import crud

db = SessionLocal()

print("=" * 50)
print("СПИСОК КАТЕГОРИЙ")
print("=" * 50)

categories = crud.get_categories(db)
for cat in categories:
    print(f"{cat.id}. {cat.title}")
    books = crud.get_books_by_category(db, cat.id)
    for book in books:
        print(f"   - {book.title} ({book.price} руб.)")
        if book.description:
            print(f"     Описание: {book.description[:50]}...")
    print()

print("=" * 50)
print("ВСЕ КНИГИ")
print("=" * 50)

all_books = crud.get_books(db)
for book in all_books:
    print(f"'{book.title}' - категория: {book.category.title} - {book.price} руб.")

db.close()