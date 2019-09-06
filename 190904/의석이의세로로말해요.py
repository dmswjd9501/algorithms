import sys
sys.stdin = open('의석이의세로.txt', 'r')

T = int(input())
for t in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    max = 0

    for i in range(len(arr)):
        max = len(arr[i]) if max < len(arr[i]) else max
    print('#{}'.format(t), end=' ')

    for c in range(max):
        for r in range(5):
            if c >= len(arr[r]):
                continue
            print(arr[r][c], end='')
    print()