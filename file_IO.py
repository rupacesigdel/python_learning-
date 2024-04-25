# Reading a file
f = open('myfile.txt', 'r')
# print(f)
text = f.read()
print(text)
f.close()


# Writiing a file
f = open('myfile.txt', 'a')
f.write('hello, world!')
f.close()

# here need not to be use f.close()
# f = open('myfile.txt', 'a')
with open('myfile.txt', 'a') as  f:
    f.write("hey i am inside with")



# readline() method to read single line from file 
f = open('myfile.txt', 'r')
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Marks of student {i} in math is:{m1*2}")
    print(f"Marks of student {i} in science is:{m2*2}")
    print(f"Marks of student {i} in english is:{m3*2}")
    print(line)


# writeline() method to read single line from file 
f = open('myfile.txt', 'w')
lines = ['line1\n', 'line2\n', 'line3\n']
f.writelines(lines)
f.close
