from .item_seeds import item_list
from .pokemon_seeds import pokemon
from .app.models import db, Pokemon, Item
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()
    for pokes in pokemon:
        pokes = Pokemon(
            number = pokes.number,
            attack = pokes.attack,
            defense = pokes.defense,
            image_url = pokes.image_url,
            name = pokes.name,
            type = pokes.type,
            moves = pokes.moves,
            encounter_rate = pokes.encounter_rate,
            catch_rate = pokes.catch_rate,
            captured = pokes.captured,
        )
        db.session.add(pokes)
        db.session.commit()
        
    for item in item_list:
        item = Item(
            image_url = item.image_url,
            happiness = item.happiness,
            name = item.name,
            price = item.price,
            pokemon_id = item.pokemon_id,
        )
        db.session.add(item)
        db.session.commit()