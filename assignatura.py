import classe

class Assignatura:
    """docstring for assignatura."""
    def __init__(self, nom, codi,f):
        self.nom = nom
        self.codi = codi
        self.grups = []
        self.facu = f
    def afegeixGrup(self,grup):
        grup.assig = self
        grup.facu = self.facu
        self.grups.append(grup)

    # def llistaGrups():
    #     gr = []
    #     for g in grups
    # def buscaGrup(self, idg):
    #     for g in grups:
    #         if g.num == idg:
    #             return g
    #     print("ERROR: grup",idg,"no trobat a",self.nom)
    #     return -1
