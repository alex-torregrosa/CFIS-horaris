import classe

class Grup:
    """docstring for Grup."""
    def __init__(self, num):
        self.num = num
        self.classes = []

    def afegeixClasse(self, classe):
        self.classes.append(classe)
