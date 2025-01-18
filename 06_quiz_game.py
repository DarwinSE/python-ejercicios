# Ejericio de Preguntas

questions = (
    'Cuantos elementos hay en la tabla periodica?: ',
    'Cual es el animal mas pesado?: ',
    'Cual es el gas mas abundante en la atmosfera terrestre?: ',
    'Cuantos huesos tiene el cuerpo humano?: ',
    'Cual es el planeta mas alejado del sol?: '
)
options = (
    ('A. 116', 'B. 117', 'C. 118', 'D. 119'), 
    ('A. Ballena Azul', 'B. Rinoceronte', 'C. Elefante', 'D. Ballena Blanca'),
    ('A. Nitrogeno', 'B. Oxigeno', 'C. Hidrogeno', 'D. Helio'),
    ('A. 200', 'B. 205', 'C. 201', 'D. 206'),
    ('A. Saturno', 'B. Neptuno', 'C. Urano', 'D. Jupiter')
)

answers = ('C', 'A', 'A', 'D', 'B')
guesses = []
score = 0
question_num = 0

for question in questions:
    print('---------------------')
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input('Ingrese su respuesta (A, B, C, D): ').upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print('Correcto!')
    else:
        print('Incorrecto')
        print(f'La respuesta correcta era: {answers[question_num]}')

    question_num += 1