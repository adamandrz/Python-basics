number = int(input("Podaj liczbe :"))
divlist = []

i = 1

while (i <= number):
    if number % i == 0:
        divlist.append(i)
    i += 1

print(divlist)
