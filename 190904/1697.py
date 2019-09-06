# 3가지 방법
# 방문표시하면서 목적지에 도착했을때 최단거리
# DFS로 풀면 시간초과
import sys
sys.stdin = open('1697.txt', 'r')
from collections import deque


# 수빈이, 동생
N, K = map(int, input().split())
visit = [False] * 100001

Q = deque()
visit[N] = True
Q.append((N, 0)) # (위치, 시작점에서의 거리)
ans = 0
while len(Q):
    x, t = Q.popleft()
    if x == K: # 도착했을 때
        ans = t
        break
    if x - 1 >= 0 and visit[x - 1] == False:
        Q.append((x-1, t+1))
        visit[x - 1] = True

    if x + 1 <= 100000 and visit[x + 1]] == False:
        Q.append((x+1, t+1))
        visit[x + 1] = True

    if x << 1 <= 100000 and visit[x << 1]] == False:
        Q.append((x << 1, t + 1))
        visit[x << 1] = True

print(ans)
