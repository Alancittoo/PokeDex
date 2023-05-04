from app import app
from app.seeds import pokemon, item_list
from app.models import db, Pokemon, Item

with app.app_context():
    db.drop_all()
    db.create_all()
    for pokes in pokemon:
        pokes = Pokemon(
            number = pokes["number"],
            attack = pokes["attack"],
            defense = pokes["defense"],
            image_url = pokes["image_url"],
            name = pokes["name"],
            type = pokes["type"],
            moves = ','.join(pokes["moves"]),
            encounter_rate = 1.0,
            catch_rate = 1.0,
            captured = pokes["captured"],
        )
        db.session.add(pokes)
        db.session.commit()
        
    for item in item_list:
        item = Item(
            image_url = item["image_url"],
            happiness = item["happiness"],
            name = item["name"],
            price = item["price"],
            pokemon_id = item["pokemon_id"],
        )
        db.session.add(item)
        db.session.commit()