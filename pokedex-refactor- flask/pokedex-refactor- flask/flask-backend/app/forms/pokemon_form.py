from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired

types = [
  "fire",
  "electric",
  "normal",
  "ghost",
  "psychic",
  "water",
  "bug",
  "dragon",
  "grass",
  "fighting",
  "ice",
  "flying",
  "poison",
  "ground",
  "rock",
  "steel",
]


class PokemonForm(FlaskForm):
    number = IntegerField("Number", validators=[DataRequired()])
    attack = StringField("Attack", validators=[DataRequired()])
    defense = StringField("Defense", validators=[DataRequired()])
    image_url = StringField("Image", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    type = SelectField("Type", choices=types, validators=[DataRequired()])
    moves = StringField("Moves", validators=[DataRequired()])
    
