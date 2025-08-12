words = {"hello": "привет", "cat": "кот"}
word = input("Введи слово на английском языке ").lower()
if word in words:
    print(f"Перевод: {words[word]}")
else:
    print(f"Не знаю такого слова")