import fib.info
def llistaCarreres():
    print()
    print("Carreres FIB:")
    print("1: Enginyeria informàtica")
    print()

def carrera(num):
    if(int(num) == 1):
        return info.Info()
    else:
        print("La carrera no existeix")
        exit()
