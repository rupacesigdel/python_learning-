from operator import index


a= input("Enter the number : ")
print (f"mlultiple table of {a} is : ")

try:
 for i in range (1, 11):
    print(f"{int(a)} x {i} = {int(a)*i}")

# except Exception as e:
#   print(e)
except:
  print("inviled input")

print ("some line of code")
print("end of program")
7

try:
  num = int(input("Enter an integer: "))

except ValueError:
  print("number entered is not integer.")

except IndexError:
  print("inviled error")


# finally clause
try:
  l = [1,2,3,4]
  i = int(input("enter the index:"))
  print(l[i])
except:
  print("some error occerred")

finally:
  print("i am always  excuted")

def func1():
  try:
   l = [1,2,3,4]
   i = int(input("enter the index:"))
   print(l[i])
   return 1
  except:
   print("some error occerred")
   return 0

  finally:
   print("i am always  excuted")

x = func1()
print(x)
