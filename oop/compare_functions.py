"""Compare Functions

Two functions f and g are provided as inputs to checkio.
The first function f is the primary function and the second function g is the backup.
Use your coding skills to return a third function h which returns:
- the same output as f unless f raises an exception or returns None.
- In this case h should return the same output as g.
If both f and g raise exceptions or return None, then h should return None.

As a second output, h should return a status string indicating whether the function values are the same
and if either function erred.
A function errs if it raises an exception or returns a null value (None).

The status string should be set to:
- "same" if f and g return the same output and neither errs,
- "different" if f and g return different outputs and neither errs,
- "f_error" if f errs but not g
- "g_error" if g errs but not f
- "both_error" if both err.

Input: Two functions: f (primary) and g (backup).
Output: A function h which takes arbitrary inputs and returns a two-tuple.

Example:
        f = lambda x,y: x+y
        g = lambda x,y: (x**2 - y**2)/(x-y)
        checkio(f,g)(1,3) == (4,"same")
        checkio(f,g)(1,1.01) == (2.01,"different") # numerical precision difference
        checkio(f,g)(1,1) == (2,"g_error") # g divides by zero

How it is used: This is an exercise in working with functions as first class objects.

Precondition: hasattr(f,'__call__');
hasattr(g,'__call__')
"""
from typing import Callable


# v1
def checkio(f: Callable,
            g: Callable):
    """ exercise in working with functions as first class objects """

    def h(*args, **kwargs):
        """ function returns result depends on results of functions f and g """
        f_result = g_result = f_status = g_status = None
        try:
            f_result = f(*args, **kwargs)
            if f_result is None:
                f_status = 'f_error'
        except:
            f_status = 'f_error'
        try:
            g_result = g(*args, **kwargs)
            if g_result is None:
                g_status = 'g_error'
        except:
            g_status = 'g_error'

        if f_status and g_status:
            return None, "both_error"
        if f_status:
            return g_result, f_status
        if g_status:
            return f_result, g_status
        if f_result == g_result:
            return f_result, 'same'
        return f_result, 'different'

    return h


# v2
def checkio(f: Callable,
            g: Callable):
    """ exercise in working with functions as first class objects """

    def h(*args, **kwargs):
        """ function returns result depends on results of functions f and g """
        try:
            f_result = f(*args, **kwargs)
        except:
            f_result = None

        try:
            g_result = g(*args, **kwargs)
        except:
            g_result = None

        if f_result is not None:
            if f_result == g_result:
                return f_result, 'same'
            if g_result is not None:
                return f_result, 'different'
            return f_result, 'g_error'

        if g_result is not None:
            return g_result, 'f_error'
        return None, 'both_error'

    return h


if __name__ == '__main__':

    def g(x):
        if x > 0:
            return x
        elif x < 0:
            return -x


    c = checkio(lambda x: abs(x), g)
    result = c(0)

    print(result)
    assert result == (0, 'g_error')

    print(checkio(lambda x, y: x + y,
                  lambda x, y: (x ** 2 - y ** 2) / (x - y))(1, 3))
    print(checkio(lambda x, y: x + y,
                  lambda x, y: (x ** 2 - y ** 2) / (x - y))(1, 2))
    print(checkio(lambda x, y: x + y,
                  lambda x, y: (x ** 2 - y ** 2) / (x - y))(1, 1.01))
    print(checkio(lambda x, y: x + y,
                  lambda x, y: (x ** 2 - y ** 2) / (x - y))(1, 1))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(lambda x, y: x + y,
                   lambda x, y: (x ** 2 - y ** 2) / (x - y))(1, 3) == (4, 'same'), "Function: x+y, first"
    assert checkio(lambda x, y: x + y,
                   lambda x, y: (x ** 2 - y ** 2) / (x - y))(1, 2) == (3, 'same'), "Function: x+y, second"
    assert checkio(lambda x, y: x + y,
                   lambda x, y: (x ** 2 - y ** 2) / (x - y))(1, 1.01) == (2.01, 'different'), "x+y, third"
    assert checkio(lambda x, y: x + y,
                   lambda x, y: (x ** 2 - y ** 2) / (x - y))(1, 1) == (2, 'g_error'), "x+y, fourth"

    # Remove odds from list
    f = lambda nums: [x for x in nums if ~x % 2]


    def g(nums):
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                nums.pop(i)
        return nums


    assert checkio(f, g)([2, 4, 6, 8]) == ([2, 4, 6, 8], 'same'), "evens, first"
    assert checkio(f, g)([2, 3, 4, 6, 8]) == ([2, 4, 6, 8], 'g_error'), "evens, second"

    # Fizz Buzz
    assert checkio(lambda n: ("Fizz " * (1 - n % 3) + "Buzz " * (1 - n % 5))[:-1] or str(n),
                   lambda n: ('Fizz' * (n % 3 == 0) + ' ' + 'Buzz' * (n % 5 == 0)).strip()) \
               (6) == ('Fizz', 'same'), "fizz buzz, first"
    assert checkio(lambda n: ("Fizz " * (1 - n % 3) + "Buzz " * (1 - n % 5))[:-1] or str(n),
                   lambda n: ('Fizz' * (n % 3 == 0) + ' ' + 'Buzz' * (n % 5 == 0)).strip()) \
               (30) == ('Fizz Buzz', 'same'), "fizz buzz, second"
    assert checkio(lambda n: ("Fizz " * (1 - n % 3) + "Buzz " * (1 - n % 5))[:-1] or str(n),
                   lambda n: ('Fizz' * (n % 3 == 0) + ' ' + 'Buzz' * (n % 5 == 0)).strip()) \
               (7) == ('7', 'different'), "fizz buzz, third"
