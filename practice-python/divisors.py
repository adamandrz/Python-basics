number = int(input("Podaj liczbe :"))
divlist = []
divlist2 = []

i = 1

while (i <= number):
    if number % i == 0:
        divlist.append(i)
    i += 1

print(divlist)

listRange = list(range(1,number + 1))

for i in listRange:
    if number % i == 0:
        divlist2.append(i)

print(divlist2)
