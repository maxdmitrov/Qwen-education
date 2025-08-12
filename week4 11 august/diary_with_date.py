from datetime import datetime
text = input("Введите запись для дневника: ")
now = datetime.now()
print(f"{now} {text}")