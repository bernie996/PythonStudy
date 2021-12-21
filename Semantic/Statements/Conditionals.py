"Conditional"

"""
In Python, all conditional checks resolve to True or False.
Besides False conditional checks, other things that are naturally falsy include: empty objects, empty strings, None, and zero.

"""

"If"

"""
if conditions(booleans):
    statements
 """

"If Else"

"""
if conditions(booleans):
    statements
else:
    statements
 """

"If Elif Else, used on multiple contitions"

"""
if condition1:
    statements
elif condition2:
    statements
elif condition3:
    statements
else:
    statements
 """
 
'Example'
age = int(input("Introduce your age:"))
if age >= 18 and age < 60 :
    print("You are over 18? Wow, that's nice, %i is a good age"%(age))
elif age >= 60 and age <122:
    print("What? You are %i? What a boomer whe have over there..."%(age)) 
elif age < 0 or age >=122:
    print("Am I a joke to you?")
else:
    print("Get out of here you little hairy hands, being %i years old don't make you a person"%(age))