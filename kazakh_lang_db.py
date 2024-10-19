import sqlite3

# Создаем подключение к базе данных
conn = sqlite3.connect('kazakh_language.db')
cursor = conn.cursor()

# Таблица пользователей
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        registration_date TEXT NOT NULL
    )
''')

# Таблица отправленных домашних заданий
cursor.execute('''
    CREATE TABLE IF NOT EXISTS homework_submissions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        file_path TEXT NOT NULL,
        submission_date TEXT NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
''')

# Таблица достижений
cursor.execute('''
    CREATE TABLE IF NOT EXISTS achievements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL
    )
''')

# Таблица выполненных достижений пользователя
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_achievements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        achievement_id INTEGER NOT NULL,
        completion_date TEXT NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(achievement_id) REFERENCES achievements(id)
    )
''')

# Таблица коинов пользователя
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_coins (
        user_id INTEGER PRIMARY KEY,
        coins INTEGER NOT NULL DEFAULT 0,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
''')

# Таблица тестов
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        content TEXT NOT NULL
    )
''')

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()
