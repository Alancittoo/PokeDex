from .db import db
from flask import url_for

UNKNOWN_IMG_URL = "/images/unknown.png"

class Pokemon(db.Model):
    __tablename__ = 'pokemons'
    
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer,nullable=False, unique=True)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    name = db.Column(db.String(255), nullable=False, unique=True)
    type = db.Column(db.String)
    moves = db.Column(db.String(255), nullable=False)
    encounter_rate = db.Column(db.Float(precision=2))
    catch_rate = db.Column(db.Float(precision=2))
    captured = db.Column(db.Boolean)
    item = db.relationship(
        "Item",
        back_populates = "pokemon",
    )
    
    def to_dict(self):
        return {
            "id": self.id,
            "number": self.number,
            "attack": self.attack,
            "defense": self.defense,
            "imageUrl": url_for("static", filename = self.image_url),
            "name": self.name,
            "type": self.type,
            "moves": self.moves.split(","),
            "encounterRate": self.encounter_rate,
            "catchRate": self.catch_rate,
            "captured": self.captured,
            "item": [item.to_dict() for item in self.item]
        } 
        
    def to_dict_no_item(self):
        return {
            "id": self.id,
            "number": self.number,
            "attack": self.attack,
            "defense": self.defense,
            "imageUrl": url_for("static", filename = self.image_url),
            "name": self.name,
            "type": self.type,
            "moves": self.moves.split(","),
            "encounterRate": self.encounter_rate,
            "catchRate": self.catch_rate,
            "captured": self.captured,
        }
      
    # @staticmethod
    # def captured():
    #     captured = this.getDataValue("captured")
    #     if (captured):
    #         return this.getDataValue("imageUrl")
    #     return UNKNOWN_IMG_URL