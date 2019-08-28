# 교재에는 꺼내면서 방문 표시
# 이 코드는 방문하면서 표시할 것

import sys
sys.stdin = open('input_BFS.txt', 'r')

def BFS(s): # s = 시작점
    Q = []
    visit = [False] * (V + 1) # 정점의 개수만큼 1 ~ V 까지
    # 큐 생성, 방문표시 visit 생성
    visit[s] = True
    Q.append(s)
    # 시작점을 방문하고 큐에 삽입
    while Q:
    # 빈큐가 아닐동안
        v = Q.pop(0)
        # 큐에서 하나 꺼내온다. v
        for w in G[v]:
            # v의 방문하지 않은 인접정점을 모두 찾아서
            if not visit[w]:
                # 차례로 방문하고 큐에 삽입
                visit[w] = True
                Q.append(w)

def BFS(s): # s = 시작점
    Q = []
    visit = [False] * (V + 1)
    visit[s] = True
    D[s], P[s] = 0, 1
    Q.append(s)
    while Q:
        v = Q.pop(0)
        for w in G[v]:
            if not visit[w]:
                visit[w] = True
                D[w] = D[v] + 1 # D[] : 최단거리를 저장
                P[w] = v # P[] : 최단경로 트리 ( 1번으로부터 방문했다)
                Q.append(w)


