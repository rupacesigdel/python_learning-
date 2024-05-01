class employee:
    name = "harry"
    def __len__(self):
        i = 0
        for c in self.name:
            i =  i + 1
            return i

e = employee()
print(e.name)
print(len(e))


# __str__ use:

class Employee:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i =  i + 1
            return i
    
    def __str__(self):
        return f"The name of the employee is {self.name} str"
    def __repr__(self):
        return f"The name of the employee is ('{self.name}') repr"

    def __call__(self):
        print("Hey i am a good boy")


e = Employee("Harry")
print(str(e))
print(repr(e))

e()
