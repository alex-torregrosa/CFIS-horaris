import assignatura
import classe
import grup
from colorama import Fore, Style

class Fisica:
    
    def __init__(self):
        self.llista = self.llistaAssignatures()
        self.name = "Enginyeria Física [ETSETB]"
     
    def llistaAssignatures(self):
        f = open("etsetb/assig_fis/assig_fisica.txt")
        l = []
        for line in f:
            l.append(line)
        l=[x.strip() for x in l]
        return l
        
    def selecciona(self):
        print("A continuació tens una llista d'assignatures, selecciona la que desitjis:")
        print()
        for x in range(0,len(self.llista)):
            print(x+1,":",self.llista[x])

        print()
        i = input("escriu el numero de l'assignatura desitjada: ")
        num = int(i)
        conf = input("Has seleccionat " + self.llista[num-1] + "? (s/n) :")
        if conf != "s":
            return selecciona()
        else:
            codi = self.llista[num-1]
            a = assignatura.Assignatura(self.llista[num-1], codi,Fore.GREEN+"T"+Style.RESET_ALL)
            return a    

    def obteHorari(self, assig):
        base = "etsetb/assig_fis/"
        base += assig.codi.lower() + ".txt"
        r = open(base)
        ls = []
        for line in r:
            ls.append(line)
        ls = [x.strip() for x in ls]
        lis = []
        for el in ls:
            if len(el) > 0:
                lis.append(el.split())
        def gkey(i):
            return int(i[1])
        horari = sorted(lis, key=gkey)
        lastg = 0
        isGroup = True
        gcal = [[False for x in range(0,5)] for y in range(0,28)] #per si només hi ha subgrups
        for cl in horari:
            act = int(cl[1])
            if act != lastg:
                if not isGroup: # Venim de l'ultim subgrup del grup anterior
                    self.parseCal(scal,lastg,assig)
                elif isGroup and lastg!=0 and act==lastg+10: #només hi ha grups
                    self.parseCal(gcal,lastg,assig)
                if act%10 == 0:
                    # print("Grup",act)
                    isGroup = True
                    gcal = [[False for x in range(0,5)] for y in range(0,28)]
                else:
                    # print("  subgrup",act)
                    isGroup = False
                    scal = [row[:] for row in gcal]
                lastg = act
            h = (int(cl[3].split(':')[0]) - 8)*2
            if int(cl[3].split(':')[1]) == 30:
                h += 1   
            d = int(cl[2])-1
            if isGroup:
                gcal[h][d] = True
            else:
                scal[h][d] = True
        if isGroup:
            self.parseCal(gcal,lastg,assig)
        else:
            self.parseCal(scal,lastg,assig)

    def parseCal(self,cal, grupo, assig):
        started = False
        g = grup.Grup(grupo)
        start = -1
        for d in range(0,5):
            for f in range(0,28):
                if cal[f][d]:
                    if not started:
                        start = (f/2)+8
                        started = True
                else:
                    if started:
                        g.afegeixClasse(classe.Classe(start, (f/2)+8,d))
                    started = False
            if started:
                g.afegeixClasse(classe.Classe(start, (f/2)+8,d))
        assig.afegeixGrup(g)
        #grupo += 10

    def creaAssignatura(self):
        a = self.selecciona()
        self.obteHorari(a)
        print("Assignatura",a.nom,"creada!")
        return a
