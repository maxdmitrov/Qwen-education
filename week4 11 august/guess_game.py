import random
num = random.randint(1,10)
numb = int(input("Угадай число от 1 до 10: "))
if numb == num:
    print(f"Поздравляю!")
else:
    print(f"Не угадал. Было число {num}")