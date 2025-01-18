# Carro de compra

foods = []
prices = []
total = 0

while True:
    food = input('Ingresa que comida quieres comprar (q para salir): ')
    if food.lower() == 'q':
        break
    else:
        price = input(f'Ingresa el valor de la comida ({food}): $')
        foods.append(food)
        prices.append(float(price))

print('------------ Tu Lista ------------')

for food in foods:
    print(food)

for price in prices:
    total += price

print(f'Tu subtotal es: ${total}')