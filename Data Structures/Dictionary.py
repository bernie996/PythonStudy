"Dictionary"

"""
Data Structure to store key value pairs Key-Value
    Keys are used to represent the data, normally Strings or Numbers
    Values are used to represent the data, can be Anything
"""
example_dictionary = {
    "name" : "Mage",
    "profession" : "Wizard",
    "age" : 224,
    "mortality" : True
}

"""
------------------------------------------------------------------------
A Dictionary can also be created by using the function dict()

syntax:        new_dictionary = dict(key = "value")
#If there is more than one element, they must be separated by coma


------------------------------------------------------------------------
Accessing Data
------------------------------------------------------------------------

-Single Element

Using the same format as a dictionary, giving the Key element, the return will be the value stored in it

my_dictionary["key"] #value
    #If a key that isn't in the dictionary, it will return error
    #If key2 = key, it will obtain the same return as the key

my_dictionary["new_key"] = new_value
    #If the key is not defined, it creates a new key in the dictionary
    #If the key already exist and has a value, it overwrites that value
------------------------------------------------------------------------

-Multiple Elements

*Getting Values
    my_dictionary.values()
        #The method.values() will only referr to the "value" elements of the list

*Getting Keys
    my_dictionary.keys()
        #The method.keys() will only referr to the "keys" elements of the list

*Getting Keys and Values
    my_dictionary.items()
        #The return would be an iterable tuple of paired keys-value elements

    iteration: both elements must be given
        for key, value in my_dictionary.items():
            statement
------------------------------------------------------------------------
Ussing "in"

-Looking for a specified key in a dictionary
    "key" in my_dictionary #Boolean(T/F)

-Looking for a specified value in a dictionary
    "value" in my_dictionary.values() #Boolean(T/F)

------------------------------------------------------------------------
Dictionary Methods

- clear() #Delete all elements in the dictionary
    my_dictionary.clear()

- copy() #Make a copy of all the elements in the list
    new_dictionary = my_dictionary.copy()
        #The new dictionary will have the same elements as the fist
        one (==) but will not be the sane (is)

- {}.fromkeys(["key_or_keys"],"value_or_values") / .fromkeys(["key_or_keys"],"value_or_values")
    #Creates key-value pairs from comma separated values:
        {}.fromkeys(["a"],"b") #{"a","b"}
    #It also allows to iterate the values given
        {}.fromkeys(["data1","data2", "data2"],"Zero")
            #The returning dictionary will be a three paired key-value
            elements with all the values equal to "zero"

- get("key_stored") #value_stored
    #Return a key in an object
    #Return None instead of a Keyerror if the key doesn't exist

- pop("key_stored") #value_stored
    #Takes a single argument corresponding to a key and removes
    that key-value from the dictionary.
    #Return the value that the removed key held
    #If a key that doesn't belong to the dictionary is pop, return an error

- popitem() #rand_value_stored
    #Removes a random key in a dictionary

- update()
    #Update keys and values in a dictionary with another set of
    key-value pairs
    second_dictionary.update(first_dictionary)
        #Take all the elements of the first_dictionary and put them into the
        second one
        #If there is an element in the same key, their value it's overwrote
------------------------------------------------------------------------
"""
inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD

stock_list = inventory.copy()
print(stock_list)
# add the value 18 to stock_list under the key "cookie"
stock_list.update({"cookie" : 18})
stock_list.pop("cake")


