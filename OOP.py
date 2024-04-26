class Person:
    name = "Rupesh "
    occupation = "Engineering Student "
    networth = 10
    def  info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person() # we can creat infinity number of person .
b = Person()
c = Person()
a.name = "Rajan"
a.occupation = "accountant"

b.name = "Sujan"
b.occupation = "CA"
# print(a.name, a.occupation)
a.info()
b.info()
c.info() # here no input other information so print of class person of above asitis.



# CONSTRUCTORS IN PYTHON
class Person:
    def __init__(self, name, occupation):
        print("hey i am  a person")
        self.name = name
        self.occupation = occupation

    def  info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person("Rajkumar", "developer")
b = Person("Rajan", "CA")
# c = Person(1, 2)
a.info()
b.info()


# DECORATORS IN PYTHON
