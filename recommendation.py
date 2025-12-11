"""Recommendation logic for brow services and products."""
from typing import Dict

RECOMMENDATIONS: Dict[str, Dict[str, str]] = {
    "en": {
        "thin": "For thin brows, we recommend our Brow Rehab Package with nourishing serums.",
        "full": "To maintain full brows, try our signature brow lamination and tint combo.",
        "default": "Our most popular service is the precision Brow Design with tint for a polished look.",
    },
    "es": {
        "thin": "Para cejas delgadas, recomendamos nuestro Paquete Brow Rehab con sueros nutritivos.",
        "full": "Para mantener cejas pobladas, prueba nuestra laminación con tinte.",
        "default": "Nuestro servicio más popular es el Diseño de Cejas con tinte para un acabado pulido.",
    },
}


def get_recommendation(user_message: str, lang: str) -> str:
    lang = lang if lang in RECOMMENDATIONS else "en"
    lower = user_message.lower()
    if "thin" in lower or "delgada" in lower:
        return RECOMMENDATIONS[lang]["thin"]
    if "full" in lower or "poblada" in lower:
        return RECOMMENDATIONS[lang]["full"]
    return RECOMMENDATIONS[lang]["default"]
