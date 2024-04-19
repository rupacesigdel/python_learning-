# f-string 
letter = "hey my name is {0} and i am from {1}"
country = "Nepal"
name = "Rupesh"
print(letter.format(name, country))
print(f"hey my name is {name} and i am from {country}")


print(type(f"{2*30}"))


# Docstring /mostly asked in interview .it read from ('''   ''')
# docstring must be just below the def function .
def square(n):
    '''Take in number n, returns the squre of n'''
    print(n**2)
square(5)
print(square.__doc__)


# PEP8 
# if we input in python or cmd python as import this and enter then poem is seen title "the zen of python" ;by 'tim peters'
