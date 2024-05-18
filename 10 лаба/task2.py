import json

with open('products.json', 'r') as f:
    data = json.load(f)

new_product = {}
new_product['name'] = input("Название продукта: ")
new_product['price'] = int(input("Цена продукта: "))
new_product['weight'] = int(input("Вес продукта: "))
new_product['available'] = input("Продукт в наличии? (да/нет): ") == "да"

data['products'].append(new_product)

with open('products.json', 'w') as f:
    json.dump(data, f, indent=4)

for product in data['products']:
    print("Название:", product['name'])
    print("Цена:", product['price'])
    print("Вес:", product['weight'])
    if product['available']:
        print("В наличии")
    else:
        print("Нет в наличии!")
    print()