class Math:
    def __init__(self, num):
        self.num = num 
    
    def addtonum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a , b):
        return a + b
    
a1 = Math(5)
print(a1.num)
a1.addtonum(6)
print(a1.num)


print(a1.add(7,8))
# Or
print(Math.add(7,8))