# even_odd.py

# Шаг 1: спрашиваем число
number = int(input("Введите число: "))

# Шаг 2: проверяем, чётное или нет
if number % 2 == 0:
    print(f"Число {number} — чётное")
else:
    print(f"Число {number} — нечётное")