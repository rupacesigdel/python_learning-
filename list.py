classes= ["L.K.G",1, 2, 3, 4, 5, "rupesh", True, False] # string,boolean...etc allow in list.
print(classes)
print(type(classes))
print(len(classes))
print(classes[0])
print(classes[1])
print(classes[-2]) # count down from right side or back by using - sign.
#called negative index
print(classes[-5])
print(classes[len(classes)-7])   # it print(length of list - given numer = to be printed),here: 9-7=2;so in list 2=2.
# called positive index ...used it to best then negative index.
# can add and remove in list
print(classes[:]) #index start with 0 and end at len(classes)
print(classes[1:]) # index start with 1 and end with last
print(classes[-1:]) # here (len(classes)-1) = 9-1 =8 so,list 8 from 0 t0 8;False so False print out.
print(classes[1:-1]) # here from 1 to (len(classes)-1) = 9-1 =8 so,list 8 from 0 t0 8;False so from [1...to... False] print out.
print(classes[2:8:3])  #here from 2 to 8 in the interval of 3 is print out
if 3 in classes:
    print("yes")
else:
    print("no")

# but here we use for string too!
if "t" in "rupesh":
    print("yes")
else:
    print("no")


#list comprehension
list = [i for i in range (10)] # here print list from 0 to 9.
print(list)
list = [i*i for i in range (10)] # here print i squre list from 0 to 9.
print(list)
list = [i*i for i in range (10) if i%2 == 0] # we can make it condition or select of them throuh this if case
print(list)


# List Methods
classes = [10, 2, 4, 5]
print(classes)
# classes.append(somethinh need to be add in list)
classes.append(15)
print(classes)
# classes.sort() use to put in increasing order
classes.sort()
print(classes)
classes.reverse() # in decreasing form
print(classes)
#or,
classes.sort(reverse=True) #it is used to pu in decreasing form .
print(classes)


#  to find index of number use .index(here to be know?) and it show the first occerance only.
print(classes.index(5))
print(classes.count(5)) # to count num of repetative number. here 5 is 1

# for copy
lists = classes.copy()
lists[0] = 0
print(classes)

lists = classes
lists[0] = 0
print(classes)

classes.insert(3,9)
print(classes)


# extend()
# let here 2 list and need to be merged one of another then .extend() is used
l = [100, 200, 300, 400]
m = [500, 600, 700, 800]
l.extend(m)
print(l)
# Or,
k = l + m
print(k)
#  but it is opposit of 1st one.
m.extend(l)
print(m)

