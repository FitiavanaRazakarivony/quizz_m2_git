from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Initialiser l'extension SQLAlchemy
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    # Créer l'instance de l'application Flask
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialisation des extensions
    db.init_app(app)
    jwt.init_app(app)

    # Enregistrement des blueprints
    from .routes import register_blueprints
    register_blueprints(app)

    # Créer la base de données
    with app.app_context():
        db.create_all()

    return app

