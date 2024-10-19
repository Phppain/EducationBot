#server.py
from fastapi import FastAPI, Request, HTTPException, UploadFile, File
import shutil
from typing import Dict
from web3 import Web3
import sqlite3
import os
from telegram import Bot, Update
from datetime import datetime


# Создание FastAPI приложения
app = FastAPI()



#BDfrom datetime import datetime

app = FastAPI()

# Подключение к базе данных SQLite
def get_db_connection():
    conn = sqlite3.connect('homeworks.db')
    conn.row_factory = sqlite3.Row
    return conn

# Маршрут для загрузки домашнего задания
@app.post("/homeworks/post_homework/")
async def post_homeworks(file: UploadFile = File(...), user_id: int = 1):
    try:
        # Чтение содержимого файла
        file_content = await file.read()

        # Подключение к базе данных
        conn = get_db_connection()
        cursor = conn.cursor()

        # SQL запрос на сохранение файла в базу данных
        cursor.execute("""
            INSERT INTO homeworks (user_id, filename, file_content, upload_time)
            VALUES (?, ?, ?, ?)
        """, (user_id, file.filename, file_content, datetime.now()))

        # Сохранение изменений
        conn.commit()
        conn.close()

        return {"status": "success", "message": f"File '{file.filename}' uploaded successfully!"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while uploading file: {str(e)}")


# Подключение к блокчейну через Infura
infura_url = "https://rinkeby.infura.io/v3/7ccb23ba7b5749b6ac219a9a489c584a"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Telegram API Token
# TELEGRAM_API_TOKEN = os.getenv("7668693359:AAFwxsXf9YCDa1u5vHLJqUCL7pMhUXWwYUw")
bot = Bot(token="7668693359:AAFwxsXf9YCDa1u5vHLJqUCL7pMhUXWwYUw")


def get_db_connection():
    conn = sqlite3.connect('your_database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Возращаем тесты
DATABASE_PATH = "kazakh_lang_db.py"  # Укажи путь к твоей базе данных в проекте
@app.get("/tests/{test}")
async def get_tests(test: str) -> Dict:
    conn = get_db_connection()
    cursor = conn.cursor()

    # Запрос на получение теста по имени из таблицы tests
    cursor.execute("SELECT * FROM tests WHERE name = ?", (test,))
    test_data = cursor.fetchone()
    conn.close()

    if test_data:
        return dict(test_data)  # Возвращаем как словарь
    else:
        raise HTTPException(status_code=404, detail="Test not found!")

# Возращаем домашние задания
@app.get("/homeworks/{homework_id}")
async def get_homeworks(homework_id: int) -> str:
    conn = get_db_connection()
    cursor = conn.cursor()

    # Запрос на получение домашнего задания из таблицы homeworks
    cursor.execute("SELECT homework FROM homeworks WHERE id = ?", (homework_id,))
    homework = cursor.fetchone()
    conn.close()

    if homework:
        return homework["homework"]  # Возвращаем текст домашнего задания
    else:
        raise HTTPException(status_code=404, detail="Homework not found!")

# Функционал отправки домашнего задания

@app.post("/homeworks/post_homework/")
async def post_homeworks(file: UploadFile = File(...)):
    try:
        # Ограничиваем типы файлов, которые можно загрузить
        allowed_extensions = ["pdf", "doc", "docx", "txt", "jpg", "png"]
        file_extension = file.filename.split(".")[-1].lower()

        if file_extension not in allowed_extensions:
            raise HTTPException(status_code=400, detail="Unsupported file type")

        # Путь для сохранения файла
        file_path = os.path.join(UPLOAD_DIR, file.filename)

        # Сохраняем файл
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return {"status": "success", "message": f"File '{file.filename}' uploaded successfully!"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while uploading file: {str(e)}")
# Достижения
@app.get("/achievements/{achievement_id}")
async def get_achievements(achievement_id: int) -> Dict:
    conn = get_db_connection()
    cursor = conn.cursor()

    # Запрос на получение достижения из таблицы achievements
    cursor.execute("SELECT * FROM achievements WHERE id = ?", (achievement_id,))
    achievement = cursor.fetchone()
    conn.close()

    if achievement:
        return dict(achievement)  # Возвращаем данные как словарь
    else:
        raise HTTPException(status_code=404, detail="Achievement not found!")
