text = input("Введите текст ")
text = text.lower()
count = 0
for char in text:
    if char in "аеёиоуыэюя":
        count += 1  
print(f"В тексте {text} {count} гласных")