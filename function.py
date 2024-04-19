# function defination;
def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
        print(a, "is greater than", b)
    else:
        print(b, "is greater than ", a)
def isLesser(a,b):
    if(a<b):
        print(a, "is lesser than", b)
    else:
        print(b, "is lesser than ", a)

a = 5
b = 8
if(a>b):
    print('first letter is greater')
else:
    print ("second letter is greater")
# gmean = (a*b)/(a+b)
# print(gmean)
calculateGmean(a,b)
c = 9
d =3
isGreater(c,d)
# gmean1 = (c*d)/(c+d)
# print(gmean1)
calculateGmean(c,d)

#  pass is used to pass ta program lest back for example 
if(a>b):
    pass        #if we not use pass then it create error but pass not showing and continue..

# defult argument

def average(a=9, b=1):
    print("the average is ", ((a+b)/2))

average(4,6)
average(5)
average(b=9)


def name(fname, mname="prasad", lname ="sigdel"):
    print("hello,", fname, mname, lname)

name("Rajan", "Ganesh")


def average(a, b, c=1):
    print("The average value is ", (a+b+c)/2)

average(5,6)  #here c will take from defult value c=1 if not input other.

# variable length argument

def name(*name):
    print('hello,', name[0], name[1], name[2])

name("rupesh", 'rajan', "rajesh")


def average(*numbers):
    sum = 0
    print(type(average))
    for i in numbers:
        sum = sum+i
    print("Average is : ", sum / len(numbers))

average(4,5,6)


# Arbitrary Argument
def name(**name): 
    print(type(name))   #type is dictionary
    print("hello,", name["fname"], name["mname"], name["lname"])

name(fname = "Hari", mname ="kumar", lname ="shrestha")


#Return Function
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    # return 7 #if we call return 7 even there is another output then it will show 7 in output
    return sum/ len(numbers) # if return is not given then it gives None in output
c = average(4,5,6,7)
print(c)
# if we have a 2 return statement then it will gives first one only.


