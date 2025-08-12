team = []

while True: 
    command = input("Что нужно сделать? (добавить/удалить/показать/выйти) ").lower()
    if command == "добавить":
        name = input("Введи имя участника ")
        team.append(name)
        print(f"'{name}' успешно добавлен в команду")
    elif command == "удалить":
        a = input("Введи имя, кого нужно удалить ")
        if a in team:
                team.remove(a)
        print(f"{a} успешно удален")
    elif command == "показать":
        for i, name in enumerate(team, start=1):
            print(f"{i}. {name}")
    elif command == "выйти":
        print(f"Всё, пака!")
        break
    else:
        print(f"Неизвестная мне команда")
        
    
