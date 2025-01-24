import pytest
from src.dni import Dni
import random
from src.colors import Colors

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

pytest.mark.dni_aleatorio
def test_random_dni():
    
    # while acumulator
    minNumberDni = 11111111
    maxNumberDni = 999999999

    asciiLetterA = 65
    asciiLetterZ = 90
    
    testCases = []
    numberCases = 30
    while len(testCases) <= numberCases:
        numberDni = random.randint(minNumberDni, maxNumberDni)
        asciiCharacter = random.randint(asciiLetterA, asciiLetterZ)

        testCases.append(str(numberDni) + chr(asciiCharacter))
    
    #pytest -s to print with pytest
    for dni in testCases:
        if Dni(dni).isDniValid():
            print(f"{Colors.GREEN} Valid DNI:{Colors.RESET} {dni}")
        else:
            print(f"{Colors.RED} Invalid DNI: {Colors.RESET} {dni}")

@pytest.mark.dni_invalido
def test_invalid_dni():
    invalidDnis = [
        "43770614Z",
        "109554436M",
        "315845952J",
        "828529506A",
        "925447738E",
        "32884726C",
        "506819213Z",
        "139981092V",
        "652673519L",
        "547628548I",
        "983419495R",
        "898273005H",
        "",
        "0123"
    ]

    for dni in invalidDnis:
        assert Dni(dni).isDniValid() is False