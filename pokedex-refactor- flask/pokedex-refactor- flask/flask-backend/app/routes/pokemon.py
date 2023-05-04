from flask import Blueprint, redirect ## imports Blueprint + etcprice
from ..models import Pokemon, Item
from random import choice
pokemon = Blueprint("pokemon", __name__)

@pokemon.route("")
def get_all_pokemon():

    all_pokemons = Pokemon.query.all()
    all_pokemons_dict = [pokemon.to_dict() for pokemon in all_pokemons]
    return all_pokemons_dict

@pokemon.route("/<int:id>")
def get_one_pokemon(id):
    pokemon = Pokemon.query.get(id)
    return pokemon.to_dict()

@pokemon.route("/<int:id>/items")
def get_pokemon_item(id):
    items = Pokemon.query.get(id).item
    item_list = [item.to_dict() for item in items]
    return item_list