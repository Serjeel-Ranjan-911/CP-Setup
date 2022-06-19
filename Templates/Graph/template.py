from heapq import *

# 1-based graph
# stored as adjacency list
# edges are stored as array of tuples
# (child node,weight,meta-data...)


class Graph:
    INF = 10**9
    
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n+1)]

    def __str__(self):
        return "\n".join([str(i)+" : "+str(self.g[i]) for i in range(1, self.n+1)])

    def size(self):
        return self.n

    def getGraph(self):
        return self.g

    def addDirectedEdge(self, i, j, wt, *args):
        self.g[i].append((j, wt, *args))

    def addUndirectedEdge(self, i, j, wt, *args):
        self.g[i].append((j, wt, *args))
        self.g[j].append((i, wt, *args))

    def Dijkstra(self, source):
        # assuming graph is weighted
        # and weights are positive

        pq = []  # min heap
        start = source  # define start
        dist = [self.INF] * (self.n + 1)
        dist[start] = 0
        heappush(pq, (0, start))

        while len(pq) > 0:
            d, v = heappop(pq)
            if dist[v] < d:  # node v is already has optimal distance
                continue
            # for each neighbor of v check for optimal distance
            for w, d, *args in self.g[v]:
                if dist[w] > dist[v] + d:
                    dist[w] = dist[v] + d
                    heappush(pq, (dist[w], w))
        return dist

    def FloydWarshall(self):
        # assuming graph size is O(100) or less
        dist = [[self.INF]*(self.n+1) for _ in range(self.n+1)]

        for u in range(1,self.n+1):
            dist[u][u] = 0
            for v,d,*args in self.g[u]:
                dist[u][v] = d
        
        for u in range(1,self.n+1):
            for v in range(1,self.n+1):
                for k in range(1,self.n+1):
                    dist[u][v] = min(dist[u][v] , dist[u][k] + dist[k][v])

        return dist

    def TravellingSalesman(self):
        # assuming graph size is of O(10) or less
        dist = self.FloydWarshall()
        
        memo = [[-1]*(1 << (self.n+1)) for _ in range(self.n+1)]
        def fun(i, mask):
            if mask == ((1 << i) | 3):
                return dist[1][i]

            if memo[i][mask] != -1:
                return memo[i][mask]

            res = 10**9

            for j in range(1, self.n+1):
                if (mask & (1 << j)) != 0 and j != i and j != 1:
                    res = min(res, fun(j, mask & (~(1 << i))) + dist[j][i])
            memo[i][mask] = res 
            return res

        ans = 10**9
        for i in range(1, self.n+1):
            ans = min(ans, fun(i, (1 << (self.n+1))-1) + dist[i][1])
        return ans


# driver code
graph = Graph(5)
print(graph.size())
graph.addUndirectedEdge(1, 2, 10, -4, -5, -3)
graph.addUndirectedEdge(2, 3, 20, -4, -5, -3)
graph.addUndirectedEdge(3, 4, 30, -4, -5, -3)
graph.addUndirectedEdge(4, 1, 40, -4, -5, -3)

print(graph.Dijkstra(1))
print(graph.FloydWarshall())
print(graph.TravellingSalesman())
print(graph)
