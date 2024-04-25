a = 4
b = 4
c = "4"
print(a is b) # it compare exact location of object in memory of given value 
print(a == b) #it compare the value

print(a is c)
print(a == c)

print(a == b is c)
print(a is b is c)
print(a is b == c)
print(a == b == c)


print(a == b is not c)
print(a is b is not c)
print(a is b != c)
print(a == b != c)

# so in list comparision,
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]

print(x == y) #True
print(x is y)  # False

# in string
p = "prabin"
q = "prabin"

print(p == q) #True
print(p is q) #False

# in tuple 
i = (1,2)
j = (1,2)

print(i == j) #True
print(i is j) #False

# AND also,
l = None
m = None

print(l is m) #True
print(l is None) #True
print(l == None or l == m ) #True

