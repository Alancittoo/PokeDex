import os
from flask import Flask
from flask_migrate import Migrate
from app.config import Configuration
from .models import db
from .routes.pokemon import pokemon
from .routes.items import item ## import order routes

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(pokemon, url_prefix="/api/pokemon") ## connects route to app
app.register_blueprint(item, url_prefix="/api/item") ## connects route to app

db.init_app(app)
migrate = Migrate(app, db)

# import statement for CSRF
from flask_wtf.csrf import CSRFProtect, generate_csrf

@app.route("/")
def index():
    return "hello"

# after request code for CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response
