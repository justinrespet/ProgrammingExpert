"""
Integer Sum

Write a function named integer_sum that accepts any number of positional arguments,
which are assumed to be integers. This function should return the sum of all these
integers.

To handle invalid input (arguments that are not integers) you must write the
following decorators and use them to describe the integer_sum function.

- flatten_lists: this decorator should flatten any list arguments for the decorated
function by extracting their elements and passing them as individual arguments 
instead of the list. For example, if [1, 2, True] is an argument, then 1, 2, and True 
should be extracted and passed as arguments instead of the list to the decorated 
function.

- convert_strings_to_ints: this decorator should convert any string arguments that are
valid integers to integers and pass them to the decorated function. Any string that is 
not a valid integer should be removed as an argument to the decorated function.

- filter_integers: this decorator should remove any argument that is not an integer and
call the decorated function with only integer arguments

You may assume all arguments passed to integer_sum will be of type float, int, str,
or list
"""

# sample data
test1 = ('1', '2', -0.9, 4, [5, 'hi', '3'])
test2 = (2, 3, 4, -2, '2', ['1', '2', 3], 2.3)
test3 = ()
test4 = ('2.3', 'true', [1, 'hello', 4])


# flatten lists decorator
# - This is going to involve the splat operator, but I'm not certain how exactly so
# I'm going to play around with it
# - Could I aggregate all inputs into a list, and then send an unpacked version of
# that to the function?
# - from the instructions, I can assume that I will receive no iterable other than a list,
# and that I will not receive nested lists
def flatten_lists(func):
    def wrapper(*args):
        returnList = []

        for item in args:
            if isinstance(item, list):
                for i in item:
                    returnList.append(i)
            else:
                returnList.append(item)

        return func(*returnList)
    return wrapper


# - as of being in integer_sum, my data will be 'flat' if they are individual elements
# inside a tuple, as *args creates a tuple of any
@flatten_lists
def integer_sum(*args):
    return args


print("***")
print(integer_sum(*data3))
print("***")
