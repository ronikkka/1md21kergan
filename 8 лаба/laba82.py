holidays = {
    "Новый год": "new_year.jpg",
    "Рождество": "christmas.jpg",
    "8 Марта": "womens_day.jpg",
    "23 Февраля": "defenders_day.jpg"
}

holiday = input("Введите название праздника: ")

if holiday in holidays:
    filename = holidays[holiday]
    if os.path.isfile(filename):
        with open(filename, "rb") as f:
            image = f.read()
            print(image.decode("utf-8"))
    else:
        print("Открытка не найдена.")
else:
    print("Введенный праздник не найден в словаре.")