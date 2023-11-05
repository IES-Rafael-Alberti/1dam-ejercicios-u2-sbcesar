import pytest
from src.P2_02.Ej9 import pedirContrasena

@pytest.mark.parametrize(
    "input_password, expected",
    [
        ("usuario", True),
        ("contrasena_incorrecta", False),
        ("password123", False)
    ]
)

def test_pedirContrasena_params(input_password, expected):
    assert pedirContrasena(input_password) == expected