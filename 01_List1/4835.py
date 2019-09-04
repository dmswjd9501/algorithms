import sys
sys.stdin = open('4835.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 정수갯수와 비교구간
    arr = list(map(int, input().split())) # 들어오는 정수들

    max = sum(arr[:M])
    min = sum(arr[:M])


    if 10 <= N <= 100 and 2 <= M <= N:
        for i in range(0, N-M+1):
            if sum(arr[i:i+M]) > max:
                max = sum(arr[i:i+M])
            elif sum(arr[i:i+M]) < min:
                min = sum(arr[i:i+M])

        result = max - min

        print('#{} {}'.format(tc, result))
