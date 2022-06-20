# "is" vs "=="

a = [1, 2, 3]
b = a

print(a is b)
# output: True
print(a == b)
# output: True

c = list(a)

print(a == c)
# output: True
print(a is c)
# output: False

# • "is" expressions evaluate to True if two
#   variables point to the same object

# • "==" evaluates to True if the objects
#   referred to by the variables are equal
