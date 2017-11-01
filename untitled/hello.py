# Use string format with a single variable
name = 'Chris'
print "Hello {}".format(name)

# Define example function
def sum(arg1, arg2):
    return arg1 + arg2

# Use example function
print sum(2,3)

# Use function with other variable types
print sum("Hello", "world")

# Returns the class of an object
print type(name)

# Returns all available options or inheritances for an object?
print dir(name)

# Gives documentation for a given type
print help(str)

# Converts all characters of a string to uppercase
print name.upper()

# Convert a string to an int
# int(strHere)

# In Python, EVERYTHING is an object
# Variables are simply pointers to objects

boolTest = True
if boolTest:
    print "something is true"
else:
    print "nah"
