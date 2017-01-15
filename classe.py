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

class Classe:
    """docstring for Classe."""
    def __init__(self, start, end, day):
        self.start = start
        self.end = end
        self.day = day
        # print(day,start,end)

    def esCompatible(self,classe2):
        if classe2.day != self.day:
            return True
        if classe2.start > self.start:
            if self.end > classe2.start:
                return False
            else:
                return True
        else:
            if self.start < classe2.end:
                return False
            else:
                return True



if __name__ == '__main__':
    # Codi de prova de comparacions
    c1= Classe(10,13,0)
    c2= Classe(11,16,0)
    print(c1.esCompatible(c2))
    print(c2.esCompatible(c1))
