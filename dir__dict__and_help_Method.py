# dir()
x = [1, 2, 3, 4]
x1 = (1, 2, 3, 4)
print(dir(x))
print(x.__add__)
print(x1.__add__)

# __dict__
from typing import Self


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1

p = Person("John", 30)
print(p.__dict__)

# help()
print(help(Person))
