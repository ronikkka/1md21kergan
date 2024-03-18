def delit2(n):
    if not n.isdigit():
        print ("Введите числовое значение (ValueError)")
    elif int(n) == 0:
        print ("Введите число, отличное от нуля (ZeroDivisionError)")
    else:
        r = 100 / int(n)
        print (r)

n = input ("Введите число: ")
delit2(n)