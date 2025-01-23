class TablaAsignacion:
    
    def __init__(self):
        self.table = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']

    def getTable(self):
        return self.table
    
    def getLetter(self, position):
        try:
            return self.tabla[position]
        except IndexError:
            return None
    
