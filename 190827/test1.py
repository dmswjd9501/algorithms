import sys
sys.stdin = open('input_test1.txt', 'r')

tc = int(input())

for t in range(1, tc+1):
    # 행, 열, 페인트 칠하는 횟수
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(K)]
    data = [[0]*M for _ in range(N)]
    # print(data)

    for i in range(K):
        x1, y1, x2, y2, color = arr[i][0], arr[i][1], arr[i][2], arr[i][3], arr[i][4]
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if color >= data[x][y] and color in range(11) and 0 <= x1 <= N-1 and 0 <= y1 <= M-1:
                    data[x][y] = color
    # print(data)
    cnt = {}

    for row in range(N):
        for column in range(M):
            if data[row][column] not in cnt:
                cnt[data[row][column]] = 1
            elif data[row][column] in cnt:
                cnt[data[row][column]] += 1
    # print(cnt)
    print('#{} {}'.format(t, max(cnt.values())))


