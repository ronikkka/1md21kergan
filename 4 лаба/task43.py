def dates (d):
    day, m, y = map( int, d.split(sep='.'))
    if day * m == y % 100:
        return True
    else: return False

d = input("Введите дату в формате дд.мм.гггг: ")
print(dates(d))