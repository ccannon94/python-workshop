# Create an empty list
items = []
items.append('Eggs')
items.append('Bacon')
items.append('Grits')

print items[1]

myName = []
myName.append('Christopher')
myName.append('Charles')
myName.append('Cannon')

print myName

# So that's weird, this is apparently a circular linked list
print myName[-1]

# One line instantiation
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print len(letters)

if 'Bob' in myName:
    print "This is Bob!"
if 'Christopher' in myName:
    print "This is Chris!"

# Create a list of Apple Products
appleProducts = ['MacBook Pro', 'iPad Pro', 'iPad 2', 'Apple Watch', 'iPhone 8 Plus', 'Apple TV 4th Generation', 'Apple TV 3rd Generation' 'Mac Mini', 'iPhone 6', 'iPhone 5c']

if len(appleProducts) > 5:
    print "You spent too much!"

# Prints all the way to the end
print appleProducts[0:]

# Prints index 0 through 3 (b/c it's exclusive at the end
print appleProducts[:4]

# Funny, it adds a nice space in the middle
print "Monty", "Python"

# Format is a nifty thing
print "My name is {} and I am {} years old".format("Chris", str(23))

decades = [2010, 2000, 1990, 1980, 1970, 1960, 1950, 1940]

# Foreach
for year in decades:
    if year == 1970:
        #Let's just skip the 70's...
        continue
    print "Hey it's the " + str(year) + "'s!"

# open a file to write!
myfile = open('output.txt', 'w')

text = 'I am using the write method to write to this output file! Yippeeee!'

myfile.write(text)

myfile.close()

# open the same file for reading!
myfile2 = open('output.txt', 'r')
contents = myfile2.read()
myfile2.close()
print contents

# open the file to append something to it!

myfile3 = open('output.txt', 'a')
myfile3.write('\nNow I\'m adding new things!')
myfile3.close()

# iterate through the file
for line in open('output.txt', 'r'):
    print line