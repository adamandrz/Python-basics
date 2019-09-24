number = int(input("Podaj liczbe dodatnią: "))

def fibb(n):
    if n <= 0:
        print("Podaj liczbe dodatnia!")
    elif n == 1:
        print(0)
    elif n == 2:
        print(1)
    else:
        print(fibb(n-1) + fibb(n-2))
        return fibb(n-1) + fi85bb(n-2)

print(fibb(number))
