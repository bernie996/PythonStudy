"""
Basic Functions
-----------------------------------------------------------------------------------------------------------
print()   Show in console the value of the given argument
"""
mael = 'Solo'
number5 = 5
print(mael) #Solo
print(number5) #5


"""
-----------------------------------------------------------------------------------------------------------
input()   Read the argument given by the user and allow to interpret it as data

It can have a string inside, that will be printed before the system pauses waiting for the input
"""
age = input('How old are you? ')
print('So you are ' + age +' years old.')

'The input can be inserted inside the print argument'
print(input("What is your favorite book? ") + ' is a very rare one.')

"""
-----------------------------------------------------------------------------------------------------------
type()   Return the type of data of the given argument


-----------------------------------------------------------------------------------------------------------

The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.

round(number, digits)

number	(Required). The number to be rounded
digits	(Optional). The number of decimals to use when rounding the number. Default is 0
"""