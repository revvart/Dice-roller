import random
import os
print('To set the language as english type en/Чтобы установить язык на русский, напишите ru')
lang = input()
text = [string.rstrip() for string in open(f'{lang}.txt', encoding='utf-8')]
diceCode = text[1]
while True:
    amount, edges = map(int,input(text[0] +'\n').split(diceCode))
    os.system("cls")
    summary=0
    print(text[3], f'{amount}{diceCode}{edges}')
    for i in range(amount):
        throw = random.randint(1, edges)
        summary+=throw
        print(throw)
    print(text[2], summary)
