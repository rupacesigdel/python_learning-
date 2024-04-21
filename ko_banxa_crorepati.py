questions = [
    [" How many provence are there Government of Nepal?", 5, 7, 9, 11, 2],
    [" How many zone are there Government of Nepal?", 12, 13, 14, 15, 3],
    [" How many distric are there Government of Nepal?", 76, 77, 78, 75, 2],
    [" How many municipalities are there Government of Nepal?", 373, 383, 283, 273, 3],
    [" How many Sub-metropolitan are there Government of Nepal?", 8, 9, 10, 11, 4],
    [" How many Local Level are there Government of Nepal?", 753, 747, 763, 757, 1],
    [" How many Local Level are there Government of Nepal?", 753, 747, 763, 757, 1],
    [" How many Local Level are there Government of Nepal?", 753, 747, 763, 757, 1],
    [" How many Local Level are there Government of Nepal?", 753, 747, 763, 757, 1],
    [" How many Local Level are there Government of Nepal?", 753, 747, 763, 757, 1],
    [" How many Local Level are there Government of Nepal?", 753, 747, 763, 757, 1],
    [" How many Local Level are there Government of Nepal?", 753, 747, 763, 757, 1],
    [" How many Local Level are there Government of Nepal?", 753, 747, 763, 757, 1],
]
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, "1 Crore"]

for i in range (0,len(questions)):
    question = questions[i]
    print(f"\n\nQuestion is on your screen:\n {questions[i]}")
    print(f"Option for Rs.{levels[i]} :")
    print(f"a. {question[1]}       b.{question[2]}")
    print(f"c.{question[3]}        d.{question[4]}")
    reply = int(input("Enter your answer (1-4) :- "))
    if (reply == question[-1]):
        print(f"Correct answer!!!, you have won Rs. {levels[i]}")
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 13):
            money = 5000000
        else:
            money = 0
    else:
        print("Wrong answer!")
        break

print(f"You have save {money} which can you take home.")