import classe

class Grup:
    """Representa un grup, incloent-hi el seu horari"""
    def __init__(self, num):
        self.num = num
        self.classes = []
        self.assig = ""
        self.facu = "#";

    def afegeixClasse(self, classe):
        self.classes.append(classe)

    def esCompatible(self,grup2):
        for classe in self.classes:
            for classe2 in grup2.classes:
                if not classe.esCompatible(classe2):
                    return False
        return True
    def horaFi(self):
        fi = 0
        for classe in self.classes:
            if classe.end > fi:
                fi = classe.end
        return fi

    def __repr__(self):
        return '{}: grup {} '.format(self.assig.nom,
                                     self.num)
