from queue import PriorityQueue
from heapq import heappush, heappop

Q = []
arr= [1, 3, 5, 7, 9, 2, 4, 6, 8, ]


arr = [(3, 2), (2, 5),(1, 8), (0, 9),(2, 1), (3, 4), (2, 1)]

PQ = PriorityQueue()
for val in arr:
    PQ.put(val)

while not PQ.empty():
#     print(PQ.get())
