class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print("Ресторан открыт!")

newrestaurant = Restaurant ("Синьор помидор", "Итальянская")

print(newrestaurant.restaurant_name)
print(newrestaurant.cuisine_type)

newrestaurant.describe_restaurant()
newrestaurant.open_restaurant()