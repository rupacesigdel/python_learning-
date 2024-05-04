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


# Multiple inheritance:
class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
       print(f"The name is {self.name} ")
class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
       print(f"The dance is {self.dance} ")

class DancerEmployee(Employee, Dancer):
    def __init__(self, name, dance):
        self.name = name
        self.dance = dance

o = DancerEmployee("Pratha", "Classical")
print(o.name)
print(o.dance)
o.show()  # it show which has first input then this value is output, like here is Dancer.
print(DancerEmployee.mro())



# Multilevel Inheritance
class Animal:
   def __init__(self, name, species):
      self.name = name
      self.species = species
   def show_detail(self):
      print(f"Name: {self.name}")
      print(f"Species: {self.species}")

class Dog(Animal):
   def __init__(self, name, breed):
      Animal.__init__(self, name, species = "Dog")
      self.breed = breed
   def show_detail(self):
      Animal.show_detail(self)
      print(f"Breed: {self.breed}")

class GoldenRetriever(Dog):
    def __init__(self, name, color):
     Dog.__init__(self, name, breed = "Golden Retriver")
     self.color = color

    def show_detail(self):
        Dog.show_detail(self)
        print(f"Color: {self.color}")

O = GoldenRetriever("tommy", "black")
O.show_detail()


# Hybrid and Hierarchical Inheritance
# Hybrid;

class BaseClass:
    pass

class Derived1(BaseClass):
    pass

class Derived2(BaseClass):
    pass

class Derived3(Derived1, Derived2):
    pass


# Hierarchical Inheritance;

class BaseClass:
    pass

class D1(BaseClass):
    pass

class D2(BaseClass):
    pass

class Dn(D1):     # here in Dn , n = 1,2,3,4......can be made many more like this.
    pass

class Dn(D2):     # here in Dn , n = 1,2,3,4......can be made many more like this.
    pass
