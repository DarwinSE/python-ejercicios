# Calculadora de Interes Compuesto

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input('Ingresa la cantidad de solicitada: '))
    if principle <= 0:
        print('La cantidad solicitada debe ser mayor o igual a 0')
    
while rate <= 0:
    rate = float(input('Ingresa el ratio de interes: '))
    if rate <= 0:
        print('La cantidad solicitada debe ser mayor o igual a 0')

while time <= 0:
    time = float(input('Ingresa la cantidad de años: '))
    if time <= 0:
        print('La cantidad solicitada debe ser mayor o igual a 0')

total = principle * pow((1 + rate / 100), time)

print(f'El total de la deuda al final de los {time:.0f} años es: ${total:.2f}')