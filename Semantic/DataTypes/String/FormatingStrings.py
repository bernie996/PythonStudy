"Formating Strings"

"String Concatenation"

"Used to combine multiple Strings together, using + operator"
"To use concatenation, the variables must be of the same type"

s10= "I'm a"
s11= "Soldier"
s12 = s10 + " " + s11


"""
----------------------------------------------------------------------------------------------------------
Variables Interpolation in Strings

- F-Strings

"""
s13 = 10
inside = f"I've told you {s13} times already"
print(inside)

"""
- .format method
"""
s14 = 5
outside = "She came here {} times".format(10)
print(outside)
