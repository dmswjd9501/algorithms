import sys
sys.stdin = open('5099.txt', 'r')


def BFS(n, m):
    oven = [0] * n
    chk = [0] * n
    cnt = 0

    for i in range(n):
        oven[i] = cheese.pop(0)
        cnt += 1
        chk[i] = cnt

    while oven:
        for i in range(n):
            if oven[i] == 0: continue
            oven[i] = oven[i] // 2

            if oven[i] == 0:
                if cnt < m:
                    oven[i] = cheese.pop(0)
                    cnt += 1
                    chk[i] = cnt
                else:
                    chk[i] = 0

            if chk.count(0) == n - 1:
                for i in chk:
                    if i != 0: return i

T = int(input())

for t in range(1, T + 1):
    # 화덕크기, 피자개수
    n, m = map(int, input().split())
    cheese = list(map(int, input().split()))
    result = BFS(n, m)
    print('#{} {}'.format(t, result))
