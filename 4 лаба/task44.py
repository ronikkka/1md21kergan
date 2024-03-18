def udacha(l):
    h = len (l)//2
    h1 = 0
    h2 = 0

    for i in range(h):
        h1 += int(l[i])

    for i in range(h, len(l)):
        h2 += int(l[i])

    if h1 == h2:
        print("Ваш билет счастливый!")
    else: print ("Ваш билет не счастливый!")


l = input ("Введите номер вашего билета: ")
udacha(l)