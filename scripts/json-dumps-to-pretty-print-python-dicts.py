# The standard string repr for dicts is hard to read:
import json
my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
print(my_mapping)
# output: {'b': 42, 'c': 12648430, 'a': 23}  # 😞

# The "json" module can do a much better job:
print(json.dumps(my_mapping, indent=4, sort_keys=True))
# output: {
#     "a": 23,
#     "b": 42,
#     "c": 12648430
# }

# Note this only works with dicts containing
# primitive types (check out the "pprint" module):
json.dumps({all: 'yup'})
# output: TypeError: keys must be a string
