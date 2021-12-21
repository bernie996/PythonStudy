"Operators"

"""
The Basic Hierarchy order, like in others languages, is:
(P)arenthesis
(E)xponents
(M)Multiplication
(D)Division
(A)Addition
(S)Substraction
"""

"The operators + and - are used to addition and substraction"
a1,a2,a3 = 10, 25, 5
a4 = a1 + a2 - a3
print(a1, "+", a2, "-", a3, "= ", a4)


"The operators * and / are used to multiplication and division"

b1,b2,b3 = 5, 45, 9
b4 = (b1 * b2) / b3
print("(", b1, "x",b2,")", "/", b3, "=",b4)

"Remember: The result of the division of two integers will be a float"

"The operator % will return the remainder of a division"
c1,c2 = 30,4
c3 = 30 % 4
print("Rest of: ", c1, "%", c2, "=" ,c3)

"There is an operator that can return the power of a given number"
d1,d2 = 5,3
d3 = d1 ** d2
print(d1,"power to", d2, "=" ,d3)

"Also, another operator can be used to calculate integrer divitions "
e1,e2 = 50,7
e3 = 50 // 7
print("Integrer divition of", e1, "/", e2, "=",e3)


