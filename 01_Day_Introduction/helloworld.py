import math

# Introduction
# Day 1 - 30DaysOfPython Challenge

print(2 + 3)   # addition(+)
print(3 - 1)   # subtraction(-)
print(2 * 3)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%)
print(3 // 2)  # Floor division operator(//)

# Checking data types

print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Asabeneh'))          # String
print(type([1, 2, 3]))           # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

# Exercise: Level 2
'''Create a folder named day_1 inside 30DaysOfPython folder. 
Inside day_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4. 
Remember to use print() when you are working on a python file. 
Navigate to the directory where you have saved your file, and run it.'''

# Question 1 - Check python version:  3.8.8

# Question 2
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 % 4)
print(3 / 4)
print(3 ** 4)
print(3 // 4)

# Question 3
print('John')
print('Doe')
print('Countryland')
print('I\'m enjoying 30 days of Python')

# Question 4
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Your name'))
print(type('Your family name'))
print(type('Your country'))

# Exercise: Level 3
'''
1. Write an example for different Python data types such as:
Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
2. Find an Euclidian distance between (2, 3) and (10, 8)
'''

print('\n')
print(99)
print(9.9)
print(9 + 9j)
print('String')
print(True)
print('List: ',['ListElement_00','ListElement_01','ListElement_02'])
print('Tuple: ', ('TupleElement_00','TupleElement_01','TupleElement_02'))
print('Set:', {'SetElement_00','SetElement_01','SetElement_02'})
print('Dictionary:', {'DicKey_00':'DicValue_00', 'DicKey_01':'DicValue_01', 'DicKey_02':'DicValue_02'})

# Euclidian distance between (2,3) and (10,8)
print('\n')
print('Euclidian distance between (2,3) and (10,8): ', math.sqrt((((10 - 2)**2 + (8 - 3)**2))))
