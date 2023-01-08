# Pythonic ways of checking if all
# items in a list are equal:

lst = ["a", "a", "a"]

print(len(set(lst)) == 1)
# output: True

print(all(x == lst[0] for x in lst))
# output: True

print(lst.count(lst[0]) == len(lst))
# output: True

# I ordered those from "most Pythonic" to "least Pythonic"
# and  "least efficient" to "most efficient".
# The len(set()) solution is idiomatic, but constructing
# a set is less efficient memory and speed-wise.
