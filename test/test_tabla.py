import pytest
from src.tabla_asignacion import TablaAsignacion

@pytest.mark.obtener_tabla
def test_get_table():
    assert TablaAsignacion().getTable()

@pytest.mark.obtener_letra
def test_get_letter_from_position():
    tabla_asignation = TablaAsignacion()
    table = tabla_asignation.getTable()
    
    for i in range(len(table)):
        assert tabla_asignation.getLetterFromPositionTable(i)

@pytest.mark.calcular_letra
def test_calculate_letter():
    tabla_asignation = TablaAsignacion()
    letter = tabla_asignation.calculateLetter("77422360")
    assert letter == 'J'