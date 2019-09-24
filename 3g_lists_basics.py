#lista - nawiasy kwadratowe, elementy trzymaja kolejnosc, sa zmienne
friends = ["Seba", "Andrzej", "Marek", "Zbigniew"]

#tuple - nawias okragly, elementy trzymaja kolejnosc, sa nie zmienne
friends2 = ("Seba", "Andrzej", "Marek", "Zbigniew")

print(friends)

print(friends[0])
print(friends[2])
print(friends[-1])
print(friends[0:])
print(friends[1:])
print(friends[2:4]) #wyswietla od 3 do konca
friends[1] = "Milosz"
print(friends)