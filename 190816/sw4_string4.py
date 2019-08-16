import sys
import pprint
sys.stdin = open('input4.txt', 'r')

for t in range(1, 11):
    N = int(input())
    matrix = [input() for _ in range(8)]

    cnt = 0
    for x in range(8):
        for i in range(8-N+1):
            tmp = matrix[x][i:i+N]
            if tmp == tmp[::-1]:
                cnt += 1

    matrix_2 = list(zip(*matrix))

    count = 0
    for row in range(8):
        for j in range(8-N+1):
            tmp = matrix_2[row][j:j+N]
            if tmp == tmp[::-1]:
                count += 1

    print('#{} {}'.format(t, cnt + count))