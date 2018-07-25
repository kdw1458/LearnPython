import os
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

# print
print('Interest Calculator:')

# input
original_amount = float(input('Principal amount ?'))
inrate = float(input('Rate of Interest ?'))
period = int(input('Duration (no. of years) ?'))

# multiple assignments in a single line
value, year, amount = 0, 1, original_amount

# Tuple unpacking
 data = ("David", "USA", "Python")
name, country, language = data

# while
while year <= period
    value = amount + (inrate*amount)
    print("Year %d Rs. %.2f" % (year, value))
    amount = value
    year = year + 1
interest = value - original_amount
print('\nInterest = %0.2f' %interest)
