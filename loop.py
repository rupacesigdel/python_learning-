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

i = 0
while True:
    print(i)
    i = i + 1
    if(i%100 == 0):
        break
