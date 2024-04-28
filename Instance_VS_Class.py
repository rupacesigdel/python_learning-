class Employee:
    companyName = "Lenovo"      #class associate property bcz it is same for all.
    noOfEmployees = 0
    def __init__(self, name) -> None:
        self.name = name
        self.raise_amount = 0.02         #instance property bcz can creat different for diff employee
        Employee.noOfEmployees += 1
    def showDetails(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

emp1 = Employee("Rupesh")
emp1.raise_amount = 0.3     #instance property
emp1.companyName = "Apple"
emp1.showDetails()
# Employee.showDetails(emp1)
Employee.companyName = "Google"     #it chane company name for both employee
print(Employee.companyName)

emp2 = Employee("Roshan")
emp2.showDetails()
