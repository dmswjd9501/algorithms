import sys
sys.stdin = open('input_4871.txt', 'r')

def DFS(v, G):
    stack = []
    stack.append(v)
    visit[v] = True

    for w in graph[v]:
        if w == G:
            return 1
        if visit[w] == False:
            if DFS(w, G) == 1:
                return 1
    return 0

tc = int(input())
for t in range(1, tc+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visit = [False] * (V+1)
    for _ in range(E):
        depart, arrive = map(int, input().split())
        graph[depart].append(arrive)
    # print(graph)
    S, G = map(int, input().split())
    result = DFS(S, G)

    print('#{} {}'.format(t, result))