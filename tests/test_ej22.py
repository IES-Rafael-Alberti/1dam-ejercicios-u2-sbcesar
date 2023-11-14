import pytest
from src.P2_02.Ej22 import contardorDigitos

@pytest.mark.parametrize(
    "numero, expected",
    [
        (12345, (2, 3)),
        (9876, (4, 0)),
        (10101, (2, 3)),
        (0, (0, 0)),
        (7, (0, 1)),
    ]
)
def test_contadorDigitos_params(numero, expected):
    assert contardorDigitos(numero) == expected
