# praktika
# Book API

REST API для управления книгами и категориями.  
Проект написан на **FastAPI** с использованием **SQLAlchemy** и **PostgreSQL**.

---

## Как запустить проект

Шаг 1. Клонируйте репозиторий

```bash
git clone https://github.com/ariwwzz/praktika.git
cd praktika
```

Шаг 2. Откройте проект в VS Code
В терминале выполните:
```bash
code .
```
Или откройте VS Code, нажмите File → Open Folder... и выберите папку praktika.

Шаг 3. Откройте терминал в VS Code
В VS Code нажмите Terminal → New Terminal (или нажмите Ctrl + Shift + ~).

Шаг 4. Создайте виртуальное окружение
В терминале выполните:
```bash
python3 -m venv venv
```

Шаг 5. Активируйте виртуальное окружение
В терминале выполните:
```bash
source venv/bin/activate
```
Если в начале строки появилось (venv), значит, всё работает.

Шаг 6. Установите зависимости
В терминале выполните:
```bash
pip install -r requirements.txt
```
Дождитесь окончания установки.

Шаг 7. Создайте файл .env
В левой панели VS Code (Explorer) нажмите правой кнопкой мыши на пустое место, выберите New File и назовите его .env.
Откройте этот файл и вставьте:

DB_HOST=localhost
DB_PORT=5432
DB_NAME=octagon_db
DB_USER=octagon
DB_PASSWORD=12345

Сохраните файл (Ctrl + S).

Шаг 8. Установите PostgreSQL (если не установлен)
В терминале выполните:
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib -y
sudo service postgresql start
```

Шаг 9. Создайте пользователя и базу данных
В терминале выполните:
```bash
sudo -u postgres psql -c "CREATE USER octagon WITH PASSWORD '12345';"
sudo -u postgres psql -c "CREATE DATABASE octagon_db OWNER octagon;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE octagon_db TO octagon;"
```

Шаг 10. Инициализируйте базу данных
В терминале выполните:
```bash
python3 app/init_db.py
```

Шаг 11. Запустите сервер
В терминале выполните:
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```
Важно: этот терминал нужно оставить открытым, чтобы сервер работал.

Шаг 12. Откройте документацию API
Откройте браузер и перейдите по адресу:
http://127.0.0.1:8000/docs
Вы увидите Swagger-документацию со всеми эндпоинтами.

Шаг 13. Проверьте, что данные есть в базе
Откройте новый терминал в VS Code (нажмите на значок + рядом с текущим терминалом) и выполните:
```bash
sudo -u postgres psql -d octagon_db -c "SELECT * FROM categories;"
```
Вы должны увидеть список категорий.
Затем выполните:
```bash
sudo -u postgres psql -d octagon_db -c "SELECT * FROM books;"
```
Вы должны увидеть список книг.

Как остановить сервер:
В терминале, где запущен сервер, нажмите Ctrl + C.


