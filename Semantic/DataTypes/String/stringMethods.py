"""
String Methods
----------------------------------------------------------------------------------------------------------
capitalize()	Converts the first and only the first character into upper case

"""
indie = "hello momma"
indieLength = indie.capitalize()
print(indieLength) #Hello momma
"""
----------------------------------------------------------------------------------------------------------
casefold()	Converts all elementens of a string into lower case

"""
indie2 = "hELLo mOmmA"
indieLength2 = indie.casefold()
print(indieLength2) #hello momma
"""
----------------------------------------------------------------------------------------------------------
center()	Returns a centered string

string.center(length, character)
"""
indie3 = "hELLo mOmmA"
indieLength3 = indie.center(30,'0')
print(indieLength3) #000000000hello momma0000000000#
"""
----------------------------------------------------------------------------------------------------------
count()	Returns the number of times a specified value appears in the string.

string.count(value, start, end)

value	Required. A String. The string to value to search for
start	Optional. An Integer. The position to start the search. Default is 0
end	Optional. An Integer. The position to end the search. Default is the end of the string

"""
indie4 = 'Blue as the Blue dark Sky'
indieLength4 = indie4.count('Blue')
print(indieLength4) #2

"""
----------------------------------------------------------------------------------------------------------
endswith()	Returns true if the string ends with the specified value

string.endswith(value, start, end)
"""
indie5 = 'I thought i had 10, but I only have 5'
indieLength5 = indie5.endswith('5')
print(indieLength5)  #True
"""
----------------------------------------------------------------------------------------------------------
encode()	    Returns an encoded version of the string
expandtabs()	Sets the tab size of the string
find()	        Searches the string for a specified value and returns the position of where it was found
format()	    Formats specified values in a string
format_map()	Formats specified values in a string
index()	        Searches the string for a specified value and returns the position of where it was found
isalnum()	    Returns True if all characters in the string are alphanumeric
isalpha()   	Returns True if all characters in the string are in the alphabet
isdecimal() 	Returns True if all characters in the string are decimals
isdigit()   	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()   	Returns True if all characters in the string are lower case
isnumeric()	    Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	    Returns True if all characters in the string are whitespaces
istitle()	    Returns True if the string follows the rules of a title
isupper()	    Returns True if all characters in the string are upper case
join()	        Joins the elements of an iterable to the end of the string
ljust()	        Returns a left justified version of the string
lower()	        Converts a string into lower case
lstrip()	    Returns a left trim version of the string
maketrans()	    Returns a translation table to be used in translations
partition()	    Returns a tuple where the string is parted into three parts
replace()	    Returns a string where a specified value is replaced with a specified value
rfind()	        Searches the string for a specified value and returns the last position of where it was found
rindex()	    Searches the string for a specified value and returns the last position of where it was found
rjust()	        Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	    Splits the string at the specified separator, and returns a list
rstrip()	    Returns a right trim version of the string
split()	        Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	        Returns a trimmed version of the string
swapcase()	    Swaps cases, lower case becomes upper case and vice versa
title()	        Converts the first character of each word to upper case
translate()	    Returns a translated string
upper()	        Converts a string into upper case
zfill()	        Fills the string with a specified number of 0 values at the beginning
"""
