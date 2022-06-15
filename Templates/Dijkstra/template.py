from heapq import heappush, heappop

INF = 10**9


def dijkstra(g, n):
    pq = [] #min heap

    start = 1 # define start
    dist = [INF] * (n + 1)
    dist[start] = 0
    heappush(pq, (0, start))

    while len(pq) > 0:
        d, v = heappop(pq)
        if dist[v] < d: # node v is already has optimal distance
            continue
        for w, d in g[v]: # for each neighbor of v check for optimal distance
            if dist[w] > dist[v] + d:
                dist[w] = dist[v] + d
                heappush(pq, (dist[w], w))

    return dist


# driver code

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
for i in range(m):
    u, v, w = map(int, input().split())
    g[u].append((v, w))
    g[v].append((u, w))


print(dijkstra(g, n))
