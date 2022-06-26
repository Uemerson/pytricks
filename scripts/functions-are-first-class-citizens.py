# Functions are first-class citizens in Python:

# They can be passed as arguments to other functions,
# returned as values from other functions, and
# assigned to variables and stored in data structures.

def myfunc(a, b):
    return a + b


funcs = [myfunc]
print(funcs[0])
# output: <function myfunc at 0x107012230>
print(funcs[0](2, 3))
# output: 5
