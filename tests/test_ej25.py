import pytest
from src.P2_02.Ej25 import palabraMasLarga

@pytest.mark.parametrize(
    "frase, expected",
    [
        ("Esta es una frase de ejemplo", "ejemplo"),
        ("Otra prueba con palabras", "palabras"),
        ("Una palabra", "palabra"),

        ("No hay palabras", ""),
        ("", ""),
    ]
)
def test_palabraMasLarga_params(frase, expected):
    assert palabraMasLarga(frase) == expected
