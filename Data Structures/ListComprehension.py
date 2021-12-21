"""
List Comprehension
-------------------------------------------------------------------------------------------------------------
 Sintax

 [___ for ___ in ___]


Used to manipulate every element of a list, the comprehension itself gives a return value as a list

#The First Space will refere to the action or the return
#The Second Space is the element that will be used to refere each element in the list
#The Third space will refer to the list itself

ex:

new_list = [x.upper() for x in old_list]

true_or_false = [bool(value) for value in list_of_elements]
-------------------------------------------------------------------------------------------------------------
Conditional Logic

There are conditions that can be added to the list comprehension sintax

[___ for ___ in ___ if (condition)]

[___ if (condition) else ___ for ___ in ___]

example: Eliminate all vowels of a phrase


hello = "Good morning USA, I have the feeling that today is gonna be a wonderfull day!"

salute = ''.join(n for n in hello if n not in "aeiou" )

print (salute)
"""


