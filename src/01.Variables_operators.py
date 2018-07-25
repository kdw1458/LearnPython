# The following identifiers are used as reserved words, or keywords of the
# language, and cannot be used as ordinary identifiers.
# False      class      finally    is         return
# None       continue   for        lambda     try
# True       def        from       nonlocal   while
# and        del        global     not        with
# as         elif       if         or         yield
# assert     else       import     pass
# break      except     in         raise

# print
print('Interest Calculator:')
print("%4d" % (4*3), end=' ') # ' ' instead '\n'
print() # '\n'

# input
original_amount = float(input('Principal amount ?'))
inrate = float(input('Rate of Interest ?'))
period = int(input('Duration (no. of years) ?'))

# string
a = "%f" % 1.2 # '1.200000'
b = "-" * 5 # '-----'
a + b # '1.200000-----'

# F-strings (this is supported >= 3.6)
answer = 42
print(f"The answer is {answer}") # The answer is 42
import datetime
d = datetime.date(2004, 9, 8)
f"{d} was a {d:%A}, we started the mailing list back then."
#'2004-09-08 was a Wednesday, we started the mailing list back then.'

# lists
a = [ 1, 2, 3, 'USA', 'MO']
a[0] # 1
a[-1] # 'MO'
a[1:3] # [2, 3]
a[1:8] # [2, 3, 'USA', 'MO']
a[1:-1] # [2, 3, 'USA']
a[0:4:2] # [1, 3]
a[0:5:2] # [1, 3, 'MO']
a[0::2] # [1, 3, 'MO']
1 in a # True
'USA' in a # True
'Korea' in a # False
len(a) # 5
if a:
    print("a is not empty")
else:
    print("a is empty")
b = list(range(1,5)) # [1, 2, 3, 4]

# multiple assignments in a single line
value, year, amount = 0, 1, original_amount

# Tuple unpacking
 data = ("David", "USA", "Python")
name, country, language = data


# Operators

# // operator gives the floor division result
4.0 // 3 # 1.0
4.0 / 3 # 1.3333333333333333

# ** : power
2**3 # 8

# Type conversions
# float(string) -> float value
# int(string) -> integer value
# str(integer) or str(float) -> string representation
a = 8.126768
str(a) # '8.126768'

# for loop, range()
sum = 0.0
for i in range(1, 11):
    sum += 1.0 / i
    print("%2d %6.4f" % (i , sum))

# math package
import math
a = math.sqrt(4)
