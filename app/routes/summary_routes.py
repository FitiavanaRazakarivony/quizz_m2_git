from flask import Blueprint, request, jsonify
from app.utils import summarize_text_simple

utils_routes = Blueprint('utils_routes', __name__)

@utils_routes.route('/summarize', methods=['POST'])
def summarize_text():
    """
    Résume un texte envoyé dans une requête POST.
    """
    data = request.get_json()
    text = data.get('text', '')
    ratio = data.get('ratio', 0.2)

    if not text:
        return jsonify({"error": "Le texte est requis pour le résumé."}), 400

    summary = summarize_text_simple(text, ratio)
    return jsonify({"summary": summary})
