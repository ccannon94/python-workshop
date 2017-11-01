# coding: utf-8

'''
TODO: 
	1. Create a variable called 'name' that holds a name.
	2. Create an if-else block that prints he name variable if it is in all capital
    letters otherwise, convert it to all capital letters and then print it.

'''

name = "Chris"

if name.isupper():
    print "Already upper"
    print name
else:
    name = name.upper()
    print(name)