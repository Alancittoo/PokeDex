from flask import Flask, Blueprint, redirect, request ## imports Blueprint + etcprice
from ..models import Pokemon, Item
from ..forms.pokemon_form import PokemonForm
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

@pokemon.route("", methods=["POST"])
def add_pokemon():
    form = PokemonForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = form.data
        print(f"data 👉 {data}")
        
        new_pokemon = Pokemon(
            number=data["number"],
            attack=data["attack"],
            defense=data["defense"],
            image_url=data["image_url"],
            name=data["name"],
            type=data["type"],
            moves=data["moves"],
            encounter_rate= 1.0,
            catch_rate= 1.0,
            captured=False
        )
        
        db.session.add(new_pokemon.to_dict())
        db.session.commit()
        return
    else:
        return form.errors
