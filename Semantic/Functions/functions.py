"Functions"

"""
-------------------------------------------------------------------------------------
Group of statements designed to do a particular task

Example:
input()
print()



It has all the code necessary for the user to run a determined action

They can be categorized in two kinds:
    Inbuilt Functions:

    User Defined Functions: Perform a task designed by the user. 

The type of task could be:
    Process Data: processData(data)
    Calculation : calculateSum(a,b)
-------------------------------------------------------------------------------------
-Syntax:

def name_of_function():
    block of runnable code

-Call

A function is called using the name of the function followed by
parenthesis

-Parameter

Is the variable that holds the value of represent the argument given to
the function

-Argument

Is the data that is actually being send to the function

-Return

#Exist the function
#Output whatever value es placed after the return keyword
#Pops the function off of the call sack
-------------------------------------------------------------------------------------

Advantages:
    Reusable: One defined, we can call the function whenever we want
    Modularity: We can use multiple functions to split problems so every function
                will be used to solve a determinated problem
    Maintenance: If a change must be done, it is necesary that we can change
                a single function to solve the problem
To retrieve data from a function we use the command "return"
example:
def sum(a,b):
    tot=a+b
    return tot
result = sum(10,5)


""" 