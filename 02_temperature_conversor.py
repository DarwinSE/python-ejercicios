# Simple temperature conversion

unit = input('En que unidad esta la temperatura? Celsius o Farenheit? (C o F): ')
temperature = float(input('Ingresa la temperatura: '))

if unit.lower() == 'c':
    converted_temperature = (temperature * 9)/5 + 32
    print(f'La temperatura en Fahrenheit es: {converted_temperature:.2f}')
elif unit.lower() == 'f':
    converted_temperature = (temperature - 32) * 5/9
    print(f'La temperatura en Celsius es: {converted_temperature:.2f}')
else:
    print('Ingresaste una unidad incorrecta. Intente nuevamente.')