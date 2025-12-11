"""Booking management for the brow designer shop chatbot."""
from datetime import datetime, timedelta
from typing import Dict, Optional

LANG_TEXTS: Dict[str, Dict[str, str]] = {
    "en": {
        "ask_date": "Sure! What date and time would you like to book?",
        "invalid": "I couldn't understand that date. Could you rephrase?",
        "slot_unavailable": "Sorry, that slot is not available. Please choose another time.",
        "confirm": "I can book {time}. Should I confirm it? (yes/no)",
        "confirmed": "Your appointment for {time} is confirmed!",
        "cancelled": "No problem, I didn't make the booking. Let me know if you want another time.",
    },
    "es": {
        "ask_date": "¡Claro! ¿Qué fecha y hora prefieres?",
        "invalid": "No pude entender esa fecha. ¿Puedes decirla de otra forma?",
        "slot_unavailable": "Lo siento, ese horario no está disponible. Por favor elige otro.",
        "confirm": "Puedo agendar {time}. ¿Confirmo la cita? (sí/no)",
        "confirmed": "¡Tu cita para {time} está confirmada!",
        "cancelled": "No hay problema, no hice la reserva. Avísame si quieres otro horario.",
    },
}


class BookingManager:
    """Manage in-memory booking slots for demo purposes."""

    def __init__(self) -> None:
        self.available_slots = self._generate_slots()

    def _generate_slots(self):
        now = datetime.now().replace(minute=0, second=0, microsecond=0)
        slots = []
        for day_offset in range(1, 4):
            day = now + timedelta(days=day_offset)
            for hour in (10, 12, 14, 16):
                slots.append(day.replace(hour=hour))
        return slots

    def parse_datetime(self, text: str) -> Optional[datetime]:
        patterns = ["%Y-%m-%d %H:%M", "%Y/%m/%d %H:%M", "%d-%m-%Y %H:%M", "%d/%m/%Y %H:%M"]
        for pattern in patterns:
            try:
                return datetime.strptime(text.strip(), pattern)
            except (ValueError, AttributeError):
                continue
        return None

    def is_available(self, slot: datetime) -> bool:
        return slot in self.available_slots

    def request_appointment(self, text: str, lang: str) -> Dict[str, Optional[datetime]]:
        lang = lang if lang in LANG_TEXTS else "en"
        parsed = self.parse_datetime(text)
        if not parsed:
            return {"message": LANG_TEXTS[lang]["invalid"], "slot": None}
        slot = parsed.replace(minute=0, second=0, microsecond=0)
        if not self.is_available(slot):
            return {"message": LANG_TEXTS[lang]["slot_unavailable"], "slot": None}
        return {"message": LANG_TEXTS[lang]["confirm"].format(time=slot.strftime('%Y-%m-%d %H:%M')), "slot": slot}

    def confirm_appointment(self, slot: datetime, confirm_yes_no: str, lang: str) -> str:
        lang = lang if lang in LANG_TEXTS else "en"
        yes_words = ["yes", "sí", "si", "confirm", "ok"]
        if confirm_yes_no.lower() in yes_words:
            if slot in self.available_slots:
                self.available_slots.remove(slot)
            return LANG_TEXTS[lang]["confirmed"].format(time=slot.strftime('%Y-%m-%d %H:%M'))
        return LANG_TEXTS[lang]["cancelled"]
