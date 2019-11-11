import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 55]

#pusta lista na wyniki
thesame = []

#petla sprawdzajaca czy emelement listy a zawiera sie w liscie b
for i in a:
  if i in b:
      thesame.append(i)

#wydruk listy wynikowej
print(thesame)

#pusta lista na wyniki
thesame2 = []

#generowanie dlugosci list c i d
range_c = random.randint(1,20)
range_d = random.randint(1,20)

c = []
d = []

#generowanie elementow listy c
for i in range(1,range_c):
    c.append(random.randint(0,10))

#generowanie elementow listy d
for i in range(1,range_d):
    d.append(random.randint(0,10))

#print(c)
#print(d)

#petla sprawdzajaca czy emelement listy c zawiera sie w liscie d
for i in  c:
    if i in d:
        thesame2.append(i)

print(thesame2)
