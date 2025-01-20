# Ejemplo de conexion de API

import requests

base_url = 'https://pokeapi.co/api/v2/'

def get_pokemon_info(name):
    url = f'{base_url}/pokemon/{name}'
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f'Fallo al recibir los datos {response}')

pokemon_name = 'charmander'
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f'Información de {pokemon_name}:')
    print(f'Nombre: {pokemon_info['name'].capitalize()}')
    print(f'Altura: {pokemon_info['height']} metros')
    print(f'Peso: {pokemon_info['weight']} kilogramos')
    print(f'Tipo: {''.join(pokemon_info['types'][0]['type']['name'])}')
    print(f'Habilidades: {', '.join(ability['ability']['name'] for ability in pokemon_info['abilities'])}')