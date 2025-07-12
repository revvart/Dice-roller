import random
import os

while True:
    amount, edges = map(int,input("Введите дайсы в формате 1к6 ").split('к'))
    os.system("cls")
    summary=0
    for i in range(amount):
        throw = random.randint(1, edges)
        summary+=throw
        print(throw)
    print("Всего:", summary)
