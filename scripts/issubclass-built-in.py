# You can check for class
# inheritance relationships
# with the "issubclass()" built-in:
class BaseClass:
    pass


class SubClass(BaseClass):
    pass


print(issubclass(SubClass, BaseClass))
# output: True
print(issubclass(SubClass, object))
# output: True
print(issubclass(BaseClass, SubClass))
# output: False
