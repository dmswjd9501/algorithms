import sys
sys.stdin = open('1979.txt', 'r')

T= int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)
    cnt = 0
    for row in range(N):
        for column in range(N):
            if arr[row][column]:  #

    print('#{} {}'.format(t, cnt))
