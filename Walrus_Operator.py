# foods = list()
# while True:
#     food = input("what food do you like?: ")
#     if food  == "quit":
#         break
#     foods.append(food)

#  here using walrus 
foods = list()
while ( food := input("what food do you like?: ")) != "quit":
    foods.append(food)
    