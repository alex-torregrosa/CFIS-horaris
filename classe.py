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
