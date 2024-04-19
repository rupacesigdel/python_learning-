'''{#  hey rupesh,plese dont remove this line.
print("hey i am\' a \"good boy\"\nand this viewer is also a good boy/girl")
'''
# print("helloword")
'''
print("hey", 6, 7,sep="~", end="009\n")
print("rupesh")

a=122444545873653264
print(a)
b="rupesh"
print(b)

print("types", type(a))
print("types", type(b))

#dictionnary

dict1 ={"name":"rupesh","age":20,"canvote":True}
print(dict1)


#list

integrates = ["egges", "flour", "sugar", "salt"]
print(integrates[0:2])

letters = ["A", "B", "C","D", "E"]
print(letters[4:])
print(letters[1:])
print(letters[-2:])
print(letters[2:4])
print(letters[:2])
print(letters[3:0])


#operators 
print(15+12)
print(15-7)
print(15/6)
print(15*7)
print(2**5)

# ex
n =  20
m =  7
ans1 =n+m 
print("Addition of ",n, "and" ,m,"is",ans1)
ans2 = n-m 
print("subtraction of ",n, "and",m, "is", ans2)
ans3 = n*m
print("Multiplication of ",n, "and",m, "is", ans3)
ans4 = n/m
print("Division of ",n, "and",m, "is", ans4)
ans5 = n%m
print("Modulus of ",n, "and",m, "is", ans5)
ans6 = n//m
print("Floor division of ",n,"and",m, "is", ans6)


# TypeCasting
# a = "1"
# b = "2"
# print(a + b)

a = 1
b = 2
print(a + b)

# basic typecasting :- string to integer
a = "1"
b = "2"
print(int(a) + int(b))

# implicit TypeCasting
c = 1.9
d = 8
print(c + d)


# User input function
a = input()
print (a) #or
print("my name is :", a)

#  eg.
b = input("Enter first number: ")
c = input("Enter second number: ")
print(b + c)
# variable = int(input(b))
# variable = int(input(c))
print(int(b) + int(c))
# if we use int(c) = rupesh error occer in python so 
# variable = int(input()) or,
# variable = flot(input())


# string making
name = "rupak"
friend = "prabin"
another_friend = "rajan"
apple = "he said,\"i wamt to eat an apple\""
print("hello! ", name ," ,", apple)
# print character,
print(name[0])
print(name[1])
print(name[2])
print(name[3])
# but for apple string we need to use for loop like ,
print("Lets use for loop\n")
for character in apple:
    print(character)
print(len(apple))
# or,
friend = """he said
hey siri 
you are my best friend 
"i want to say sth\""""
print("hello! ", friend)


# string slicing
name = "Rupesh,Sigdel"
print(len(name))
print(name[0:5]) # here 0 is startig from and 5 is end point or range up to there
print(name[:5])
print(name[-5:-2]) # first -5 from last and remove 2 then remain is ans.
print(name[5:0])
print(name[0:-1]) # here the -1 act ; len(name)-1 = 13-1=12, so from 0 to 12 letter print.
print(name[0:-2])
print(name[10:-2])
print(name[0:5:1]) # here 1 is interval of letter from one to another here is print each and every.
print(name[::5]) #here 5 is interval of letter which escape from start point with another 5th letter.
print(name[::-5]) #here 5 is interval of letter which escape from end point with another -5th letter in backward.
print(name[:5:-2])


# string method
a = "Rupesh!!! !!! !!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!")) # remove ! sign or (" ") letter
print(a.split(" ")) #make a list in the form of this:- [" "," "," "]
print(a.replace("Rupesh","John"))

blogHeading = "introduction To Python"
print(blogHeading.capitalize()) # making starting capital and other small automatic

str1 = "Welcome to python and python world!!!"
print(len(str1)) # print num of words use iin it.
print(str1.center(50)) # print 50 space infront of text.
print(str1.count("python")) # count the repetative word and show in number
print(str1.endswith("!!!")) # sentence is end with given letter or not ,if yes 'True' else 'false'.
print(str1.endswith("."))
print(str1.endswith("to", 4,10)) # it show from starting of 'welcome to' has 10 and after 4 'ome to' string end with to or not? yes so 'True' output

str2 = "rupak's name is nature. he is an honest man."
print(str2.find("is")) # find the letter position in string
print(str2.index("is")) # find the position if and only if appear in string.
# print(str2.index("ishh")) #getting error bcz not getting ishh.


str3 = "MyNameIsRupeshSigdel2"
print(str3.isalnum()) # to find the alpha numeric or not? string only consist of A-Z,a-z,0-9 ; else false.
print(str3.isalpha()) # # to find the alphabetic or not? string only consist of A-Z,a-z ; else false.

print(str3.islower()) # if the given string has all small letter then true oterwise false.


str4 = " Happy Bijhaya Dashami all of you\n" # is all of string inside " " are visuable or not? here (backslash n)\n is invisuable so false. 
print(str4.isprintable())


str5 = "     "    # using space by spacebar
print(str5.isspace())
str6 = "    "     # using space by tap
print(str6.isspace())


str7 = "World Health Organization"
print(str7.istitle())   # it show the every first letter of word is capital or not ,if yes True else False.

str8 = "Every country has their National flag"
print(str8.istitle())
print(str8.startswith("Every"))
print(str8.swapcase())  # lower case change to upper and vice versa. like a into A ....
print(str8.title())



#LOOP 
# else if
a = int(input("Enter your age:"))
print("your age is :", a)
# print(a>18)
# print(a=18)
# print(a<18)
# print(a!=18)

if (a > 18):
    print("you can drive")
else:
    print("you can't drive")


num = int (input("Enter the value of num: "))
if (num < 0):
    print("Number is negative")
elif(num == 0):
    print("Number is zero")
elif(num == 99):
    print("Number is special")
else:
    print("Number is positive")

print("I am happy now")


# Nested if
num = int (input("Enter the value of num: "))
if (num < 0):
    print("Number is negative")
elif(num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif(num > 10 and num <= 20):
        print("Number is between 11 - 20")
    else:
        print("Number is greater tan 20")
else:
    print("number is zero")



#Time greeting example by self :-
import time

from pandas import Timestamp


time = int(input("Enter time:"))
if (24> time > 20):
    print("Goog Night")
elif (time < 17):
    if (time >= 12):
        print("Good Afternoon")
    elif(time > 5):
        print("Good Morning")
    else:
        print("Good night")
else:
    print("inviled")


#  BY code with  harry;-
import time 
Timestamp = time.strftime("%H:%M:%S")
print(Timestamp)
Timestamp = time.strftime("%H")
print(Timestamp)
timestamp = time.strftime("%M")
print(timestamp)
timestamp = time.strftime("%S")
print(timestamp)


#matchcase
x = int(input("Enter the value: "))
# x is veriable to match
match x:
    # if x is 0
    case 0 :
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 ==  0:
        print("x % 2 == 0 and case is 4")
    # empty case with if condition
    case _ if x < 10:
        print("x is < 10")
    # defult case (will only be mached if the above case were not matched)
    # so it is basically just an else:
    case _:
        print(x)


# Loop 
# for loops
name = 'Rupesh'
for i in name:
    print(i)
    if (i == "p"):
        print("This is something specisl!")

colors = ["red", "green", "blue", "yellow"]
# for x in colors:
#     print(x)
#     if(x == "blue"):
#         print("its blue color")
for color in colors:
    print(color)
for i in color:
    print(i)


# for k in range (5):
#     print(k+1)
for k in range (1,12,3):
    print(k)
# for k in range (1,2000):
#     print(k)



# while loops
i = int(input("enter the value: "))
while(i <= 30):
    i = int(input("enter the value:"))
    print(i)

print("done with the loop")

# break and continous
for i in range(12):
    print("5 X", i+1, "=", 5 * (1+i))
    if(i == 10):
        break
print("if case is out from loop ")


for i in range(12):
    if(i == 10):
        print("skip the iteration")
        continue
    print("5 X", i, "=", 5 * (i))

}'''

i = 0
while True:
    print(i)
    i = i + 1
    if(i%100 == 0):
        break


# do-while loop ; do{};while