from collections import deque


class Tree:
    INF = 10**9

    def __init__(self, n):
        self.n = n
        self.t = [[] for _ in range(n+1)]

    def __str__(self):
        return "\n".join([str(i)+" : "+str(self.t[i]) for i in range(1, self.n+1)])

    def __len__(self):
        return self.n

    def getTree(self):
        return self.t

    def addBranch(self, i, j, wt, *args):
        self.t[i].append((j, wt, *args))
        self.t[j].append((i, wt, *args))

    # height of all subtrees rooted at node root
    def setAllHeights(self, root):
        # leaf are given height 1
        height = [1]*(self.n+1)

        def dfs(node, parent):
            for child, *args in self.t[node]:
                if child != parent:
                    dfs(child, node)
                    height[node] = max(height[node], height[child]+1)
        dfs(root, -1)
        self.height = height
        return height

    def getDiameter(self):
        self.setAllHeights(root=1)
        self.diameter = max(self.height)

        def dfs(node, parent):
            firstMax, secondMax = 0, 0
            for child, *args in self.t[node]:
                if child != parent:
                    firstMax, secondMax, t = sorted(
                        [firstMax, secondMax, self.height[child]], reverse=True)
                    dfs(child, node)
            self.diameter = max(self.diameter, firstMax+secondMax)

        dfs(1, -1)
        return self.diameter

    def getDistanceBetween(self, a, b):
        def dfs(node, parent,dis):
            if node == b:
                return dis
            for child, *args in self.t[node]:
                if child != parent:
                    res = dfs(child,node,dis+1)
                    if res != -1:
                        return res
            return -1

        return dfs(a,-1,0)

# Driver Code
tree = Tree(5)
tree.addBranch(1, 2, 1)
tree.addBranch(1, 3, 1)
tree.addBranch(2, 4, 1)
tree.addBranch(2, 5, 1)

print(tree)
print(len(tree))
print(tree.setAllHeights(1))
print(tree.getDiameter())
print(tree.getDistanceBetween(1, 5))
