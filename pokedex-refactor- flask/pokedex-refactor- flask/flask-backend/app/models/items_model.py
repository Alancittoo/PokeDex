from .db import db
from flask import url_for

class Item(db.Model):
    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255), nullable=False)
    happiness = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(255))
    price = db.Column(db.Integer, nullable=False)
    pokemon_id = db.Column(db.Integer, db.ForeignKey("pokemons.id"), nullable=False)
    pokemon = db.relationship(
        "Pokemon",
        back_populates = "item"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "imageUrl": url_for("static", filename = self.image_url),
            "happiness": self.happiness,
            "name": self.name,
            "price": self.price,
            "pokemon": self.pokemon.to_dict_no_item()
        }