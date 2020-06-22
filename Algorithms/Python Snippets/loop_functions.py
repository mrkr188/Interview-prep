arr = [1,2,3,4]

# map
# function as fitst argument, list as second
x = map(lambda x: x*x, arr)
print(list(x))


# filter
# a&1 is equivalant to a%2 but faster
x = filter(lambda x: x&1, arr)
print(list(x))


# reduce
from functools import reduce
# to get sum of list
print(reduce(lambda x, y: x+y, arr))
# to get max of list
print(reduce(lambda x, y: x if x>y else y, arr))


# using operator
import operator
# get index and value of max element in list
ix, val = max(enumerate(arr), key=operator.itemgetter(1))
print(ix, val)

