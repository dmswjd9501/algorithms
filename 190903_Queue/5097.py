import sys
sys.stdin = open('5097.txt', 'r')

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(m):
        tmp = arr[0]
        arr = arr[1:] + [tmp]

    print('#{} {}'.format(t, arr[0]))
