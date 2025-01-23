class Dni:
    def __init__(self, dni):
        self.dni = dni

    def getDni(self):
        return self.dni
    
    def getLetter(self):
        return self.getDni()[-1]