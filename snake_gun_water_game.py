import random
game = ['snake', 'gun', 'water']
computer = c = 0
command = p = 0
run = True
while run:
    computer_choice = random.choice(game)
    # print(computer_choice) # to vew computer input option only.
    command = input("snake, gun, water or quite: ")
    if command == computer_choice :
        print("it's tie.")
    elif(command == "snake"):
        if computer_choice == "gun":
            print("computer won !")
            c += 1
        else:
            print("you won !!!")
            p += 1
    elif(command == "gun"):
        if computer_choice == "water":
            print("computer won !")
            c += 1
        else:
            print("you won !!!")
            p += 1
    elif(command == "water"):
        if computer_choice == "snake":
            print("computer won !")
            c += 1
        else:
            print("you won !!!")
            p += 1
    elif command == "quit":
        break
    else:
        print("inviled input:")
