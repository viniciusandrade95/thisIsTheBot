"""Conversation manager orchestrating chatbot responses."""
from dataclasses import dataclass, field
from typing import Optional

from booking import LANG_TEXTS, BookingManager
from intent_detection import Intent, detect_intent
from knowledge_base import answer_question
from language_detection import detect_language
from recommendation import get_recommendation


def translate_text(en_text: str, es_text: str, lang: str) -> str:
    return es_text if lang == "es" else en_text


@dataclass
class ConversationState:
    current_language: str = "en"
    booking_in_progress: bool = False
    tentative_slot: Optional[str] = None
    last_slot_datetime: Optional[object] = None


@dataclass
class ConversationManager:
    booking_manager: BookingManager = field(default_factory=BookingManager)
    state: ConversationState = field(default_factory=ConversationState)

    def process_input(self, user_input: str) -> str:
        self.state.current_language = detect_language(user_input)
        lang = self.state.current_language

        intent = detect_intent(user_input, {
            "booking_in_progress": self.state.booking_in_progress
        })

        if intent == Intent.GREETING:
            return translate_text("Hi there! How can I help with your brows today? 😊", "¡Hola! ¿En qué puedo ayudarte con tus cejas hoy? 😊", lang)
        if intent == Intent.GOODBYE:
            self._reset_booking_state()
            return translate_text("Thanks for visiting! Have a great day!", "¡Gracias por tu visita! ¡Que tengas un gran día!", lang)

        if self.state.booking_in_progress:
            return self._handle_booking_flow(user_input)

        if intent == Intent.BOOKING:
            self.state.booking_in_progress = True
            return translate_text("Great! Let's book your appointment.", "¡Genial! Hagamos tu cita.", lang) + " " + LANG_TEXTS[lang]["ask_date"]

        if intent == Intent.FAQ:
            return answer_question(user_input, lang)

        if intent == Intent.RECOMMENDATION:
            return get_recommendation(user_input, lang)

        return translate_text("I'm here to help with brows, bookings, or questions!", "¡Estoy aquí para ayudarte con cejas, reservaciones o preguntas!", lang)

    def _handle_booking_flow(self, user_input: str) -> str:
        lang = self.state.current_language
        yes_words = ["yes", "sí", "si", "confirm", "ok"]
        no_words = ["no", "not", "cancel", "no gracias"]

        if self.state.tentative_slot:
            if user_input.lower() in yes_words:
                confirmation = self.booking_manager.confirm_appointment(self.state.last_slot_datetime, user_input, lang)
                self._reset_booking_state()
                return confirmation
            if user_input.lower() in no_words:
                message = LANG_TEXTS[lang]["cancelled"]
                self._reset_booking_state()
                return message

        result = self.booking_manager.request_appointment(user_input, lang)
        slot = result.get("slot")
        self.state.last_slot_datetime = slot
        if slot:
            self.state.tentative_slot = slot.strftime('%Y-%m-%d %H:%M')
            self.state.booking_in_progress = True
            return result["message"]
        return result["message"]

    def _reset_booking_state(self) -> None:
        self.state.booking_in_progress = False
        self.state.tentative_slot = None
        self.state.last_slot_datetime = None
