'''
DataTypes

At Python you don't have to specify the type of data when you first describe it.
Simply put the value of the data.

Note Type: Does not contain any value. Example:
    A = ""

name = "Carlos Miralles"

Numeric Types: int, float, complex. Examples:
    Number = 300
    Dot = 3.655

Usefull Tip:

In Python, if you want to describe a large integer number, you can also separate it with underscores:

Number1 = 120584
Number2 = 120_584

print(Number1) #120584
print(Number2) #120584

Sequences: Ordenated characters like
        str(strings)
        byte(sequence or byte)
        bytearray
        list
        tuple
        range

Binary: They are defined with the use of 0B at the start of the binary sequence. Example:
    bin = 0B1010
    This assign to bin the value of 10 and it's adopt the datatype of int.

Hexadecimal: They are defined with the use of 0X at the start of the hexadecimal sequence. Example:
    bin = 0X1010
    This assign to bin the value of 4112 and it's adopt the datatype of int.

Boolean: Are the ones that have assigned True or False as values of their variables
    music = False
    So a command like print(music) will print: False

    Also, you can define statements automatically as true or false 
    print(10<2) will print a False value because it's a false statement

Convertions:
    With Python you can transform numerical types between them.
    example:

    Alc = 31.5
    Blc = int(Alc)
    print(Blc)
    The output will be 31 due to that is the integer part of the first double variable written

    And also can convert decimal numbers into another hexadesimal representations
    example:

    ten = 10
    tenten = bin(ten)
    print(tenten)
    The output will be 0b1010

    *If you want to know the type of data in witch you are working with in a variable you can print the Type of the variable:

    example:
    A = "Blue"
    print (type(A))

    The output should be: <class str'>
'''