import random
from src.colors import Colors
from src.dni import Dni
from os import system, name
from src.tabla_asignacion import TablaAsignacion
import time

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def is_valid_option(option):
    try:
        user_option = int(option)
        if user_option not in [1, 2, 3]:
            return False
        return user_option
    except ValueError:
        return False

def is_valid_quantity(quantity):
    try:
        user_quantity = int(quantity)
        if user_quantity < 1:
            return False
        return user_quantity
    except ValueError:
        return False

def randomDni(numberCases):    
    minNumberDni = 11111111
    maxNumberDni = 99999999

    asciiLetterA = 65
    asciiLetterZ = 90

    i = 0
    validDni = 0
    invalidDni = 0
    while i <= numberCases:
        numberDni = random.randint(minNumberDni, maxNumberDni)
        asciiCharacter = random.randint(asciiLetterA, asciiLetterZ)

        dni = f"{numberDni}{chr(asciiCharacter)}"

        if Dni(dni).isDniValid():
            print(f"{Colors.GREEN} Valid DNI:{Colors.RESET} {dni}")
            validDni += 1
        else:
            print(f"{Colors.RED} Invalid DNI: {Colors.RESET} {dni}")
            invalidDni += 1
        
        i += 1
    print("-" * 40)
    print(f"DNIs inválidos generados: {Colors.RED} {invalidDni} {Colors.RESET}")
    print(f"DNIs válidos generados: {Colors.GREEN} {validDni} {Colors.RESET}")

def validDni(numberCases):
    minNumberDni = 11111111
    maxNumberDni = 99999999

    i = 0
    while i < numberCases:
        numberDni = random.randint(minNumberDni, maxNumberDni)
        letter = TablaAsignacion().calculateLetter(numberDni)
        
        dni = f"{numberDni}{letter}"
        
        if Dni(dni).isDniValid():
            print(f"{Colors.GREEN} Valid DNI:{Colors.RESET} {dni}")
            i += 1
        

while True:
    print("Que tipos de DNI quieres generar?")
    print("1. DNI valido")
    print("2. DNI aleatorio")
    print("3. Salir")

    userOption = is_valid_option(input())
    if userOption:
    
        if userOption == 3:
            clear()
            break
        
        print("Cuántos quieres generar?")
        userQuantity = is_valid_quantity(input())
        if userQuantity:
            if userOption == 1:
                validDni(userQuantity)
            if userOption == 2:
                randomDni(userQuantity)
            input("Presiona cualquier tecla para reiniciar")
        else:
            print("Cantidad no valida, debe ser un número natural y mayor a 0")
            time.sleep(2)
    else:
        print("Opcion no valida, solo puedes elegir 1 o 2")
        time.sleep(2)
    
    clear()
    
                


