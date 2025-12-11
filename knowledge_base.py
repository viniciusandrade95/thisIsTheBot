"""Simple FAQ knowledge base for brow services."""
from typing import Dict, List

FAQ_DATA: Dict[str, List[dict]] = {
    "en": [
        {"keywords": ["price", "cost"], "answer": "Our brow shaping starts at $35, with tinting and lamination options available."},
        {"keywords": ["hours", "open", "closing"], "answer": "We are open Monday to Saturday from 9am to 7pm."},
        {"keywords": ["location", "where"], "answer": "We are located downtown near the plaza, with easy parking nearby."},
    ],
    "es": [
        {"keywords": ["precio", "costo"], "answer": "El diseño de cejas inicia en $35, con opciones de tinte y laminado."},
        {"keywords": ["horario", "abierto", "cierran"], "answer": "Abrimos de lunes a sábado de 9am a 7pm."},
        {"keywords": ["ubicación", "dónde", "donde"], "answer": "Estamos en el centro, cerca de la plaza, con estacionamiento cercano."},
    ],
}

DEFAULT_ANSWERS = {
    "en": "I'm sorry, I don't have that information right now.",
    "es": "Lo siento, no tengo esa información en este momento.",
}


def answer_question(query: str, lang: str) -> str:
    """Return an FAQ answer if one matches the query."""
    lang = lang if lang in FAQ_DATA else "en"
    lower_query = query.lower()
    for entry in FAQ_DATA.get(lang, []):
        if any(keyword in lower_query for keyword in entry["keywords"]):
            return entry["answer"]
    return DEFAULT_ANSWERS.get(lang, DEFAULT_ANSWERS["en"])
