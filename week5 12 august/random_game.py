import random

print("😊 Добро пожаловать в игру 'Угадай число' 😊")

while True:
        print()
        print("У тебя будет 3 попытки, чтобы отгадать число от 1 до 10")
        print()
        start = input("Начнем игру? (да/нет) ").lower()
        if start == "да":
            num = random.randint(1, 10)
        
            for i in range(3):
                try:
                    numb = int(input(f"Попытка {i+1}. Введите число: "))
                except ValueError:
                    print("Пожалуйста, введите целое число")
                    continue

                if numb == num:
                    print()
                    print(f"🎉 Поздравляю! Ты угадал! Это число {num} 🎉")
                    break
                elif numb > num:
                    print("❌ Загаданное число меньше вашего ❌")
                elif numb < num:
                    print("❌ Загаданное число больше вашего ❌")
            else:
                print()
                print(f"❌ Игра окончена! Было загадано число {num} ❌")
                print()

        elif start == "нет":
                print("👋 Увидимся в следующий раз! 👋 ")
                break 
        repeat = input("Повторим игру? (да/нет) ").lower()
        if repeat == "нет":
            print("👋 Увидимся в следующий раз! 👋 ")
            break       