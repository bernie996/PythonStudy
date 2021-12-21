"Logical Operators"

"Are used to build logic expressions using boolean values"
"It is case sensitive, so the first letter of True or False mush be Uppercase"
" and : Is used to check if two events ocurr"
a1, a2, a3 = True, True, False
print("True and True : ",a1 and a2,"\n","True and False : ",a1 and a3,"\n","False and True : ",a2 and a3,"\n" )

" or : Is used to check if at least one of the events ocurr "
b1, b2, b3, b4 = True, True, False, False
print("True or True : ",b1 or b2,"\n","True or False : ",b1 or b3,"\n","False or True : ",b2 or b3,"\n", "False or False : ",b3 or b4,"\n")

" not : This operator change the value of a boolean"
c1,c2 = True, False
print("not True : ",not c1,"\n","not False :", not c2,"\n")

"""
Comparision Operators: Using a = 1 and b = 1

Op |	    What it does	                          | Example
-----------------------------------------------------------------------
== |	Truthy if a has the same value as b	          | a == b  # True
!= |	Truthy if a does NOT have the same value as b |	a != b  # False
>  |    Truthy if a is greater than b                 | a > b   # False
<  |	Truthy if a is less than be b                 | a < b   # False
>= |    Truthy if a is greater than or equal to b     | a >= b  # True
<= |	Truthy if a is less than or equal to b        | a <= b  # True

Logical Operators

Op	|   What it does	                                        |Example
----------------------------------------------------------------------------------------------------------------
and |	Truthy if both a AND b are true (logical conjunction)	|if a and b: print(c)
or	|   Truthy if either a OR b are true (logical disjunction)	|if am_tired or is_bedtime: print("go to sleep")
not	|   Truthy if the opposite of a is true (logical negation)	|if not is_weekend: print("go to work")


is vs. "=="

In python, "==" and "is" are very similar comparators, however they are not the same.
"is" is only truthy if the variables reference the same item in memory

==: checks if the values are the same
'is': cheks if both elements have the same space in memory

a = 1
a == 1  # True
a is 1  # True
----------------------------------------------------------------------------------------------------------------
a = [1, 2, 3]  # a list of numbers
b = [1, 2, 3]
a == b  # True
a is b  # False
----------------------------------------------------------------------------------------------------------------
c = b
b is c  # True



"""

