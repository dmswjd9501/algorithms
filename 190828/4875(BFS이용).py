import sys
sys.stdin = open('input_4875.txt', 'r')

def BFS(r, c, n):
    Q = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    visit = [[False] * n for _ in range(n)]
    visit[r][c] = True
    Q.append([r, c])
    while Q:
        r, c = map(int, Q.pop(0))
        for i in range(4):
            if r+dy[i] < 0 or r+dy[i] > n-1 or c+dx[i] < 0 or c + dx[i] > n-1:
                continue
            elif maze[r+dy[i]][c+dx[i]] == '3':
                return 1
            elif visit[r+dy[i]][c+dx[i]] == False and maze[r+dy[i]][c+dx[i]] == '0':
                visit[r+dy[i]][c+dx[i]] = True
                Q.append([r+dy[i], c+dx[i]])

    return 0

tc = int(input())
for t in range(1, tc+1):
    N = int(input())
    maze = [input() for _ in range(N)]
    # print(maze)
    for i in range(N):
        if '2' in maze[i]:
            column = maze[i].find('2')
            row = i
    result = BFS(row, column, N)

    print('#{} {}'.format(t, result))