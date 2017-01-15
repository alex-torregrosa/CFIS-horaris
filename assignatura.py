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

import classe

class Assignatura:
    """docstring for assignatura."""
    def __init__(self, nom, codi,f):
        self.nom = nom
        self.codi = codi
        self.grups = []
        self.facu = f
    def afegeixGrup(self,grup):
        for x in range(0,len(self.grups)):
            if self.grups[x].esIgual(grup):
                self.grups[x].num = str(self.grups[x].num) + '/' +str(grup.num)
                return 0
        grup.assig = self
        grup.facu = self.facu
        self.grups.append(grup)

    # def llistaGrups():
    #     gr = []
    #     for g in grups
    # def buscaGrup(self, idg):
    #     for g in grups:
    #         if g.num == idg:
    #             return g
    #     print("ERROR: grup",idg,"no trobat a",self.nom)
    #     return -1
