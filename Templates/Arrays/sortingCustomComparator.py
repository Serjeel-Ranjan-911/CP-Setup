from functools import cmp_to_key

def compare(A,B):
    if len(A) > len(B):
        return 1
    return -1
    
fruits = ['apple','mango','banana','papaya','kiwi']
fruits.sort(key=cmp_to_key(compare))
print(fruits)