"""
Custom Modules

They, just like the built-in modules, can be import
They are import by using the file name

for example:

file1.py: (This is a separated file)

def fn():
    return "do something"
def other_fn():
    return "or not"

file2.py: (This is a separated file)

import file1
file1.fn()          #do something
file1.other_fn()    #or not
"""