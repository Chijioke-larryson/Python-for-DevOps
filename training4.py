"""
Project Title: Requestion API in Python

This project is designed to interact with the Requestion API using Python.
It provides functionalities to send requests and handle responses effectively.

## Installation

Instructions on how to install and set up the project.
"""

import requests
base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url =(f"{base_url}pokemon/{name}")
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data

    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")



pokemon_name = "typhlosion"
pokemon_info = get_pokemon_info(pokemon_name)


if pokemon_info:
    print(f"Information about {pokemon_info["name"]}:")
    print(f"Information about {pokemon_name} id is {pokemon_info["id"]}:")
    print(f"Information about {pokemon_name} height {pokemon_info["height"]}:")
    print(f"Information about {pokemon_name} weight  {pokemon_info["weight"]}kg:")
    