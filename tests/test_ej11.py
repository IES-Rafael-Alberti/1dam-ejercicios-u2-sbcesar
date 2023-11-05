import pytest
from src.P2_02.Ej11 import palabraAlReves

@pytest.mark.parametrize(
    "palabra, expected",
    [
        ("hola", "aloh"),  # Palabra invertida: hola -> aloh
        ("python", "nohtyp"),  # Palabra invertida: python -> nohtyp
        ("radar", "radar"),  # Palabra invertida: radar -> radar
        ("casa", "asac"),  # Palabra invertida: casa -> asac
    ]
)
def test_palabraAlReves_params(palabra, expected):
    assert palabraAlReves(palabra) == expected
