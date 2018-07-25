# line split
s = "This is \
line split"
print(s) # This is line split

s = "This is \n line split in two lines"
print(s)
# This is
#  line split in two lines

s = """This is a
multiline string"""
print(s)
# This is a
# multiline string

# etc
s = "I am " "David " "Park" # I am David Park
len(s) # 15
s[::-1] # 'kraP divaD ma I'

# String related methods
s = "i am david park"
s.title() # I Am David Park
s.upper() # I AM DAVID PARK
s.lower() # i am david park
s.title().swapcase() # i aM dAVID pARK
s.isalnum() # False # Is it alpha numeric? (false beacuse of the space)
s = "IamDavidPark123"
s.isalnum() # True
s.isalpha() # False # Is it alphabet?
s = "123"
s.isdigit() # True
s = "I Am David"
s.istitle() # True
s.islower() # False # Is all lower case?
s.isupper() # False
s.split(" ") # ['I', 'am', 'David']
len(s.split(" ") # 3 # number of words
"-".join("I am David".split(" ")) # 'I-am=David'

# Strip
s = "    I am David\n"
print(s)
#    I am David
#
print(s.strip()) # remove whitespace and newline
# I am David
s = " abc,.def*^"
s.lstrip(" ba,d.") # "c,.def*^" # strip every single charecter from the left until it does not match
s.rstrip("f^d*") # " abc,.de"

# Find
s = "Have a nice day"
s.find("nice") # 7
s.startwith("Have") # True
s.startwith("day") # False
s.upper().startswith("NICE", 7, 11) # True
s.endwith("day") # True
 
# String is iterable
for ch in "David"
    print(ch)
# D
# a
# v
# i
# d
