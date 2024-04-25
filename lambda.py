# # by the simply we do; 
# def double(x):
#     return x*2
# print(double(5))

def here(fx,value):
    return 6 + fx(value)

# but here using lambda; it is use for many equation approch easily in one line only
double = lambda x: x*2
cube = lambda x : x*x*x
avg = lambda x,y: (x+y)/2
avg1 = lambda x,y,z: (x+y+z)/3

print(double(8))
print(cube(8))
print(avg(4,5))
print(avg1(2,3,4))

print(here(cube,2)) # here pass a function using def from above
# OR,
print(here(lambda x : x*x*x, 2))
print(here(lambda x : x*x, 2))


# Map ,Filter and reduce

def cube(x):
    return x*x*x
print(cube(2))

# by simple convert one to another list


l = [1, 2, 3, 4, 5, 3]
# newl = []
# for item in l:
#     newl.append(cube(item))
# print(newl)

# by using map()
# MAP
newl = list(map(lambda x: x*x*x, l)) # if lambda is use then def not need and empty list too.
print(newl)

# FILTER
# filter()
def filter_function(a):
    return a < 4
newnewl = list(filter(filter_function, l))
print(newnewl)
#  here using lambda without using def function.
newnewl = list(filter(lambda x: x % 2 == 0, l))
print(newnewl)


# REDUCE
# reduce()
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8 , 9]

def my_sum(x,y):
    return x + y

sum = reduce(my_sum, numbers)
# using lambda
sum = reduce(lambda x,y: x + y, numbers)
print(sum)
