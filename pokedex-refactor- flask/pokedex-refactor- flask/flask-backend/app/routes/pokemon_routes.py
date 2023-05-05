from flask import Flask, Blueprint, redirect, request ## imports Blueprint + etcprice
from ..models import Pokemon, Item, types
from ..forms.pokemon_form import PokemonForm
from random import choice
from ..models import db
pokemon = Blueprint("pokemon", __name__)

## gets all pokemon
@pokemon.route("")
def get_all_pokemon():
    all_pokemons = Pokemon.query.all()
    all_pokemons_dict = [pokemon.to_dict() for pokemon in all_pokemons]
    return all_pokemons_dict

## gets single pokemon based off id
@pokemon.route("/<int:id>")
def get_one_pokemon(id):
    pokemon = Pokemon.query.get(id)
    return pokemon.to_dict()

## gets list of all items
@pokemon.route("/<int:id>/items")
def get_pokemon_item(id):
    items = Pokemon.query.get(id).item
    item_list = [item.to_dict() for item in items]
    return item_list

##  gets all pokemon types
@pokemon.route("/types")
def get_types():
    return types

## creates a new pokemon
@pokemon.route("", methods=["POST"])
def add_pokemon():
    data = request.json
    form = PokemonForm()
    form['csrf_token'].data = request.cookies['csrf_token']
        
    new_pokemon = Pokemon(
        number=data["number"],
        attack=data["attack"],
        defense=data["defense"],
        image_url=data["imageUrl"],
        name=data["name"],
        type=data["type"],
        moves=','.join(data["moves"]),
        encounter_rate= 1.0,
        catch_rate= 1.0,
        captured=True
    )
        
    db.session.add(new_pokemon)
    db.session.commit()
    return new_pokemon.to_dict()

## edit a new pokemon
@pokemon.route("/<int:id>", methods=["PUT"])
def edit_pokemon(id):
    pokemon = (Pokemon.query.get(id)).to_dict()
    pokemon["name"] = "Pikachu"
    data = request.json
    pokemon.update(data)
    # form = PokemonForm()
    # form['csrf_token'].data = request.cookies['csrf_token']
        
    # updated_pokemon = Pokemon(
    #     number=data["number"],
    #     attack=data["attack"],
    #     defense=data["defense"],
    #     image_url=data["imageUrl"],
    #     name=data["name"],
    #     type=data["type"],
    #     moves=','.join(data["moves"]),
    #     encounter_rate= 1.0,
    #     catch_rate= 1.0,
    #     captured=False
    # )
        
    # db.session.add(new_pokemon)
    db.session.commit()
    return pokemon

    # data = request.json
    # print(f"data 👉 {data}")
    # form = PokemonForm()
    # form['csrf_token'].data = request.cookies['csrf_token']