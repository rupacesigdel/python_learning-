import functools
import time

@functools.lru_cache(maxsize=None)
def Fx(n):
    time.sleep(5)
    return n*5

print(Fx(20))
print("Done for 20")
print(Fx(2))
print("Done for 2")
print(Fx(6))
print("Done for 6")

# here the Memoization occur so not take 5 sec for repeatative words.
print(Fx(20))
print("Done for 20")
print(Fx(2))
print("Done for 2")
print(Fx(6))
print("Done for 6")

print(Fx(60))
print("Done for 60")
