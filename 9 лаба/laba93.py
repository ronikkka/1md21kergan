import csv

with open('products.csv', 'r') as f:
    reader = csv.reader(f)
    total_sum = 0

    for row in reader:
        product, quantity, price = row
        quantity = int(quantity)
        price = float(price)
        product_cost = quantity * price
        total_sum += product_cost
        print(f"Нужно купить: {product} - {quantity} шт. за {product_cost} руб.")

print(f"Итоговая сумма: {total_sum} руб.")
