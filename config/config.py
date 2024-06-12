import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()



DEFAULT_COMMANDS = (
    ("newtask", "Создать задачу"),
    ("tasks", "Последние 10 задач"),
    ("today", "Задачи на сегодня"),
)
