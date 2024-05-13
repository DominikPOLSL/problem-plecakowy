class Bag:

    def __init__(self):
        self.max = 100
        self.current = 0
        self.value = 0
        self.lista = [{}]

    def wypisz(self):
         print(self.lista)

    def dodaj(self, dic: {}):
        self.lista.append(dic)
        self.current += dic.get("Weight")
        self.value += dic.get("Value")








