    """
    Functool Modules

    functools.cache(user_function)
        Lightweight unbounded function cache.

    functools.cmp_to_key(func)
        Transform an old=style function to a key function. Used with tools
        that accept key functions (such as sorted(), min(), max(), etc). This
        Function is primarily used as a transition tool for programs being
        converted from Python 2 which supported the use of comparision
        functions.
        Note:
            A comparison function is any callable that accept two arguments, 
            compares them, and returns a negative number for less-than,
            zero for equality, or a positive number for greater-than.
            A key function is a callable that accepts one argument and 
            returns another value to be used as the sort key.
    
    functools.reduce(function, iterable [,initializer])
        Apply function of two arguments cumulatively to the items of
        iterable, from left to right so as reduce the iterable to a single
        value. For example:
        reduce(lambda x,y: x+y, [1,2,3,4,5])
        x is the accumulated value
        y is the update value from the iterable
        If the optional initializer is present, it is placed before the item
        of the iterable in the calculation, 
           """