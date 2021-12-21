"""Tuples have the same function that
 list does but cannot be modified"""
"""
Syntax:

my_tuple = (1,2,3,4)

This is a way to store data that cannot be deleted or changed
--------------------------------------------------------------
Uses:

-Tuples are faster than list

-Makes the code safer to unexpected modifications

-Can be used as keys in dictionaries

-They are the result of certain methods like .items() when they are
    applied to dictionaries

----------------------------------------------------------
Creation

-Using ()

    first_tuples = (1,2,3,4)

 -Tuple function

    second_tuples = tuple(2,4,6,8)
----------------------------------------------------------
Accesing to the elements

my_tuple[i]= #i element of the tuple
    #Like in list, if the i element is negative, it will consider the
    last element as the start

----------------------------------------------------------
Looping

A for looping can iterate over the elements of a tuple

ex:     my_tuple = (1,2,3,4,5)
        for ju in my_tuple:
            action

----------------------------------------------------------
Methods

-count()

    Return the number of times a number apears in a tuple

-index

    Returns the index at which a value is found in a tuple

    my_tuple.index(value) #position of the value
    #if the value is not in the tuple, return an error
----------------------------------------------------------



"""
zeroTuple = ("a","b","c","d","e")
print(zeroTuple)

firstTuple = (10)
secondTuple = (10,)
"The first one will be defined as an int"
print(type(firstTuple))
print(type(secondTuple))
print()
"Simple Functions Associated"

fourthTuple = (2,7,12,17,22,17)
print(fourthTuple)
print(fourthTuple[4])
print(fourthTuple*2)
print(fourthTuple.count(17))
print(fourthTuple.index(22))

"""If you want to transform a list into a tuple """

listA1 = [1,2,3,4,5]
print(type(listA1))
print(listA1)
tupleA1 = tuple(listA1)
print(type(tupleA1))
print(tupleA1)

