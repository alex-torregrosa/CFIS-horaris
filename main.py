# CFIS-horaris, a timetable generator for CFIS students
#     Copyright (C) {year}  {name of author}
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.

import assignatura
import etseib
import fib
import horari
from colorama import Fore, Back, Style, init
init()

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


def generaHoraris(assig):
    if len(assig) > 1:
        horaris = []
        for grup in assig[0].grups:
            h = generaHoraris(assig[1:])
            for el in h:
                el.afegeixGrup(grup)
            horaris += h
        return horaris
    elif len(assig) == 1:
        h = []
        for grup in assig[0].grups:
            h.append(horari.Horari([grup]))
        return h

def filtraHoraris(horaris):
    final = []
    for horari in horaris:
        if horari.esPossible():
            final.append(horari)
    return final
def getKey(horario):
    if not horario.pucDinar():
        return 100 + horario.horaFi()
    return horario.horaFi()

def creaHoraris(assignatures):
    print("Generant horaris per a",len(assignatures),"assignatures...")
    h = generaHoraris(assignatures)
    print(len(h),"horaris trobats, filtrant...")
    h = filtraHoraris(h)
    print(len(h),"horaris possibles, ordenant per hora de finalització...")
    return sorted(h,key=getKey)


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

    horaris = creaHoraris(assignatures)
    n=0;
    while n < len(horaris):
        input("Prem enter per a mostrar l'horari "+str(n+1))
        print(horaris[n])
        horaris[n].representa()
        print(horaris[n].pucDinar())
        n += 1
