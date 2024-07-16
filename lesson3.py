# text = "Поздравляю! "
# run = True
# while run:
#     name = input('Введите имя друга: ')
#     if name == "стоп": break
#     text = text + name + ", "
# print(text)

text = ""
name = 'Поздравляю! '
while not name == "стоп, ":
    text = text + name
    name = input('Введите имя друга: ') + ", "

text = text[:-2] + "."
print(text)







