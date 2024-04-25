x = 10 #global variable
print (x)

def my_function():
    global x
    x = 4
    y = 5  # local variable
    print (y)
    print (x)

my_function()
print(x)
# print (y) #this will cause an error bcz y is local variable

