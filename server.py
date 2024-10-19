#server.py
from fastapi import FastAPI, Request, HTTPException
from typing import Dict
from web3 import Web3
import sqlite3
import os
from telegram import Bot, Update
from telegram.ext import CommandHandler

# Создание FastAPI приложения
app = FastAPI()



#BD
bd = {
    "test": {
        "grammar": {
            "question_number": 1,
            "question": "first_Question",
            "answers": {
                "a_answer": "a",
                "b_answer": "b",
                "c_answer": "c",
                "d_answer": "d"
            }
        }
    },
    "homeworks": {
        1: {
            "homework": "some homework 1"
        },
        2: {
            "homework": "some homework 2"
        },
        3: {
            "homework": "some homework 3"
        }

    },
    "achievements": {
        "hard_achievements": {

        }
    }
}


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
@app.get("/tests/{test}")
async def get_tests(test: str) -> Dict:
    for bd_test in bd["test"]:
        if bd_test == test:
            return bd["test"][test]
    raise HTTPException(status_code=404, detail="Test not found!")

# Возращаем домашние задания
@app.get("/homeworks/{id}")
async def get_homeworks(homework_id: int) -> str:
    for i in bd["homeworks"][homework_id]:
        if i == homework_id:
            return bd["homeworks"][homework_id]["homework"]
        else:
            raise HTTPException(status_code=404, detail="Homework not Found!")

# Функционал отправки домашнего задания
@app.post("/homeworks/post_homework/")
async def post_homeworks():
    pass

# Достижения
@app.get("/achievements/{achievement_id}")
async def get_achievements(achievement_id):
    pass

#
# # Установка вебхука для Telegram бота
# @app.post("/webhook/")
# async def telegram_webhook(request: Request):
#     data = await request.json()
#     update = Update.de_json(data, bot)
#     dispatcher.process_update(update)
#     return {"message": "Webhook received"}
#
#
# # Функция для обработки команды /start в боте
# def start(update, context):
#     user = update.message.from_user
#     context.bot.send_message(chat_id=user.id, text="Добро пожаловать! Это Kazakh Telegram Bot с поддержкой блокчейна!")
#
#
# dispatcher = Dispatcher(bot, None, workers=0)
# dispatcher.add_handler(CommandHandler("start", start))
#
#
# # Проверка подключения к блокчейну
# @app.get("/check-connection")
# async def check_connection():
#     if web3.isConnected():
#         return {"message": "Successfully connected to Ethereum network"}
#     else:
#         return {"message": "Failed to connect"}
#
#
# # Получение баланса адреса через Telegram Mini App
# @app.post("/balance/{address}")
# async def get_balance(address: str, update_id: int):
#     balance = web3.eth.get_balance(address)
#     eth_balance = web3.fromWei(balance, 'ether')
#
#     # Отправка баланса пользователю через Telegram
#     bot.send_message(chat_id=update_id, text=f"Баланс: {eth_balance} ETH")
#     return {"address": address, "balance": eth_balance}