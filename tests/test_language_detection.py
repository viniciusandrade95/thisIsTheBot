import pytest

from language_detection import detect_language


def test_detects_english():
    assert detect_language("Hello") == "en"


def test_detects_spanish():
    assert detect_language("Hola, ¿cómo estás?") == "es"


def test_empty_defaults_to_en():
    assert detect_language("") == "en"
