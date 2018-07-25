#!/usr/bin/env python3

# If-else , the control flow

number = int(input("Enter a number: "))
if number < 100:
    print("The number is less than 100")
elif number == 100:
    print("The number is 100")
else:
    print("The number is greater than 100")

# Truth value testing
if x:
    pass
# Don't do this
if x == True:
    pass


# while

# Fibonacci series (1 1 2 3 5 8 13 21 ...)
a, b = 0, 1
while b < 100:
    print(b)
    a, b = b, a + b

# Power series (e**x = 1 + x + x**2/2! + …. + x**n/n! where 0 < x < 1)
x = float(input("Enter the value of x: "))
n = term = num = 1
sum = 1.0
while not n > 100:
    term *= x / n
    sum += term
    n += 1
    if term < 0.0001:
        break
    elif n%10:
        continue # this will take the execution back to the starting of the Loop
    print("n = %s" % n)
print("No of Times= %d and Sum= %f" % (n, sum))

# For Loop
a = [1, 2, 3, 4, 5]
for x in a[::2]:
     print(x) # 1 3 5
for x in range(1,7,2):
    print(x) # 1 3 5
else:
    print("Bye")
