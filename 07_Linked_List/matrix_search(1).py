import sys
sys.stdin = open('matrix_search.txt', 'r')

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # print(arr)
    col = [0] * (n+1)

    for i in range(n):
        row = 0
        for j in range(n):
            if arr[j][i] != 0:
                row += 1

            elif arr[j][i] == 0 and row != 0:
                col[row] += 1
                row = 0
        if row != 0:
            col[row] += 1

    result = []

    for i in range(n):
        if col[i] != 0:
            result.append([i, i * col[i]])

    result_sort = sorted(result, key=lambda x: x[1])
    print('#{} {}'.format(t, len(result_sort)), end=' ')

    for value in result_sort:
        print(value[0], value[1] // value[0], sep=' ', end=' ')
    print()