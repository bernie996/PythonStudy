""" Strings """
"""
----------------------------------------------------------------------------------------------------------
Can be declared either with single quotes or double quotes

To use quotes inside another quotes, it is necessary to use
diferent types in each case:

quote: "She said 'You are so funny!'"
"""

d1 = "String first practice"
print(d1)
"""----------------------------------------------------------------------------------------------------------
To create a string that can pass across lines you have to define the variable with triple " or ' , as if it 
were a comment """

d2 = """If you don't stop
to sing latin music at my room
I'll die soon"""
print(d2)
"""
-------------------------------------------------------------------------------------------------------------
String Index

Each character of a string represent a position in the index of the string
Each position is indicated between [], being the first one will have the position 0

string = "stringUser"

So string[0] should be "s"

"""
"""----------------------------------------------------------------------------------------------------------
If you want to print character that is within a string, you have to put the position of the character
between []"""

s3 = "Volcano"
print(s3[5],s3[1])

"""If you want to print a definite part of a string, put the positions of the initial and the final with double point
in between. You had to know that the last character will not be printed.
If you don't specify the start or the end index of the print string, it will print from the start or will print until
it reach the end
----------------------------------------------------------------------------------------------------------
"""
s4 = """Tell me if you want to be with me
Oh oh oh
Tell me if you want to be with me"""
print(s4[0:33])
print(s4[:33])
print(s4[0:])
"""The negative numbers on the slicing of a string is used to delimite spaces that are before the end."""

s5 = "Waiting for the end to come "
print(s5[-8:-1])
"""
----------------------------------------------------------------------------------------------------------
You can also slice a string while doing jump between characters"""

s6 = "The fun that you can not be"
print(s6[0::2])

"""And if you want to reverse..."""
print(s6[::-1])
"""
----------------------------------------------------------------------------------------------------------
"""
