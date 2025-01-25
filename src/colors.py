class Colors():
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'

    def __init__(self, code, color):
        self.code = code
        self.color = color

    def __str__(self):
        return self.color