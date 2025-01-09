import os
from transformers import pipeline
from gtts import gTTS
from langdetect import detect

def save_uploaded_file(upload_folder, file):
    """Sauvegarde un fichier téléchargé dans le dossier spécifié."""
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)
    return file_path

def summarize_text_simple(text, ratio=0.2):
    """
    Résume un texte en utilisant Hugging Face Transformers (modèle BART).

    :param text: Texte à résumer (chaîne de caractères).
    :param ratio: Proportion du texte à conserver dans le résumé (entre 0 et 1).
    :return: Résumé sous forme de chaîne de caractères.
    """
    # Charger le pipeline de résumé avec le modèle BART
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    # Obtenez le résumé du texte
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)

    # Retourner le résumé
    return summary[0]['summary_text']

def detect_language(text):
    """
    Détecte la langue du texte.
    :param text: Texte dont la langue doit être détectée.
    :return: Code de la langue détectée (ex : 'en', 'fr').
    """
    try:
        return detect(text)
    except Exception as e:
        print(f"Erreur lors de la détection de la langue : {e}")
        return 'en'  # Langue par défaut

def text_to_speech(text):
    """
    Convertit le texte en audio avec une détection automatique de la langue.
    :param text: Texte à convertir en parole.
    """
    try:
        lang = detect_language(text)
        print(f"Langue détectée : {lang}")

        # Conversion du texte en audio
        tts = gTTS(text=text, lang=lang)
        file_name = "output.mp3"
        tts.save(file_name)

        # Lecture du fichier audio
        os.system("start output.mp3")  # Windows
        # Pour Linux : os.system('xdg-open output.mp3')
        # Pour macOS : os.system('open output.mp3')
    except Exception as e:
        print(f"Erreur : {e}")