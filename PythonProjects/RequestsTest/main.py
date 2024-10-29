import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = ''
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

create_pokemon_body = {
    "name": "Бульбазавр",
    "photo_id": 1
}

change_name_body = {
    "pokemon_id": "12331",
    "name": "New Name",
    "photo_id": 2
}

catch_in_pokeball_body = {
    "pokemon_id": "9"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = create_pokemon_body )
print(response_create.text)

response_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = change_name_body )
print(response_change_name.text)

response_catch_in_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = catch_in_pokeball_body )
print(response_catch_in_pokeball.text)