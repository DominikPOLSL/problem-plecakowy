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
        #print("Dodano", dic.get("Weight"), "Aktualnie: ",self.current)

    def check(self, used_item: [{}]):
        if self.current > self.max:
            #print("Powyzej wagi")
            return False

        if used_item in self.lista:
            #print("Ten sam item")
            return False

        else: return True
    # def CanAdd(self, dic: {},):
    #
    #     finall = True
    #
    #     if self.current + dic.get("Weight") > self.max:
    #         finall = False
    #
    #
    #     for i in self.lista:
    #         if dic.get("Name") == i.get("Name"):
    #             finall = False
    #
    #     return finall







