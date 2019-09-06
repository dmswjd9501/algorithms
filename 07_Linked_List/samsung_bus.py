import sys
sys.stdin = open('samsung_bus.txt', 'r')

def bus_node(ai, bi):
    global G
    for j in range(ai, bi+1):
        G[j] += 1

def how_many(cj):
    global G
    for i in range(len(cj)):
        if i != len(cj)-1:
            print(G[cj[i]], end=' ')
        else:
            print(G[cj[i]], end='')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)] # (Ai, Bi)
    P = int(input())
    Cj = list(int(input()) for _ in range(P))
    G = [0 for _ in range(5001)]

    for i in range(len(arr)):
        Ai, Bi = arr[i][0], arr[i][1]
        bus_node(Ai, Bi)

    print('#{}'.format(t), end=' ')
    how_many(Cj)
    print()