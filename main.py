import random
from bag import *
#from items import *

if __name__ == '__main__':

    #seed = random.randint(0,3)

    lista = [{"Name": "PC", "Weight": 20, "Value": 100},
             {"Name": "TV", "Weight": 30, "Value": 140},
             {"Name": "Phone", "Weight": 10, "Value": 70},
             {"Name": "Tablet", "Weight": 15, "Value": 90},
             ]

    smallestWeight = 10

    random.seed(80)

    lista_osobnikow = []


    for i in range(4):
        lista_osobnikow.append(Bag())

        cond = True
        while (cond):
            seed = random.randint(0, 3)
            if lista_osobnikow[i].CanAdd(lista[seed]):
                lista_osobnikow[i].dodaj(lista[seed])

            else:
                for j in lista:
                    if j.get("Weight") == smallestWeight:
                        cond = False

        print("\n")


