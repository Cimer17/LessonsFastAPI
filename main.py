# uvicorn main:app --host 0.0.0.0 --port 8000 --reload        
from fastapi import FastAPI, Query
import random

app = FastAPI()

# Список загадок
riddles = [
    {"question": "Что можно увидеть с закрытыми глазами?", "answer": "Сон"},
    {"question": "Что можно держать, но нельзя потрогать?", "answer": "Слово"},
    {"question": "Что идет, но с места не двигается?", "answer": "Время"},
    {"question": "Что всегда перед нами, но мы его не видим?", "answer": "Будущее"},
    {"question": "Что становится больше, если из него убрать?", "answer": "Дыра"}
]

# Секретный API-ключ
SECRET_KEY = "mysecretkey123"

# Функция для выдачи случайной загадки
@app.get("/riddle")
def get_riddle():
    return random.choice(riddles)

# Функция для генерации случайного числа по API-ключу
@app.get("/random_number")
def get_random_number(api_key: str = Query(...)):
    if api_key == SECRET_KEY:
        return {"random_number": random.randint(1, 100)}
    else:
        return {"error": "Неверный API-ключ"}

# Функция для шифрования методом Цезаря
def caesar_cipher(text: str, shift: int, decrypt: bool = False) -> str:
    if decrypt:
        shift = -shift
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# API для шифрования
@app.get("/encrypt")
def encrypt(api_key: str = Query(...), text: str = Query(...), shift: int = Query(...)):
    if api_key == SECRET_KEY:
        return {"encrypted_text": caesar_cipher(text, shift)}
    else:
        return {"error": "Неверный API-ключ"}

# API для расшифровки
@app.get("/decrypt")
def decrypt(api_key: str = Query(...), text: str = Query(...), shift: int = Query(...)):
    if api_key == SECRET_KEY:
        return {"decrypted_text": caesar_cipher(text, shift, decrypt=True)}
    else:
        return {"error": "Неверный API-ключ"}