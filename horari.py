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
