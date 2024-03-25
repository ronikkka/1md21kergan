def z1(ch):
    list = [1,2,3,4,5]
    if ch in list:
        print(list, ch, "Поздравляю, Вы угадали число!" )
    else:
        print(list, ch, "Нет такого числа!")

def z2(i):
    import collections
    list2 = [1, 4, 3, 4, 4]
    povt = 0
    for i in range(0,4):
        d = list2.count(list2[i])
        el = list2[i]
        if el == povt:
            break
        if d != 1:
            print(el, d)
            povt = list2[i]

def z3(z):
    dni=['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье']
    kolvo = int(input("Введите количнство выходных на неделе:"))
    otd = list(dni[-kolvo:])
    rab = list(dni[:-kolvo])
    print("Ваши выходные:", otd)
    print("Ваши рабочие дни:", rab)

def z4(g):
    fam1 = ['Иванов','Смирнов','Сидорова','Горчаренко','Каратаева','Большухина','Козловский','Керган','Морозов','Александров']
    fam2 = ['Гончаров', 'Исаев', 'Волков', 'Соколов', 'Гречкин', 'Скворцов', 'Крылов', 'Кузнецов', 'Широков', 'Беляев']
    sport = tuple(fam1[3:8]+fam2[:5])
    print(fam1)
    print(fam2)
    print(sport)
    print(len(sport))
    sort = tuple(sorted(sport))
    sname = 'Иванов'
    if 'Иванов' in sort:
        print("Студент Иванов в спортивной команде")
        ivanov=sort.count(sname)
        print("Фамилия встречается ", ivanov, " раз")





z2(2)

z3(3)

z4(4)