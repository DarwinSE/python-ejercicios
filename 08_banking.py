# Programa de Banco

def show_balance():
    print(f'Tu balance es ${balance:.2f}')

def deposit():
    amount = float(input('Ingresa la cantidad a ser depositada: '))

    if amount < 0:
        print('No es una cantidad valida')
        return 0
    else:
        return amount

def withdraw():
    amount = float(input('Ingresa la cantidad a ser retirada: '))

    if amount < 0:
        print('No es una cantidad valida')
        return 0
    elif amount > balance:
        print('No tienes suficiente saldo')
        return 0
    else:
        return amount

balance = 0
is_running = True

while is_running:
    print('Banco Simple!')
    print('1. Mostrar Saldo')
    print('2. Depositar')
    print('3. Retirar')
    print('4. Salir')

    choice = input('Ingresa tu eleccion (1-4): ')

    if choice == '1':
        show_balance()
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        balance -= withdraw()
    elif choice == '4':
        is_running = False
    else:
        print('Opcion invalida')

print('Gracias por usar nuestro Banco')