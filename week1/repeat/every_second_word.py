text = input("Напишите предложение ")
words = text.split()

for i in range(1, len(words),2):
    print(words[i])
