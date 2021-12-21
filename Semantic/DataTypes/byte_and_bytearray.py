""""""

"The maximum value of a byte is 255"
list1 = [10,15,16,8,47,50,255]
print(list1)
print(type(list1))
print()

bit1 = bytes(list1)
print(bit1)
print(type(bit1))
"bytes cannot be edited or get elements added "

bitA1 = bytearray(list1)
print(bitA1)
print(type(bitA1))
"bytearrays can be modified or get elements added"

bitA1[2] = 33
print(bitA1)
