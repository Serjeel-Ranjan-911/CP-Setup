from bisect import *

# using binary search on sorted arrays

# find index of an element
def bsearch(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return -1

# find index of largest element smaller than given value
def upper_bound_strict(a, x):
    i = bisect_left(a, x)
    if i:
        return i-1
    return -1

# find index of largest element smaller than (OR) equal to given value
def upper_bound(a, x):
    i = bisect_right(a, x)
    if i:
        return i-1
    return -1


# find index of smallest element greater than given value
def lower_bound_strict(a, x):
    i = bisect_right(a, x)
    if i != len(a):
        return i
    return -1

# find index of smallest element greater than (OR) equal to given value
def lower_bound(a, x):
    i = bisect_left(a, x)
    if i != len(a):
        return i
    return -1
