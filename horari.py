class Horari(object):
    """Representa un possible horari de doble titulació, amb llista
    de grups respectius."""
    def __init__(self,  grups):
        # self.assignatures = assig
        self.grups = grups

    def afegeixGrup(self,grup):
        self.grups.append(grup)

    def esPossible(self):
        for x in range(0, len(self.grups)):
            for y in range(x+1, len(self.grups)):
                if not self.grups[x].esCompatible(self.grups[y]):
                    return False
        return True

    def creaGrafica(self):
        graf = [['·' for x in range(0,5)] for y in range(0,28)]
        # print("size",len(graf))
        for grup in self.grups:
            for classe in grup.classes:
                for h in range(int((classe.start-8)*2 ), int((classe.end-8)*2)):
                    # print("h=",h)
                    graf[h][classe.day] = grup.facu

        return graf

    def representa(self):
        graf = self.creaGrafica()
        c = 8.0
        for row in graf:
            print('{:4.1f}'.format(c),":",end=" ")
            c+= 0.5
            for el in row:
                print(el,end=" ")
            print()

    def pucDinar(self):
        graf = self.creaGrafica()
        for d in range(0,5):
            lliures = 0
            for x in range(8,16):
                if graf[x][d] == '·':
                    lliures += 1
            if lliures == 0:
                return False
        return True

    def horaFi(self):
        fi = 0
        for grup in self.grups:
            f = grup.horaFi()
            if f > fi:
                fi = f
        return fi
    def __repr__(self):
        res = ""
        for g in self.grups:
            res += g.__repr__()
            res += ", "
        return res
