import time

name = input( "Podaj swoje imie : " )
age = input( "Podaj ile masz lat : " )
repeat = input( "Ile razy chcesz zoabczyc ten komunikat? " )
curr_year = time.strftime("%Y")
year_of_100 = int( curr_year ) + 100 - int( age )

print( "Dzisiaj mamy: " + curr_year )
for i in range(0, int( repeat) ):
    print( name + " 100 lat skonczysz w :" + str(year_of_100 ))
    i =+ 1
