# string method
a = "Rupesh!!! !!! !!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!")) # remove ! sign or (" ") letter
print(a.split(" ")) #make a list in the form of this:- [" "," "," "]
print(a.replace("Rupesh","John"))

blogHeading = "introduction To Python"
print(blogHeading.capitalize()) # making starting capital and other small automatic

str1 = "Welcome to python and python world!!!"
print(len(str1)) # print num of words use iin it.
print(str1.center(50)) # print 50 space infront of text.
print(str1.count("python")) # count the repetative word and show in number
print(str1.endswith("!!!")) # sentence is end with given letter or not ,if yes 'True' else 'false'.
print(str1.endswith("."))
print(str1.endswith("to", 4,10)) # it show from starting of 'welcome to' has 10 and after 4 'ome to' string end with to or not? yes so 'True' output

str2 = "rupak's name is nature. he is an honest man."
print(str2.find("is")) # find the letter position in string
print(str2.index("is")) # find the position if and only if appear in string.
# print(str2.index("ishh")) #getting error bcz not getting ishh.


str3 = "MyNameIsRupeshSigdel2"
print(str3.isalnum()) # to find the alpha numeric or not? string only consist of A-Z,a-z,0-9 ; else false.
print(str3.isalpha()) # # to find the alphabetic or not? string only consist of A-Z,a-z ; else false.

print(str3.islower()) # if the given string has all small letter then true oterwise false.


str4 = " Happy Bijhaya Dashami all of you\n" # is all of string inside " " are visuable or not? here (backslash n)\n is invisuable so false. 
print(str4.isprintable())


str5 = "     "    # using space by spacebar
print(str5.isspace())
str6 = "    "     # using space by tap
print(str6.isspace())


str7 = "World Health Organization"
print(str7.istitle())   # it show the every first letter of word is capital or not ,if yes True else False.

str8 = "Every country has their National flag"
print(str8.istitle())
print(str8.startswith("Every"))
print(str8.swapcase())  # lower case change to upper and vice versa. like a into A ....
print(str8.title())
