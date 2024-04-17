#  hey rupesh,plese dont remove this line.
print("hey i am\' a \"good boy\"\nand this viewer is also a good boy/girl")
'''
print("helloword")
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
friend = '''he said
hey siri 
you are my best friend 
"i want to say sth\"'''
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


