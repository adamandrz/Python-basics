a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

number = int(input("Podaj liczbe: "))


for i in a:
    if i < number:
        b.append( i )

print( a )
print( b )
