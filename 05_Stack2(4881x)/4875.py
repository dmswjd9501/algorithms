import sys
sys.stdin = open('input_4875.txt', 'r')

def DFS(x, y, n):

    visit[x][y] = True # 방문 체크
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        if x+dy[i] > n-1 or y+dx[i] > n-1 or x+dy[i] < 0 or y+dx[i] < 0: # 배열 밖으로 빠지면
            continue
        elif data[x+dy[i]][y+dx[i]] == 3: # 도착점 3에 도달하게 된다면
            return 1
        elif (visit[x+dy[i]][y+dx[i]] == False) and data[x+dy[i]][y+dx[i]] == 0: # 방문하지 않았고, 그 값이 0이라면
            if DFS(x+dy[i], y+dx[i], n) == 1:
                return 1
    return 0

tc = int(input())
for t in range(1, tc+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    visit = [[False]*N for _ in range(N)]
    # print(data)
    # print(visit)
    for row in range(N):
        for column in range(N):
            if data[row][column] == 2:
                x = row
                y = column
                break
    result = DFS(x, y, N)
    print('#{} {}'.format(t, result))