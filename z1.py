# Задача на диапазон значений

volume = int(input("Сколько воды нам нужно?: " ))
volume2 = int(input("Какой этаж?: " ))

if volume <=5 and volume2 <=53:
    print('dostavleno')
elif volume <=2 and volume2 <=99:
    print("Vse ok")
elif volume <=1 and volume2 <=100:
    print("Dostavleno vse ok")
else:
    print("Не доставлено")

