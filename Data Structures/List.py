"""List and Function Associated"""

"""
--------------------------------------------------------
To create a list just simply create a 
ordenate sequence of elements that you want to get
in there

list1= [10, 8.75, "String", bool(True)]
print(list1)

print(list1[1]) 
#It will print the first element

print(list1[2:4]) 
#It will print from second to fourth element

print(list1*2) 
#It will print the list twice
--------------------------------------------------------
Applicable Functions

-list(group_of_elements): 
#Creates a list contining the referenced elements
    example: list(range(a,b))

-len(element): 
#It will return print the size of the list
    print(len(list1)) 

-Delete
    del(list2[1], list2[3])
    print(list2)
#Remove elements from the list by position

-Check if a Value is in a list
value_in_list in created_list #Boolean

--------------------------------------------------------
Methods
--------------------------------------------------------
Add Elements

-append
    list2.append(60)
    print(list2)
#Add one and only one given element to the list

-extend
    list2.extend([110,120])
    print(list2)
#Add all elements given to the list

-insert
    list5 = [100,200,300,400,500]
    list5.insert(0, 50)
    print(list5)
    print()
#Insert a value in a designed position
--------------------------------------------------------
Remove Elements

-remove:
    list2.remove(10)
    print(list2)
#Remove a designed element from the list

-clear:
    list3 = [1,2,3,4,5]
    list3.clear()
    print(list3)
#Delete all elements from a list

-pop:
    list3 = [1, 2, 3, 4, 5]
    extracted = list3.pop(1) #2
#Remove and return the element in the given position.
#If there is no position, it uses the last element by default

--------------------------------------------------------
Other Usefull Methods


-sort
    list6.sort()
    print(list6)
#Put elements of a list in order

-index
    list7.index(a)
#Return the position of a given element of a list
#If there is more than one of the elements that are being asked
only the first one will be returned
    lst.index(a,b,c)
#given three elements, the first one will represent the element that is
being consulted for
#The second one will be the position from where the list
is going to start looking for, while the last one is the end position in the
list where the search will be done

-count
    lst.count(a)
#return the number of times the element "a" is in the list

-reverse
    lst2 = lst1.reverse()
#Return a list of the elements of the file in inverse order

-join
    message = ["Mamma", "I've just kill a man", "Put a gun against his head", "And I triggered now hes dead"]
    ",".join(message)
#String method usually used to convert list in strings
-------------------------------------------------------------------------------------------------------------
Swaping Values

my_list[1], my_list[2] = my_list[2], my_list[1]

-------------------------------------------------------------------------------------------------------------
Slicing

Makes new list using one of them

    some_list[start:end:space]
#The start element "some_list[start:]" shall always have the colons, even if is just one
#The start element can be a negative, getting the element from inverse order in straight order
#The start and end element will represent given positions
#The end element "some_list[:end]" is exclusive, so it doesn't include the last element
#The step element count number every "step" numbers
#The step element, in negative numbers, reverse the order or the elements

examples:
    some_list[1,2,3,4,5,6]
    other_list = some_list[:2] #[1,2]
    other_list = some_list[4:]  #[5,6]
    other_list = some_list[3:4] #[4]
    other_list = some_list[-2:] #[5,6]
    other_list = some_list[:-2] #[1,2,3,4]
    other_list = some_list[2:-1] #[3,4,5]
    other_list = some_list[::2] #[1,3,5]
    other_list = some_list[1::2] #[2,4,6]
    other_list = some_list[:4:3] #[1,4]
    other_list = some_list[::-1] #[6,5,4,3,2,1]
    other_list = some_list[1::-1] #[2,1]
    other_list = some_list[:1:-2] #[6,4]
-------------------------------------------------------------------------------------------------------------
Nested Lists



"""
