import sys
sys.stdin = open('파리퇴치.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            for x in range(M):
                for y in range(M):
                    sum += matrix[i+x][j+y]
                    result = sum if sum > result else result
    print('#{} {}'.format(t, result))