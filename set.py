# for non repetative list need to be creat then set is use in case of list
s = {2, 4, 2, 6}
print(s)
# here set only took {2, 3, 6} not 2 , two times .

info = {"carla", 19, False, 5.9, 19} # output is in different order which dont has fixed 
print(info)

# rupesh = {} # its same as dict bracs. so it print empty dict.
# we have to creat empty set by following method
rupesh = set()
print(type(rupesh))

for value in info:
    print(value)


# Union,Intersection,complement

s1 = {1, 2, 3, 4, 5, 6, 7, 8}
s2 = {2, 3, 5, 7}
print(s1.union(s2)) # getting new set by union two set 
s1.update(s2) # put all s2 value in set s1 . but s2 remain same
print(s1,s2)

print(s1.intersection(s2)) #getting common from both set s1 and s2.
print(s1.intersection_update(s2)) #getting common from both set and remain value is lost.

# # symmetric different (A delta B) = (A union B) - (A intersection B) 
print(s1.symmetric_difference(s2))

# # difference and difference_update
print(s1.difference(s2))
print(s1.difference_update(s2))

# isdisjoint,issuperset,issubset,
print(s1.isdisjoint(s2))
print(s1.issubset(s2))
print(s1.issuperset(s2))

# add(),remove()/discard,pop(),del()
s1.add(20)
print(s1)

s1.remove(5)
print(s1)


s1.discard(5)
print(s1)


s3 = s1.pop()
print(s1)
print(s3)

del s1
print(s1)

s2.clear()
print(s2)

# check if item exists
if 2 in s1:
    print("2 is present")
else:
    print("2 is absent")