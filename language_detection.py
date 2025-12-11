"""Language detection utilities for the chatbot."""
import re

SUPPORTED_LANGUAGES = {"en", "es"}
SPANISH_HINTS = ["hola", "buenos", "gracias", "¿", "¡", "ción", "que", "qué", "cómo", "dónde", "precio", "cita"]


def detect_language(text: str) -> str:
    """Detect language code ('en' or 'es'), defaulting to English on failure."""
    if not text or not text.strip():
        return "en"
    lower_text = text.lower()
    if any(hint in lower_text for hint in SPANISH_HINTS):
        return "es"
    if re.search(r"[áéíóúñ]", lower_text):
        return "es"
    return "en"
