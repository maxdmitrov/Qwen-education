# спрашиваем 1 число
a = int(input("Введи первое число: "))

# спрашиваем 2 число
b = int(input("Введи второе число: "))

# спрашиваем операцию 
op = input("Какую операцию произведем? (+,-,*,/) ")

if op == "+":
    result = a + b
elif op == "-":
    result = a - b 
elif op == "*":
    result = a * b 
elif op == "/":
    result = a / b 
else: 
    result = "Ошибка: неизвестная команда"

print(f"Результат {a} {op} {b} = {result}")