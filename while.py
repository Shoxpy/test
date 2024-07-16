x = 0

while x < 100:
    x += 1
    print(x)

run = True
while run:
    print('Вечность', x)
    x = random.randint (1, 1000)
    if x == 500:
        run = False