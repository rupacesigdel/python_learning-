# Inheritance
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of the Employee: {self.id} is {self.name}")


class Programmer(Employee):
    def showLanguage(self):
        print("The defult language is python")


e = Employee("Roshan Das", 420)
e.showDetails()
e1 = Employee("rajan stha", 400)
e1.showDetails()
e2 = Programmer("ronik sigdel", 430)
e2.showLanguage()
e3 = Programmer("rejan shah", 415)
e3.showLanguage()


# Access Modifiers,types;
# 1.Public access modifirs

class Employee:
    def __init__(self, age, name):
        self.name = name
        self.age = age

a = Employee(20, "Rupesh")
print(a.name)
print(a.age)


# 2.private access modifirs
class Employee:
    def __init__(self):
      self.__name = "Rupesh"

a = Employee()
# print(a.__name) #cannot be accessed directly
print(a._Employee__name) # can be accessed indirectly
print(a.__dir__())



# 3.Protected access modifirs
class Student:
   def __init__(self):
      self._name = "Rupesh"
    
   def _funName(self):          #protected method
    return " CodeWithHarry"
   
class Subject(Student):             #inherited class
   pass

obj = Student()
obj1 = Subject()

# calling by object of student class
print(obj._name)
print(obj._funName())
# calling by object of subject class
print(obj1._name)
print(obj1._funName())





# single inheritance
# A class inherits properties and behaviors from a single parent class.

class Animal:
   def __init__(self, name, species):
      self.name = name
      self.species = species
   def make_sound(self):
      print("Sound made by Animal")

class Dog(Animal):
   def __init__(self, name, breed):
      Animal.__init__(self, name, species = "Dog")
      self.breed = breed
   def make_sound(self):
      print("Bark!")

d = Dog("dog","doggy")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()

# 