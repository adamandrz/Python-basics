a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

value = int(input("Podaj wartosc < 100 :"))
for x in a:
    if x <= value:
        b.append(x)

print(b)
