# uvicorn main:app --host 192.168.0.241 --port 8000 --reload     
# http://127.0.0.1:8000/docs
from fastapi import FastAPI, Query
import random

app = FastAPI(
    title="FastAPI Example",
    description="API с загадками, генератором случайных чисел и шифром Цезаря \nОбщий API КЛЮЧ - mysecretkey123",
    version="1.0.0"
)

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

@app.get("/riddle", summary="Получить случайную загадку", description="Возвращает случайную загадку с ответом из предустановленного списка.")
def get_riddle():
    return random.choice(riddles)

@app.get("/random_number", summary="Получить случайное число", description="Возвращает случайное число от 1 до 100, если передан верный API-ключ.")
def get_random_number(api_key: str = Query(..., description="API-ключ для доступа")):
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

@app.get("/encrypt", summary="Зашифровать текст методом Цезаря", description="Шифрует текст методом Цезаря с указанным сдвигом, если передан верный API-ключ.")
def encrypt(api_key: str = Query(..., description="API-ключ для доступа"), text: str = Query(..., description="Текст для шифрования"), shift: int = Query(..., description="Сдвиг для шифра Цезаря")):
    if api_key == SECRET_KEY:
        return {"encrypted_text": caesar_cipher(text, shift)}
    else:
        return {"error": "Неверный API-ключ"}

@app.get("/decrypt", summary="Расшифровать текст методом Цезаря", description="Расшифровывает текст методом Цезаря с указанным сдвигом, если передан верный API-ключ.")
def decrypt(api_key: str = Query(..., description="API-ключ для доступа"), text: str = Query(..., description="Текст для расшифровки"), shift: int = Query(..., description="Сдвиг для шифра Цезаря")):
    if api_key == SECRET_KEY:
        return {"decrypted_text": caesar_cipher(text, shift, decrypt=True)}
    else:
        return {"error": "Неверный API-ключ"}
