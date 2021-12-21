"Input"

"Input used as a pause"

input()

"You can assign a value to an input"

s = input()
print(s)

"If is necessary to put some indications, they can be placed inside the argument"

s2 = input("Indicate the ammount of gold: ")
print("Gold:",s2)

"If you want to restrict the type of data that will be given"

s3 = int(input("Please put a number here: "))
print(s3)

"If you want to put more than one data"

s4 = input("Put your name, age and gender separated by comas: ").split(',')
print(s4)

"Using for cicles"

s5= [x for x in input("Enter the name of your friends separated by spaces: ").split()]
for x in s5:
    print(x,end=" ")
