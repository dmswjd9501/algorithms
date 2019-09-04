import sys
sys.stdin = open('4828.txt', 'r')
tc = int(input())

for tc in range(1, tc+1):

    N = int(input())
    arr = list(map(int, input().split()))

    result = 0
    min = arr[0]
    max = arr[0]

    for i in range(0, N):
        if 1 <= arr[i] <= 1000000:
            if arr[i] > min:
                max = arr[i]
            else:
                min = arr[i]
        result = max - min

    print('#{} {}'.format(tc, result))