from booking import BookingManager, LANG_TEXTS


def test_generate_slots():
    manager = BookingManager()
    assert len(manager.available_slots) > 0


def test_request_invalid_date():
    manager = BookingManager()
    result = manager.request_appointment("not a date", "en")
    assert result["slot"] is None
    assert LANG_TEXTS["en"]["invalid"].split('.')[0] in result["message"]


def test_booking_and_confirmation_flow():
    manager = BookingManager()
    slot = manager.available_slots[0]
    response = manager.request_appointment(slot.strftime('%Y-%m-%d %H:%M'), "en")
    assert response["slot"] == slot
    confirmation = manager.confirm_appointment(slot, "yes", "en")
    assert "confirmed" in confirmation.lower()
    assert slot not in manager.available_slots
