import random, math


def je_v_mejah(x, y, xmax, ymax):
    return x >= 0 and y >= 0 and x < xmax and y < ymax


def preveri_okoli(xne, yne, x, y):
    for i in range (yne - 1, yne + 2):
        for j in range(xne - 1, xne + 2):
            if (y == i and x == j):
                return True

    return False


class Polje:
    def __init__(self):
        self.odkrito = False
        self.zastavica = False
        self.mina = False
        self.stevilka = 0


class Igra:
    def __init__(self, velikostx, velikosty):
        self.tabela = []
        self.velikostx = velikostx
        self.velikosty = velikosty
        self.prvic = True
        self.id = -1
        self.tabela_rekurzija = []
        self.stevilo_min = math.ceil(0.225 * self.velikostx * self.velikosty - 11)
        self.konec = False


        for y in range(velikosty):
            self.tabela.append([])

            for x in range(velikostx):
                self.tabela[y].append(Polje())

    
    def konec_igre(self):
        for y in range(self.velikosty):
            for x in range(self.velikostx):
                if self.tabela[y][x].mina:
                    self.tabela[y][x].odkrito = True
        self.konec = True

    def zmaga(self):
        for y in range(self.velikosty):
            for x in range(self.velikostx):
                if not self.tabela[y][x].mina and not self.tabela[y][x].odkrito:
                    return False
        return True

            


    def generiraj_mine(self, xne, yne):
        ze_generirane_mine = []

        for i in range(self.stevilo_min):
            x = random.randint(0, self.velikostx - 1)
            y = random.randint(0, self.velikosty - 1)

            while ((x, y) in ze_generirane_mine) or preveri_okoli(xne, yne, x, y):
                x = random.randint(0, self.velikostx - 1)
                y = random.randint(0, self.velikosty - 1)

            self.tabela[y][x].mina = True
            ze_generirane_mine.append((x, y))


    def prestej_mine(self, x, y):
        stevec = 0
        for i in range (y - 1, y + 2):
            for j in range(x - 1, x + 2):
                if not(y == i and x == j) and je_v_mejah(j, i,self.velikostx, self.velikosty):
                    if self.tabela[i][j].mina:
                        stevec += 1
        return stevec

                    
    def razkrij(self, x, y):
        self.tabela[y][x].odkrito = True
        steviloklik = self.prestej_mine(x, y)
        self.tabela[y][x].stevilka = steviloklik
       
        if steviloklik == 0:
            for i in range (y - 1, y + 2):
                for j in range(x - 1, x + 2):
                    if not(y == i and x == j) and je_v_mejah(j, i,self.velikostx, self.velikosty):
                        if not self.tabela_rekurzija[i][j]:
                            self.tabela_rekurzija[i][j] = True
                            self.tabela[i][j].odkrito = True
                        
                            stevilo = self.prestej_mine(j, i)
                    
                            if stevilo > 0:
                                self.tabela[i][j].stevilka = stevilo
                            elif stevilo == 0 and not self.tabela[i][j].mina:
                                self.razkrij(j, i)


    def klik(self, x, y):
        if not self.konec:
            for i in range(self.velikosty):
                self.tabela_rekurzija.append([])

                for j in range(self.velikostx):
                    self.tabela_rekurzija[i].append(False)

            if self.prvic:
                self.prvic = False
                self.generiraj_mine(x, y)
                self.razkrij(x, y)
            elif self.tabela[y][x].mina:
                self.konec_igre()
            else:
                self.razkrij(x, y)

            if self.zmaga():
                self.konec_igre()
    

class Minolovec:

    def __init__(self):
        self.igre = {}
        return


    def prost_id_igre(self):
        if not self.igre:
            return 0
        else:
            for i in range(len(self.igre) + 1):
                if i not in self.igre.keys():
                    return i 


    def nova_igra(self, velikost):
        nov_id = self.prost_id_igre()
        igra = 0

        if velikost == 1:
           igra = Igra(10, 10)
        elif velikost == 2:
            igra = Igra(20, 16)
        elif velikost == 3:
            igra = Igra(35, 20)

        igra.id = nov_id
        self.igre[nov_id] = igra

        return nov_id
    
