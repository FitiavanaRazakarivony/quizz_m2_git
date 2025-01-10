from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from app.models import User
from app import db
from app.utils import save_uploaded_file

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/register', methods=['POST'])
def register_user():
    name = request.form.get('name')
    password = request.form.get('password')
    model_image = request.files.get('model_image')

    if not name or not password or not model_image:
        return jsonify({"error": "Le nom, le mot de passe et l'image modèle sont requis."}), 400

    try:
        # Hachage du mot de passe
        hashed_password = generate_password_hash(password)

        # Sauvegarde de l'image
        model_image_path = save_uploaded_file('uploads', model_image)

        # Enregistrement dans la base de données
        new_user = User(name=name, password=hashed_password, model_image_path=model_image_path)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": f"Utilisateur '{name}' inscrit avec succès."}), 201
    except Exception as e:
        return jsonify({"error": f"Erreur lors de l'inscription : {str(e)}"}), 500
