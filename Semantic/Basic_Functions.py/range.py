"""
Ranges come altogether with loops

They can be represented in various ways:

(n): n elements from 0 to n-1
(1,n): will take elements from 1 to n-1
(1,n,a): Take elements from 1 to n-1 with a step of "a" elements, skiping "a" everytime


"""
ra1 = range(5)
"It goes from zero to the integrer value"

for i in ra1:
    print(i)
print()

"If the range is not going to start at zero"

ra2 = range(5, 9)
for i in ra2:
    print(i)
print()

"When you are going to define the skips in the values that the cicles have"

ra3 = range(0,45,5)
for i in ra3:
    print(i)