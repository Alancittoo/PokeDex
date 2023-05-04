from flask import Blueprint, redirect ## imports Blueprint + etcprice
from ..models import Pokemon
pokemon = Blueprint("pokemon", __name__)

@pokemon.route("")
def get_all_pokemon():
    """route to fetch and display all pokemons"""
    # Query our DB to get all pokemons
    all_pokemons = Pokemon.query.all()
    print(all_pokemons)
    all_pokemons_dict = [pokemon.to_dict() for pokemon in all_pokemons]
    print(all_pokemons_dict)
    return all_pokemons_dict