from collections import defaultdict


class multiset:
    def __init__(self):
        self.multiset = defaultdict(int)

    def add(self, key):
        self.multiset[key] += 1

    def remove(self, key):
        if key in self.multiset:
            self.multiset[key] -= 1
            if self.multiset[key] == 0:
                del self.multiset[key]

    def __contains__(self, val):
        return self.multiset[val] > 0

    def __len__(self):
        return sum(self.multiset.values())

    def __str__(self):
        return "< " + "".join([(str(i)+" ")*self.multiset[i] for i in self.multiset])+">"


# Driver Code
mset = multiset()

mset.add("a")
mset.add("b")
mset.add("c")
mset.add("c")
mset.add("d")

print(mset)
print(len(mset))
print("a" in mset)
print("b" in mset)
print("c" in mset)

mset.remove("c")
print("c" in mset)
mset.remove("c")
print("c" in mset)
