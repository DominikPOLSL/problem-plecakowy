class Bag:

    def __init__(self):
        self.max = 100
        self.current = 0
        self.lista = [{}]

    def wypisz(self):
         print(self.lista)

    def dodaj(self, dic: {}):
        self.lista.append(dic)
        self.current += dic.get("Weight")
        print(self.current)

    def CanAdd(self, dic: {},):

        finall = True

        if self.current + dic.get("Weight") > self.max:
            finall = False


        for i in self.lista:
            if dic.get("Name") == i.get("Name"):
                finall = False

        return finall







