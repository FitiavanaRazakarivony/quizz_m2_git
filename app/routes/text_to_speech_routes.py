from flask import Blueprint, request, jsonify
from app.utils import text_to_speech

text_to_speech_routes = Blueprint('text_to_speech_routes', __name__)

@text_to_speech_routes.route('/text-to-speech', methods=['POST'])
def text_to_speech_route():
    """
    Accepte un texte et renvoie une réponse de succès ou d'erreur.
    Effectue la conversion en parole.
    """
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({"error": "Le texte est requis pour la conversion."}), 400

    try:
        text_to_speech(text)
        return jsonify({"message": "Conversion en parole réussie."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
