import classe

class Assignatura:
    """docstring for assignatura."""
    def __init__(self, nom, codi):
        self.nom = nom
        self.codi = codi
        self.grups = []
    def afegeixGrup(self,grup):
        self.grups.append(grup)
