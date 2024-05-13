import random
from bag import *

if __name__ == '__main__':

    #Lista dostepnych przedmiotow do spakowania
    lista = [{"Id": 0, "Name": "PC", "Weight": 20, "Value": 100},
             {"Id": 1, "Name": "TV", "Weight": 30, "Value": 140},
             {"Id": 2, "Name": "Phone", "Weight": 10, "Value": 70},
             {"Id": 3, "Name": "Tablet", "Weight": 15, "Value": 90},
             {"Id": 4, "Name": "Mouse", "Weight": 9, "Value": 40},
             {"Id": 5, "Name": "Speaker", "Weight": 8, "Value": 43},
             {"Id": 6, "Name": "Keyboard", "Weight": 12, "Value": 60},
             ]

    #random.seed(80)

    subjects = []

    conditional = True

    for i in range(16):

        bag = Bag()
        unused_weights = []
        #Uzupelnienie dostpenych wag przedmiotow
        for j in lista:
            unused_weights.append(j.get("Weight"))

        #Wypisanie dostepnych wag przedmiotow jeden raz
        if conditional:
            print("\nMozliwe wagi: ",unused_weights,"\n")
            conditional = False

        print("Obiekt numer ", i + 1)

        #Pętla działa do czasu dopóki suma aktualnej wagi plecaka z minimalną dostępną wagą jest nizsza niż maksymalna waga
        while bag.current + min(unused_weights) <= bag.max:
            seed = random.randint(0,len(lista)-1)
            j = 0
            #Pętla działa tylko jeśli wylosowany przedmiot nie znajduje sie już w plecaku, przedmiot jest dostępny w liscie dostępnych wag,
            #oraz dodanie przedmiotu nie spowoduje przekroczenie wagi
            while (lista[seed] not in bag.lista) and (bag.current + lista[seed].get("Weight") < bag.max) and unused_weights not in bag.lista:
                j = lista[seed].get("Weight")
                bag.dodaj(lista[seed])
                unused_weights.remove(lista[seed].get("Weight"))

            #Jeśli nastąpiło dodanie przedmiotu do plecaka, to wyświetli się informacja
            if j != 0:
                print("Dodano: ",j,"kg - Aktualna waga: ", bag.current,"kg", " Aktualna wartosc: ", bag.value)

        #Dodanie obsobnika do listy osobników
        subjects.append(bag)
        print("\n")


