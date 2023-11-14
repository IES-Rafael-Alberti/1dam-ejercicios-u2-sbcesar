import pytest
from src.P2_02.Ej17 import sumaDigitos

@pytest.mark.parametrize(
    "num, expected",
    [
        (12345, 15),
        (9876, 30),
        (0, 0),
        (7, 7),
        (10101, 3),
    ]
)
def test_sumaDigitos_params(num, expected):
    assert sumaDigitos(num) == expected