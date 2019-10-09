
number = int( input("Podaj liczbe (dzielna) :" ) )
check = int( input ("Podaj dzielną :"))

if number % 2 == 0:
    if number == 4:
        print ( "To jest liczba cztery, która jest liczbą parzystą! ")
    else:
        print ( str(number) + " jest liczba parzystą! ")
else:
    print ( str(number) + " jest liczba nieparzystą! ")

res = number % check
if  res == 0:
    print (str(number) + " Dzieli się przez " + str(check) + " bez reszty.")
else:
    print (str(number) + " Dzieli się przez " + str(check) + " z resztą " + str(res) + " .")
