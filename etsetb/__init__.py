import etsetb.fisica

def llistaCarreres():
    print()
    print("Carreres ETSETB:")
    print("1: Enginyeria física")
    print("2: Telecos (encara no disponible)")
    print()

def carrera(num):
    if(int(num) == 1):
        return fisica.Fisica()
    elif(int(num)==2):
        print("No disponible!!")
        exit()
    else:
        print("La carrera no existeix")
        exit()
