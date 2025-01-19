# Juego de piedra papel o tijera

import random

def jugar():
    options = ('piedra', 'papel', 'tijeras')
    while True:
        player = None
        computer = random.choice(options)

        while player not in options:
            player = input('Elije una opción (piedra, papel o tijeras): ').strip().lower()

        print(f'Jugador: {player}')
        print(f'Computadora: {computer}')

        if player == computer:
            print('Empate!')
        elif (player == 'piedra' and computer == 'tijeras') or \
             (player == 'papel' and computer == 'piedra') or \
             (player == 'tijeras' and computer == 'papel'):
            print('Ganaste!')
        else:
            print('Perdiste!')

        play_again = ''
        while play_again not in ('s', 'n'):
            play_again = input('Jugar otra vez? (s/n): ').strip().lower()

        if play_again == 'n':
            break

    print('Gracias por jugar!')

jugar()
