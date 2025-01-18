# Simple calculator

operator = input('Ingresa un tipo de operacion (+ - * /): ')
num1 = float(input('Ingresa el primer numero: '))
num2 = float(input('Ingresa el segundo numero: '))

if operator == '+':
    result = num1 + num2
    print(round(result, 2))
elif operator == '-':
    result = num1 - num2
    print(round(result, 2))
elif operator == '*':
    result = num1 * num2
    print(round(result, 2))
elif operator == '/':
    if num2 == 0:
        print('Error: Division por cero')
    else:
        result = num1 / num2
        print(round(result, 2))
else:
    print('Error: Operacion invalida')