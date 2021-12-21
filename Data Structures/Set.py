"Set Type"

""""
-------------------------------------------------------

Syntax:

    my_set = {a,b,c,d,e}

-By function:

    my_set = set(1,2,3,4)
-------------------------------------------------------
-Set type does not allow to create duplicates.
    my_set = {1,2,2,3} #{1,2,3}

-It uses {} and cannot be sliced

-Elements in a set aren't ordered

-It is not possible to access to an item by index

-------------------------------------------------------
Boolean Comprobation

value in my_tuple #boolean(t/f)
-------------------------------------------------------
Methods

-add(value)

    #Add an element to a set. If the element already exist,
    it doesn't change

my_set = (1,2,3,4)
my_set.add(5) #(1,2,3,4,5)

-remove(value)

    #Remove a value from a set. If there isn't any elements
    like the one in the parameter, it returns error
    #If is necessary to avoid errors .discard() can also be used

-copy()

    #Creates a copy of a set

-clear()

    #Removes all the contents of the set
-------------------------------------------------------
Seth Math

Having two set of elements

first_set = {1,2,3,4,5,6}
second_set = {2,4,6,8,10}

-Union: |

The union will result in a set of the common and uncommon elements

union_set = first_set | second_set
    #{1,2,3,4,5,6,8,10}

-Intersection: &

The intersection will result in a set of elements that are in bot sets
at the same time

inter_set = first_set & second_set

-------------------------------------------------------

 """
sett = {10, "friends", 5, "mad", 0 , "deaths", 10}
print(sett)
print(type(sett))

"If you want to add new elements to the set"

sett.update(["enemies", 15])
print(sett)

sett.remove("mad")
print(sett)

"A frozen set is a set which it's elements cannot be uptaded or removed"

frozSett= frozenset(sett)