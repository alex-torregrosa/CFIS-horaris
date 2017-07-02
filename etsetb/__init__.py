# CFIS-horaris, a timetable generator for CFIS students
#     Copyright (C) 2017  Roger Serrat
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
