# The "timeit" module lets you measure the execution
# time of small bits of Python code

import timeit
print(timeit.timeit('"-".join(str(n) for n in range(100))',
                    number=10000))

# output: varied time, depends on the machine you are running (e.g: 0.29281292100040446)

print(timeit.timeit('"-".join([str(n) for n in range(100)])',
                    number=10000))

# output: varied time, depends on the machine you are running (e.g: 0.18732479500022237)

print(timeit.timeit('"-".join(map(str, range(100)))',
                    number=10000))

# output: varied time, depends on the machine you are running (e.g: 0.18732479500022237)
