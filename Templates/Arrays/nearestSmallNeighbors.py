from collections import deque

# the following function finds any small number that is nearest
# to the left of the current number
# Concept - Monotonic Stack


def nearestSmallLeftNeighbors(arr):
    stack = deque()
    result = [-1] * len(arr)
    for i in range(len(arr)):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(i)
    return result


# driver code
arr = [1, 1, 6, 4, 10, 2, 5]
leftNeighbors = nearestSmallLeftNeighbors(arr)
rightNeighbors = [len(arr)-i-1 if i != -1 else -
                  1 for i in nearestSmallLeftNeighbors(arr[::-1])[::-1]]

print(leftNeighbors)
print(rightNeighbors)
