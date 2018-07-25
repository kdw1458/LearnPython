#!/usr/bin/env python3

# Data Structures

# Lists
a = [1, 2, 3, 4, 4]
a.append(6) # [1, 2, 3, 4, 4, 6]
a.insert(0,-1) # [-1, 1, 2, 3, 4, 4, 6]
a.count(4) # 2
a.remove(3) # [-1, 1, 2, 4, 4, 6]
a.reverse() # [6, 4, 4, 2, 1, -1]
b = [7, 8, 9]
a.append(b) # [6, 4, 4, 2, 1, -1, [7, 8, 9]]
a.extend(b) # [6, 4, 4, 2, 1, -1, [7, 8, 9], 7, 8, 9]
a.remove(b) # [6, 4, 4, 2, 1, -1, 7, 8, 9]
a.sort() # [-1, 1, 2, 4, 4, 6, 7, 8, 9]
del a[0] # [1, 2, 4, 4, 6, 7, 8, 9]
a.pop() # 9 and a = [1, 2, 4, 4, 6, 7, 8]
a.pop(0) # 1 and a = [2, 4, 4, 6, 7, 8]
a.pop(1) # 4 and a = [2, 4, 6, 7, 8]
z = [x + 1 for x in [x ** 2 for x in a]] # [5, 17, 37, 50, 65]

# Tuples
a = 'apple', "banana", 'orage' # ('apple', 'banana', 'orage')
del a[0] # error, tuple does not support del
a[1] # 'banana'
for x in a:
    print(x, end=' ') # apple banana orage

a = (123) # 123
type(a) # <class 'int'>
a = (123, ) # (123,) trailing comma
type(a) # <class 'tuple'>

x, y = divmod(15,2) # x = 7, y = 1

# Sets
a = set("ababa cd") # {' ', 'd', 'b', 'a', 'c'}
b = {'cdceef'} # {'e', 'd', 'f', 'c'}
a - b # {'b', 'a', ' '}
a | b # {' ', 'b', 'd', 'e', 'c', 'f', 'a'} sum
a & b # {'c', 'd'} intersect
a ^ b # {' ', 'b', 'e', 'f', 'a'} exclusive
a.add('e') # {' ', 'd', 'e', 'b', 'a', 'c'}

# Dictionaries
a = {'Daniel':'apple', 'David':'banana', 'Bethany':'orange'}
a['Daniel'] # 'apple'
del a['Bethany'] # {'Daniel':'apple', 'David':'banana'}
a['Sarah'] = 'grape' # {'Daniel':'apple', 'David':'banana', 'Sarah':'grape'}
'Bethany' in a # False
for x, y in a.items():
    print("%s likes %s" %(x, y))
dict((('Sarah', 'David'), ('apple', 'kiwi'))) # {'Sarah':'apple', 'David':'kiwi'}
