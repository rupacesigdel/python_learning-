import time

def using_While():
    i = 0
    while i<500:
        i = i + 1
        print(i)

def using_for():
    for i in range(500):
        print(i)


init = time.time()
using_for()
t1 = time.time() - init

init = time.time()
using_While()
t2 = time.time() - init

print(t1)
print(t2)

# example2:
print(4)
time.sleep(4)
print("this is printed after 3 seconds")

# for formatted of time show
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)