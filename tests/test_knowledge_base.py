from knowledge_base import answer_question


def test_answers_price_question_en():
    response = answer_question("What is the price?", "en")
    assert "$35" in response


def test_answers_location_question_es():
    response = answer_question("¿Dónde están ubicados?", "es")
    assert "centro" in response


def test_unknown_question_returns_default():
    response = answer_question("Do you sell coffee?", "en")
    assert "don't have" in response
