import pytest
from src.dni import Dni

@pytest.mark.obtener_dni
def test_get_dni():
    dni = "78484464T"
    assert Dni(dni).getDni() == dni

@pytest.mark.obtener_letra
def test_get_letter():
    dni = "78484464T"
    assert Dni(dni).getLetter() == "T"

@pytest.mark.obtener_numero
def test_get_number():
    dni = "39492958A"
    assert Dni(dni).getNumber() == "39492958"

pytest.mark.dni_valido
def test_valid_dni():
    validDnis = [
        "78484464T",
        "72376173A",
        "01817200Q",
        "95882054E",
        "63587725Q",
        "26861694V",
        "21616083Q",
        "26868974Y",
        "40135330P",
        "89044648X",
        "80117501Z",
        "34168723S",
        "76857238R",
        "66714505S",
        "66499420A",

    ]

    for dni in validDnis:
        assert  Dni(dni).isDniValid()