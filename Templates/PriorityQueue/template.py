from heapq import *

# for custom comparator pass tuples with first value as comparator


class minHeap:
    def __init__(self, heap=[]):
        heapify(heap)
        self.heap = heap

    def __str__(self,):
        return " ".join([str(i) for i in self.heap])

    def isEmpty(self):
        return len(self.heap) == 0

    def push(self, x):
        heappush(self.heap, x)

    def pop(self):
        return heappop(self.heap)

    def peek(self):
        if len(self.heap) > 0:
            return self.heap[0]

    def size(self):
        return len(self.heap)

    def getHeap(self):
        return self.heap

    def flush(self):
        self.heap = []


class maxHeap:
    def __init__(self, heap=[]):
        if len(heap) > 0:
            if isinstance(heap[0], tuple):  # handling array of tuples
                heap = [(-1*i[0], *i[1:]) for i in heap]
            else:  # handling array of int
                heap = [-1*i for i in heap]
        heapify(heap)
        self.heap = heap

    def __str__(self,):
        if len(self.heap) > 0 and isinstance(self.heap, tuple):
            return " ".join([str((-1*i[0], *i[1:])) for i in self.heap])
        return " ".join([str(-1*i) for i in self.heap])

    def isEmpty(self):
        return len(self.heap) == 0

    def push(self, x):
        if isinstance(x, tuple):
            heappush(self.heap, (-1*x[0], x[1:]))
        heappush(self.heap, -1*x)

    def pop(self):
        popped = heappop(self.heap)
        if isinstance(popped, tuple):
            return (-1*popped[0], *popped[1:])
        return -1*popped

    def peek(self):
        if len(self.heap) > 0:
            peeked = self.heap[0]
            if isinstance(peeked, tuple):
                return (-1*peeked[0], *peeked[1:])
            return -1*peeked

    def size(self):
        return len(self.heap)

    def getHeap(self):
        return self.heap

    def flush(self):
        self.heap = []

