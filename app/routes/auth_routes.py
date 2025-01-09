from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

auth_routes = Blueprint('auth_routes', __name__)

# Exemple de route pour l'authentification
@auth_routes.route('/authenticate', methods=['POST'])
def authenticate_user():
    user_id = request.form.get('user_id')
    image_file = request.files.get('image_path')  # L'image capturée pour la comparaison

    if not user_id or not image_file:
        return jsonify({"error": "L'ID utilisateur et l'image sont requis."}), 400

    # Traitement de l'image (simulé ici)
    return jsonify({"message": "Image capturée et authentifiée avec succès."})

@auth_routes.route('/protected', methods=['GET'])
@jwt_required()  # Protège la route avec JWT
def protected():
    """
    Exemple de route protégée par JWT.
    L'accès est autorisé uniquement aux utilisateurs authentifiés avec un token JWT.
    """
    return jsonify(message="Accès autorisé !"), 200