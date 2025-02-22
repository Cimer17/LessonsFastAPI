# Список загадок
riddles = [
    {"question": "Что можно увидеть с закрытыми глазами?", "answer": "Сон"},
    {"question": "Что можно держать, но нельзя потрогать?", "answer": "Слово"},
    {"question": "Что идет, но с места не двигается?", "answer": "Время"},
    {"question": "Что всегда перед нами, но мы его не видим?", "answer": "Будущее"},
    {"question": "Что становится больше, если из него убрать?", "answer": "Дыра"}
]

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