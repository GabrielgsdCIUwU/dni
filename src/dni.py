from src.tabla_asignacion import TablaAsignacion as TA
class Dni:
    LENGTH_DNI = 9

    def __init__(self, dni=""):
        self.dni = dni

    def getDni(self):
        return self.dni
    
    def getLetter(self):
        return self.getDni()[-1]
    
    def getNumber(self):
        return self.getDni()[:-1]

    def isInputDniValid(self):
        return bool(self.getDni())

    def isLengthDniValid(self):
        return len(self.getDni()) == self.LENGTH_DNI

    def isDniValid(self):
        return self.isInputDniValid() and self.isLengthDniValid() and \
        TA().calculateLetter(self.getNumber()) == self.getLetter()