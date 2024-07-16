# for planet in "Меркурий", "Марс", "Земля", "Юпитер", "Уран", "Плутон":
#     print(planet)

# promo = "cofe"
# for a in range(1,4):
#     answer = input("Введите ваш промокод: ")
#     if answer == promo:
#         print("Ваш кофе ")
#     else:
#         print("Неверный промокод ")


# promo = "cofe"
# for a in range(3):
#     answer = input("Введите ваш промокод: ")
#     sum = int(input("Ваш чек: "))
#     if answer == promo:
#         if sum >= 2000:
#             skd = sum * 0.02
#             pay = sum - skd
#             print(f"Итог к оплате: {pay}\nВаша скидка: {skd} ")
#             break
#         else:
#             print("Не хватает денег")
#     else:
#         print("Неверный промокод ")

# max = 0
# for i in range(5):
#     x = int(input("Сколько бутылок в ящике? "))
#     if max < x and x <= 100:
#         max = x
# print("Максимальное число" , max)

# import time
#
# for i in range(6):
#     print( 5 - i )
#     time.sleep(1)
#     if 5 - i == 0:
#         print("поехали")

import random

score_comp = 0
score_player = 0
while True:
    if score_comp == 3 or score_player == 3:
        break
    try:
        player = input("1.камень? \n2.ножницы? \n3.бумага? ")
        if player == "стоп": break
        player = int(player)

    except:

        print("выберите число от 1 до 3")

    try:

        comp = random.choice(["камень", "ножницы", "бумага"])
        if type(player) == type(""): continue
        if player == 1:
            player = "камень"
        elif player == 2:
            player = "ножницы"
        else:
            player = "бумага"
        print(comp)

        if player == "камень" and comp == "камень":
            print("ничья")
        if player == "камень" and comp == "ножницы":
            print("Победа")
            score_player = 1 + score_player
        if player == "камень" and comp == "бумага":
            print("поражение")
            score_comp = 1 + score_comp
        if player == "ножницы" and comp == "камень":
            print("поражение")
            score_comp = 1 + score_comp
        if player == "ножницы" and comp == "ножницы":
            print("ничья")
        if player == "ножницы" and comp == "бумага":
            print("Победа")
            score_player = 1 + score_player
        if player == "бумага" and comp == "камень":
            print("Победа")
            score_player = 1 + score_player
        if player == "бумага" and comp == "ножницы":
            print("поражение")
            score_comp = 1 + score_comp
        if player == "бумага" and comp == "бумага":
            print("ничья")
        print(f'компьютер {score_comp}:{score_player} игрок')

    except:
        pass
