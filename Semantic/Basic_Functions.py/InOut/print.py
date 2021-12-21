'''
Show in console the given input
Example:
'''
soldiers = 2.5
names = 'Unkown'
print(soldiers, names)

'''
There is a way to make the function print() to output multiple times the same thing  """
'''
s7 = """Don't waste your time on me
you are already the voice inside my head
"""
print(s7*2)
"""
"Placeholders %"

"%i for integrer"
"%s for string"
"%f for floating"
"""
name2 = "Jamal"
height2 = 99.9
print("His name is %s, and his height is %f cm"%(name2,height2))

"When it is necessary to specify the large of the precision"
name3 = "Eric"
height3 = 39.12
print("His name is %s, and his height is %.2f cm"%(name3,height3))

"Formats {}"

name4 = "Yumino"
height4 = 129.459
print("His name is {0}, and his height is {1}".format(name4, height4))
"By default, they will print in numeric order"