"""
Dictionary Comprehension
------------------------------------------------------------

Syntax

{__:__ for __ in __}

#The First and Second space iterates over the values of the dictionary
#The Third Space is the element that will be used to refere each element in the list
#The Fourth space will refer to the dictionary itself

my_dictionary = {
    "key1":a,
    "key2":b,
    "key3":c}

examples:

new_list = {key:value*2 for key,value  in my_dictionary.items()}
    #{"key1":2*a, "key2":2*b, "key3":2*c}

new_list = {num : num**2 for num in [1,2,3,4,5]}
    #{1:1, 2:4, 3:9, 4:16, 5:25}

key = "ABC"
value = "123"
new_list = {key[i]: value[i] for i in range(0,len(key))}
    #{"A":"1", "B":"2", "C":"3"}

new_list2 = [n:new_list.get(n) for n in range(0, len(new_list))]
------------------------------------------------------------
Conditional Logic

num_list = [1,2,3,4]
new_list = {num:("even" if num % 2 == 0 else "odd") for num in num_list}
"""
