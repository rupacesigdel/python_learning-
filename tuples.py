tup = (1, 2,3, "green", True)
print(type(tup), tup)
# tup[0]  = 4 is getting error because it is no a list.
# but we can see like 
print(tup[0])
print(tup[2])

if 3 in tup:
    print("yes 3 is present in thin tuple")

tup2 = tup[1:4]
print(tup2)

# Hence tuple and list are same but tuple index can't change where as list can.
# if we have to change index of tuple ,firts we have to change tuple into list.

lst =list(tup)
lst.append("don")
lst.pop(1)
lst[2] = "Blue"
tup = tuple(lst)
print(tup)

roll_no = (6,7, 8, 9, 10)
classes = (1, 2, 3, 4, 5)
here = roll_no + classes
print(here, "\n",here.count(1),"\n", here.index(5), "\n", len(here))
