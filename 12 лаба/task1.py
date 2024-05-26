class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print("Ресторан открыт!")

class IceCreamStand(Restaurant):
    def __init__ (self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def see_flavors(self):
        print("Сорта мороженого:")
        for flavor in self.flavors:
            print(f"{flavor}")


newIceCreamStand = IceCreamStand ("Лавка мороженого", "Мороженое")
newIceCreamStand.describe_restaurant()
newIceCreamStand.flavors = ["Шоколад", "Ваниль", "Клубника"]
newIceCreamStand.see_flavors()


