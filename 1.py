import random
while True:
    dice = input("Введите дайсы в формате 1к6 ")
    amount, num = map(int,dice.split('к'))
    k=0
    for i in range(amount):
        itog = random.randint(1, num)
        k+=itog
        print(itog)
    print("Всего:", k)
