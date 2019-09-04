import sys
sys.stdin = open('input_Contact.txt', 'r')

def BFS(v):
    stack = []
    visit = [False] * (101)
    D = [0]*(101)
    D[v] = 0
    visit[v] = True
    stack.append(v)

    while stack:
        v = stack.pop(0)
        for w in G[v]:
            if visit[w] == False:
                D[w] = D[v] + 1
                visit[w] = True
                stack.append(w)
    tmp = []
    max_value = max(D)
    for i in range(101):
        if D[i] == max_value:
            tmp.append(i)
    return max(tmp)

for t in range(1, 11):
    # 데이터길이, 시작점
    N, s = map(int, input().split())
    arr = list(map(int, input().split()))
    G = [[] for _ in range(101)]
    for i in range(len(arr)):
        if not i % 2:
            G[arr[i]].append(arr[i+1])
    result = BFS(s)

    print('#{} {}'.format(t, result))

