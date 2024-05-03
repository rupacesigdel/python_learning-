class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self) -> str:
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    # def __add__(self, x):
    #     return f"{self.i + x.i}i + {self.j + x.j}j + {self.k + x.k}k"
    # it return in the form of string so we have to change it to vector form so ,

    def __add__(self, x):
        return Vector(self.i + x.i , self.j + x.j , self.k + x.k)
v1 = Vector(3, 4, 5)
print(v1)

v2 = Vector(7, 8, 9)
print(v2)

# print(v1 + v2) # it's error in python if not use __add__() function.
print(v1 + v2)
print(type(v1 + v2))