import sys
sys.stdin = open('5102.txt', 'r')

def DFS(s, g):
    Q = []
    visit = [False] * (V+1)
    visit[s] = True
    D[s] = 0
    Q.append(s)
    while Q:
        v = Q.pop(0)
        for w in graph[v]:
            if not visit[w]: # 방문하지 않았다면
                visit[w] = True
                D[w] = D[v] + 1 # 최단 거리 추가
                if w == g:
                    return D[w]
                else:
                    Q.append(w)
    return 0

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    # print(arr)
    graph = [[] for _ in range(V+1)]
    D = [0] * (V+1)

    for i in range(E):
        graph[arr[i][0]].append(arr[i][1])
        graph[arr[i][1]].append(arr[i][0])

    S, G = map(int, input().split())

    result = DFS(S, G)
    print('#{} {}'.format(t, result))
