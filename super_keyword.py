# super keyword is used to the parent class, when a class inherits from multiple parents classes want to call from one of the parents class
class ParentClass:
    def parent_method(self):
        print("This is the parent method. ")


class ChildClass(ParentClass):
    def parent_method(self):
        print("Harry")
        super().parent_method()

    def child_method(self):
        print("This is the child method. ")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()
child_object.parent_method()

#  example 2:
class Employee:
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id


class Programmer(Employee):
    def __init__(self, name, id, lang) -> None:
        super().__init__(name, id)
        self.lang = lang

rohan = Employee("rohan das", "420")
harry = Programmer("Harry", "2345", "Python")
print(rohan.name)
print(harry.name)
print(harry.id)
print(harry.lang)