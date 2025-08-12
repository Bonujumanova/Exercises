import requests
from bs4 import BeautifulSoup
from pprint import pprint


pokemons_url: str = "https://www.pokemon.com/us/pokedex"
pokemons_response = requests.get(pokemons_url)
soup = BeautifulSoup(pokemons_response.text, features="html.parser")
pokemons = soup.find_all("ul", class_="results")
print(pokemons)
if pokemons:
    for li in pokemons:
        li = li.find_next("li", class_="animating")
        print(li)
        name = li.h5.name
        print(name)










# pokemon_name = pass_none()
# pokemon_name: str = "Charmander"
# url = (f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
#
#
# response = requests.get(url)
# print(response)
#
# pokemon_info: dict = response.json().get("name")
# print(pokemon_info)
#
#
# pokemon_info: dict = response.json()
# pprint(pokemon_info)
# print(f"{pokemon_info['name']}")
# print(f"{pokemon_info['id']}")
# print(f"{pokemon_info['height']}")
# print(f"{pokemon_info['weight']}")
