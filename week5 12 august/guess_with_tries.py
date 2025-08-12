import random
num = random.randint(1,10)
for i in range(3):
    numb = int(input("Введите число: "))
    if numb == num:
        print("Поздравляю! Ты угадал!")
        break
    elif numb > num:
        print("Загаданное число меньше вашего")
    elif numb < num:
        print("Загаданное число больше вашего")
else:
    print(f"Игра окончена! Было число {num}")
        