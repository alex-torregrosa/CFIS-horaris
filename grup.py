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

    def esIgual(self, grup2):
        for classe in self.classes:
            gotcha = False
            for cl in grup2.classes:
                if cl.day == classe.day and cl.start == classe.start and cl.end == classe.end:
                    gotcha = True
            if not gotcha:
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
