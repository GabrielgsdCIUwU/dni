import pytest
from src.tabla_asignacion import TablaAsignacion

@pytest.mark.obtener_tabla
def test_get_table():
    assert TablaAsignacion().getTable()

@pytest.mark.obtener_letra
def test_get_letter():
    tabla_asignation = TablaAsignacion()
    table = tabla_asignation.getTable()
    
    for i in range(len(table)):
        assert tabla_asignation.getLetter(i)