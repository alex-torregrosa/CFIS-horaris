import assignatura
import etseib
import fib

def obteCarrera(facu):
    if facu == "1":
        print()
        etseib.llistaCarreres()
        c = input("Selecciona una carrera: ")
        return etseib.carrera(c)
    if facu == "2":
        print()
        fib.llistaCarreres()
        c = input("Selecciona una carrera: ")
        return fib.carrera(c)
    else:
        print("La facultat seleccionada no està disponible")
        exit()
def listAssig(assig):
    for el in assig:
        print(" ",el.nom)

if __name__ == '__main__':
    print("Facultats disponibles:")
    print("1: ETSEIB")
    print("2: FIB")
    print()

    i1 = input("Selecciona la primera facultat: ")
    c1 = obteCarrera(i1)
    i2 = input("Selecciona la segona facultat: ")
    c2 = obteCarrera(i2)

    assignatures = []

    # Carrera 1
    print()
    cancelled = False
    while not cancelled:
        print("Et trobes a", c1.name)
        print("Actualment tens",len(assignatures), "assignatures:")
        listAssig(assignatures)
        ass = input("Vols afegir una assignatura? (s/n): ")
        if ass == "s":
            assignatures.append(c1.creaAssignatura())
        else:
            cancelled = True
    cancelled = False
    # Carrera 2
    print()
    while not cancelled:
        print("Et trobes a", c2.name)
        print("Actualment tens",len(assignatures), "assignatures:")
        listAssig(assignatures)
        ass = input("Vols afegir una assignatura? (s/n): ")
        if ass == "s":
            assignatures.append(c2.creaAssignatura())
        else:
            cancelled = True
