from itertools import *

def allPermutations(lst):
    return list(permutations(lst))

# Driver Code
print(allPermutations([i for i in range(4)]))
