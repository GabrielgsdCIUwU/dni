# Validación de DNI

Este proyecto es una kata de programación orientada a objetos cuyo objetivo es comprobar la validez de un DNI (Documento Nacional de Identidad) español.

## Descripción

El proyecto consiste en una serie de clases y métodos que permiten validar un DNI. La validación se realiza comprobando que el formato del DNI es correcto y que la letra de control coincide con la calculada a partir del número.

## Estructura del Proyecto

El proyecto está organizado en los siguientes directorios y archivos:

### src

- colors.py
- dni.py
- tabla_asignacion.py

### test

- test_dni.py
- test_tabla.py


## Instalación

Para instalar las dependencias necesarias, ejecuta:

```sh
pip install -r requirements.txt
```

## Uso
Para utilizar la clase y métodos de este proyecto, puedes importar desde el módulo src. Aquí tienes un ejemplo de cómo validar un DNI:

```python
from src.dni import Dni

dni = "80117501Z"
if Dni(dni).isDniValid():
    print("El DNI es válido")
else:
    print("El DNI no es válido")
```

También puedes usar el `app.py` para generar DNI aleatorio o solo válido.
```sh
py app.py
```

## Tests

Para ejecutar los tests, utiliza pytest. Los tests están ubicados en el directorio test y cubren diferentes casos de uso para la validación de DNIs.

```sh
pytest
```

En caso de que quieras ver también los prints usa este otro comando:
```sh
pytest -s
```


