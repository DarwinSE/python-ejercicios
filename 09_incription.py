# Programa de incripcion de texto

import random
import string

chars = ' ' + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f'characteres: {chars}')
# print(f'llave: {key}')

# Encriptar

text = input('Ingresa el mensaje a Encriptar: ')
cipher_text = ''

for letter in text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f'Mensaje Original: {text}')
print(f'Mensaje Encriptado: {cipher_text}')

# Desencriptar

cipher_text = input('Ingresa el mensaje a Desencriptar: ')
text = ''

for letter in cipher_text:
    index = key.index(letter)
    text += chars[index]

print(f'Mensaje Encriptado: {cipher_text}')
print(f'Mensaje Original: {text}')