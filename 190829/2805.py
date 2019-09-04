import sys
sys.stdin = open('2805.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input()) # 농장의 크기
    arr = [list(map(int, input()))for _ in range(N)]
    # print(arr)
    m = N >> 1
    sum = 0
    for r in range(N):
        for c in range(N):
            if r < m: # 작을때
                for i in range(N-2*(m-r)):
                    sum += arr[r][m-i]
            elif r == m:
                sum += arr[r][c]
            else: # 클때
                for j in range(m):
                    sum += arr[r][]

    print('#{} {}'.format(t, sum))
