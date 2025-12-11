from conversation import ConversationManager


def test_booking_flow_in_english():
    manager = ConversationManager()
    response1 = manager.process_input("Hello")
    assert "help" in response1.lower()

    response2 = manager.process_input("I want to book an appointment")
    assert "book" in response2.lower() or "cita" in response2.lower()

    slot_text = manager.booking_manager.available_slots[0].strftime('%Y-%m-%d %H:%M')
    response3 = manager.process_input(slot_text)
    assert "confirm" in response3.lower()

    response4 = manager.process_input("yes")
    assert "confirmed" in response4.lower()


def test_spanish_conversation():
    manager = ConversationManager()
    greeting = manager.process_input("Hola")
    assert "hola" in greeting.lower()

    faq_response = manager.process_input("¿Cuál es el precio?")
    assert "$" in faq_response or "precio" in faq_response

    rec_response = manager.process_input("¿Qué recomiendas para cejas delgadas?")
    assert "delgadas" in rec_response.lower() or "rehab" in rec_response.lower()
