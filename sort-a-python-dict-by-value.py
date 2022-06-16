# How to sort a Python dict by value
# (== get a representation sorted by value)

import operator
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

print(sorted(xs.items(), key=lambda x: x[1]))
# output: [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# Or:

print(sorted(xs.items(), key=operator.itemgetter(1)))
# output: [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
