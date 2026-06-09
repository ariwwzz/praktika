from app.db.db import SessionLocal, engine, Base
from app.db import crud, models

Base.metadata.create_all(bind=engine)

db = SessionLocal()

print("Добавляем категории...")

cat1 = crud.create_category(db, "Художественная литература")
cat2 = crud.create_category(db, "Научная литература")

print(f"Созданы категории: {cat1.title}, {cat2.title}")

print("\nДобавляем книги...")

crud.create_book(db, "Война и мир", "Роман-эпопея Льва Толстого", 500.0, cat1.id)
crud.create_book(db, "Преступление и наказание", "Роман Достоевского", 450.0, cat1.id)
crud.create_book(db, "Мастер и Маргарита", "Роман Булгакова", 480.0, cat1.id)

crud.create_book(db, "Краткая история времени", "Стивен Хокинг", 600.0, cat2.id)
crud.create_book(db, "Эгоистичный ген", "Ричард Докинз", 550.0, cat2.id)

print("Книги добавлены!")

db.close()
print("\nБаза данных инициализирована!")