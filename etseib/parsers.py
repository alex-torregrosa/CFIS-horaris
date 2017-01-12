from html.parser import HTMLParser
class parserLlista(HTMLParser):
    def __init__(self):
        super(parserLlista, self).__init__()
        self.currentcode = ""
        self.status = 0;
        self.llista = []
    def handle_starttag(self, tag, attrs):
        if tag == "input":
            if attrs[0][1] == "checkbox":
                self.currentcode = attrs[1][1]
                self.status = 1;
        elif tag == "th":
            if self.status > 0:
                self.status += 1
    def handle_data(self, data):
        if self.status == 3:
            self.llista.append((data,self.currentcode))
            self.status = 0

class parserHoraris(HTMLParser):
    def __init__(self):
        super(parserHoraris, self).__init__()
        self.status = 0;
        # 0-> Inicial (buscant taula2)
        # 1-> A taula2 (buscant th w90)
        # 2-> A una franja horaria, buscant TD's
        # 3 -> A un TD (franja 1h), espera a buscar </table> x sortir
        #        si esta a 3 i troba td -> TENIM HORA!!!

        self.dia = -1
        self.franja = -1
        self.cal = [[False for x in range(0,5)] for y in range(0,28)]
        self.full = -1

    def handle_starttag(self, tag, attrs):
        if self.status == 0:
            if tag == "table":
                self.status = 1
        elif self.status == 1:
            if tag == "th":
                good = False
                for at in attrs:
                    if at[0]=="width":
                        if at[1] == "90":
                            self.franja += 1
                            # print("Franja",self.franja)
                            self.status = 2
                            self.dia = -1
        elif self.status == 2:
            if tag == "td":
                self.dia += 1
                # print("Dia",self.dia)
                self.status = 3

        elif self.status == 3:
            if tag == "td":
                # print("Classe: dia",self.dia,"franja",self.franja)
                if(self.full == 1):
                    self.cal[self.franja*2][self.dia] = True
                    self.cal[(self.franja*2)+1][self.dia] = True
                else:
                    self.cal[self.franja][self.dia] = True

    def handle_endtag(self, tag):
        if self.status == 3:
            if tag == "table":
                self.status = 2
                if self.dia == 4:
                    self.status = 1

    def handle_data(self,data):
        if self.full == -1 and self.status == 2:
            if data.find("3") == -1:
                self.full = 1
            else:
                self.full = 0
