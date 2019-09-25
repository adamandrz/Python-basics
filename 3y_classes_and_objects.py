class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

class Person:
    name2 = "Ziutek"
    def __init__(self, name, age):
        if name == "":
            self.name = "Zenek"
        else:
            self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)
print(p1.name2)
p2 = Person("", 36)
print(p2.name)
print(p2.age)
print(p2.name2)