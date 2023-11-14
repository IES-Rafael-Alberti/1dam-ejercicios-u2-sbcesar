import pytest
from src.P2_02.Ej10 import esPrimo

@pytest.mark.parametrize(
    "num, expected",
    [
        (2, True),
        (3, True),
        (17, True),
        (29, True),

        (4, False),
        (20, False)
    ]
)
def test_esPrimo_params(num, expected):
    assert esPrimo(num) == expected
