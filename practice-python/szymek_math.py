import random

def dodawanie(ile, zakres):
    zadanie = []
    for i in range(1,ile + 1):
        skladnik1 = random.randint(1,zakres)
        skl = zakres - skladnik1
        if skl != 0:
            skladnik2 = random.randint(1,int(skl))
            zadanie.append(str(skladnik1) + " + " + str(skladnik2) + " = ")
        else:
            zadanie.append(str(skladnik1) + " + " + str(skl) + " = ")
    return zadanie

def odejmowanie(ile, zakres):
    zadanie = []
    for i in range(1,ile + 1):
        odjemna = random.randint(1,zakres)
        odjemnik = random.randint(1,odjemna)
        zadanie.append(str(odjemna) + " - " + str(odjemnik) + " = ")
    return zadanie



ile = int(input("Ile zadan wygenerowac :"))
zakres = int(input("Podaj zakres dzialan :"))

fmath = open("dodawanie.txt", "w")

for zad in dodawanie(ile,zakres):
    fmath.write("\n" + zad)

fmath.close()

fmath = open("odejmowanie.txt", "w")

for zad in odejmowanie(ile,zakres):
    fmath.write("\n" + zad)

fmath.close()
