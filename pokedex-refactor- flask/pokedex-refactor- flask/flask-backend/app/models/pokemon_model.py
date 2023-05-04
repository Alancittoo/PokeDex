from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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
    
    
    
    @staticmethod
    def captured():
        captured = this.getDataValue("captured")
        if (captured):
            return this.getDataValue("imageUrl")
        return UNKNOWN_IMG_URL