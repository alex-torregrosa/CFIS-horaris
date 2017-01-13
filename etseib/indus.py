import requests
import etseib.parsers
import assignatura
import classe
import grup

class Indus:
    """docstring for Indus."""
    def __init__(self):
        super(Indus, self).__init__()
        self.llista = self.llistaAssignatures()
        self.name = "Enginyeria Industrial [ETSEIB]"

    def llistaAssignatures(self):
        r = requests.get("https://guiadocent.etseib.upc.edu/simgen/form/simgen.php?lang=ca&degree=752&semester=next")
        p = etseib.parsers.parserLlista();
        p.feed(r.text)
        return p.llista

    def selecciona(self):
        print("A continuació tens una llista d'assignatures, selecciona la que desitjis:")
        print()
        for x in range(0,len(self.llista)):
            print(x+1,":",self.llista[x][0])

        print()
        i = input("escriu el numero de l'assignatura desitjada: ")
        num = int(i)
        conf = input("Has seleccionat " + self.llista[num-1][0] + "? (s/n) :")
        if conf != "s":
            return selecciona()
        else:
            codi = self.llista[num-1][1].split("_")[1]
            a = assignatura.Assignatura(self.llista[num-1][0], codi,"E")
            return a

    def obteHorari(self, assig):
        base = "https://guiadocent.etseib.upc.edu/simgen/action/result.php?degree=752&lang=ca&semester=next&grup_"
        base += str(assig.codi) + "_"
        grupo = 10
        existeix = True
        print("Buscant horaris per a",assig.nom,"...")
        while existeix:
            r = requests.get(base+str(grupo))
            if(r.text.find("#F6CECE") == -1):
                existeix = False
            else:
                # print("Grup trobat:",grupo)
                p = etseib.parsers.parserHoraris()
                p.feed(r.text)
                started = False
                g = grup.Grup(grupo)
                start = -1
                for d in range(0,5):
                    for f in range(0,28):
                        if p.cal[f][d]:
                            if not started:
                                start = (f/2) + 8
                                started = True
                        else:
                            if started:
                                g.afegeixClasse(classe.Classe(start, (f/2)+8,d))
                            started = False
                    if started:
                        g.afegeixClasse(classe.Classe(start, (f/2)+8,d))
                assig.afegeixGrup(g)
                grupo += 10

    def creaAssignatura(self):
        a = self.selecciona()
        self.obteHorari(a)
        print("Assignatura",a.nom,"creada!")
        return a

if __name__ == '__main__':
    ind = Indus();
    print(ind.selecciona())
