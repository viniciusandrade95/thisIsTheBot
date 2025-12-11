from intent_detection import Intent, detect_intent


def test_greeting_intent():
    assert detect_intent("Hello there") == Intent.GREETING


def test_goodbye_intent():
    assert detect_intent("Goodbye") == Intent.GOODBYE


def test_booking_intent():
    assert detect_intent("I want to book an appointment") == Intent.BOOKING


def test_faq_intent():
    assert detect_intent("What are your prices?") == Intent.FAQ


def test_recommendation_intent():
    assert detect_intent("Can you recommend something?") == Intent.RECOMMENDATION


def test_booking_bias_when_in_progress():
    assert detect_intent("random text", {"booking_in_progress": True}) == Intent.BOOKING
