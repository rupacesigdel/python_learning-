class Employee:
    company = "Apple"
    def show(self):
        print(f"the name is {self.name} and company is {self.company}")
    
    @classmethod 
    def changeCompany(cls, newCompany):
        cls.company = newCompany

    
e1 = Employee()
e1.name = "harry"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)





# Class Methos as Alternative Construction
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))


e = Employee("Harry", 12000)
print(e.name)
print(e.salary)

string = "John-12000"
e1 = Employee.fromstr(string)
print(e1.name)
print(e1.salary)
