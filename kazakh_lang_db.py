import sqlite3

conn = sqlite3.connect('kazakh_language.db')
cursor = conn.cursor()

# Пользователи
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        registration_date TEXT NOT NULL
    )
''')

# Отправка дз
cursor.execute('''
    CREATE TABLE IF NOT EXISTS homework_submissions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        file_path TEXT NOT NULL,
        submission_date TEXT NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
''')

# Достижения с названием и описанием
cursor.execute('''
    CREATE TABLE IF NOT EXISTS achievements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL
    )
''')

# Те достижения которые выполнены
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

# Коины пользователя, можно потом добавлять коины за выполненое задание
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_coins (
        user_id INTEGER PRIMARY KEY,
        coins INTEGER NOT NULL DEFAULT 0,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
''')


cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.commit()
conn.close()


