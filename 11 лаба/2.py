class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

rest1 = Restaurant("Еда", "Домашняя")
rest2 = Restaurant("Восток", "Азиатская")
rest3 = Restaurant("Дворик", "Русская")

rest1.describe_restaurant()
rest2.describe_restaurant()
rest3.describe_restaurant()