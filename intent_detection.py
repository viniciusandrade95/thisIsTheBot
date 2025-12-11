"""Intent detection for chatbot conversations."""
import re
from typing import Optional


class Intent:
    GREETING = "greeting"
    GOODBYE = "goodbye"
    BOOKING = "booking"
    FAQ = "faq"
    RECOMMENDATION = "recommendation"
    UNKNOWN = "unknown"


def _contains_word(text: str, words) -> bool:
    return any(re.search(rf"\b{re.escape(word)}\b", text) for word in words)


def detect_intent(text: str, state: Optional[dict] = None) -> str:
    """Detect intent from user text using simple keyword rules."""
    if not text:
        return Intent.UNKNOWN

    lower_text = text.lower()
    state = state or {}

    if state.get("booking_in_progress"):
        return Intent.BOOKING

    greetings = ["hello", "hi", "hey", "hola", "buenas", "buenos dias", "buenas tardes", "buenas noches"]
    goodbyes = ["bye", "goodbye", "see you", "adios", "hasta luego"]
    booking_keywords = ["book", "appointment", "schedule", "reserve", "cita", "reservar", "agendar"]
    recommendation_keywords = ["recommend", "suggest", "recomienda", "recomiendas", "sugerencia", "recomendar", "recomend"]
    faq_triggers = ["what", "how", "when", "price", "cuánto", "cuanto", "donde", "qué", "que", "por qué", "porque"]

    if _contains_word(lower_text, greetings):
        return Intent.GREETING
    if _contains_word(lower_text, goodbyes):
        return Intent.GOODBYE
    if _contains_word(lower_text, booking_keywords):
        return Intent.BOOKING
    if _contains_word(lower_text, recommendation_keywords):
        return Intent.RECOMMENDATION
    if "?" in lower_text or _contains_word(lower_text, faq_triggers):
        return Intent.FAQ

    return Intent.UNKNOWN
