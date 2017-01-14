import classe

class Assignatura:
    """docstring for assignatura."""
    def __init__(self, nom, codi,f):
        self.nom = nom
        self.codi = codi
        self.grups = []
        self.facu = f
    def afegeixGrup(self,grup):
        for x in range(0,len(self.grups)):
            if self.grups[x].esIgual(grup):
                self.grups[x].num = str(self.grups[x].num) + '/' +str(grup.num)
                return 0
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
