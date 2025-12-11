from recommendation import get_recommendation


def test_thin_brows_recommendation():
    response = get_recommendation("My brows are thin", "en")
    assert "thin" in response.lower()


def test_generic_recommendation():
    response = get_recommendation("Just browsing", "en")
    assert "popular" in response.lower()


def test_spanish_recommendation():
    response = get_recommendation("Cejas pobladas", "es")
    assert "pobladas" in response
