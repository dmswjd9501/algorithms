import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

for test_case

Q = deque()

for i in range(1, V+1):
    if in_degree[i] == 0:
        Q.append(i)

ans = []
while len(Q) > 0:
    v = Q.pop()
    ans.append(v)
    for w in G[v]: