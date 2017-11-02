# coding: utf-8

'''
TODO: 
	1. Create a variable called 'name' that holds a name.
	2. Create an if-else block that prints he name variable if it is in all capital
    letters otherwise, convert it to all capital letters and then print it.

'''

name = "Chris"

#Print name if it is all uppercase, or else capitalized each letter and then print string
if name.isupper():
    print name
else:
    name = name.upper()
    print(name)

# Explicit casting
age = "21"
intAge = int(age)

# Ints will not explicity cast when concatenated with Strings
myAge = 23
print "I am " + str(myAge) + " years old"