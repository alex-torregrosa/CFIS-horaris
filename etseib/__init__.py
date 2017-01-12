import etseib.indus
def llistaCarreres():
    print()
    print("Carreres ETSEIB:")
    print("1: Enginyeria industrial")
    print()

def carrera(num):
    if(int(num) == 1):
        return indus.Indus()
    else:
        print("La carrera no existeix")
        exit()
