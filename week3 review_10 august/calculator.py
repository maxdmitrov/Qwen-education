num1 = int(input("Введи первое число "))
num2 = int(input("Введи второе число "))
op = input("Какую операцию выполним? (+,-,*,/) ")
if op == ("+"):
    result = num1 + num2
    print(f"Результат {result}")
elif op == ("-"):
    result = num1 - num2
    print(f"Результат {result}")
elif op == ("*"):
    result = num1 * num2
    print(f"Результат {result}")
elif op == ("/"):
    result = num1 / num2
    print(f"Результат {result}")
else: 
    print(f"Ошибка: неизвестная операция")