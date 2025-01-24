from enum import Enum

class Colors(Enum):
    RESET = (1, '\033[0m')
    RED = (2, '\033[91m')
    GREEN = (3, '\033[92m')

    def __init__(self, code, color):
        self.code = code
        self.color = color

    def __str__(self):
        return self.color