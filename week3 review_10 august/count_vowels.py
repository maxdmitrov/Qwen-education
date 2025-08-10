text = input("Введи текст: ")
vowels = "аеёиоуыэюя"
count = 0
for char in text: 
    if char in vowels:
        count += 1
print(f"В этом тексте {count} гласных")