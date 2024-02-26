from random import randint
mist = 0
cor = 0
while mist < 3:
    n1 = randint(1, 10)
    n2 = randint(1, 10)
    otv = input(str(n1) + "+" + str(n2) + "=")
    if int(otv) == n1 + n2:
        print("Правильно!")
        cor += 1
    else:
        print ("Неправильно!")
        mist += 1
print("Игра окончена. Правильных ответов:", cor)