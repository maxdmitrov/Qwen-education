secret = 13
a = int(input("Какое число я загадал? "))
if a == secret:
    print(f"Ты угадал, это число {secret}")
elif a > secret:
    print("Упс, ты не угадал. Мое число меньше")
else:
    print("Упс, ты не угадал. Мое число больше")
