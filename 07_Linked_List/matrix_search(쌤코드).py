import sys
sys.stdin = open('matrix_search.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = []
    # 튜플로 행, 열 저장

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                continue
            r, c = i, 0
            while r < N and arr[r][j]:
                c = j
                while c < N and arr[r][c]:
                    arr[r][c] = 0
                    c += 1
                r += 1

            ans.append((r-i, c-j))

    ans.sort(key=lambda a: (a[0]*a[1], a[0])) # a는 ans의 각각 하나의 자료
                                              # 튜플 두 개 곱하면 면적
