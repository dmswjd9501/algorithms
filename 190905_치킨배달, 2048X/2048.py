import sys
sys.stdin = open('2048.txt', 'r')

# 방향으로 1번 이동한 다음에, 또 빈공간이 있을 수 있으니까 1번 더 move

def game(n, direction, board):

    if direction == 'left':
        for r in range(n):
            for c in range(n-2, -1, -1):
                if board[r][c-1] == 0:
                    board[r][c-1] += board[r][c]
                    board[r][c] = 0
                elif board[r][c-1] and board[r][c] and board[r][c-1] == board[r][c]:
                    board[r][c-1] += board[r][c]
                    board[r][c] = 0
                    visit[r][c] = False

    elif direction == 'right':
        for r in range(1, n):
            for c in range(n):
                if board[r-1][c] == 0:
                    board[r-1][c] += board[r][c]
                    board[r][c] = 0
                elif board[r-1][c] and board[r][c] and board[r-1][c] == board[r][c]:
                    board[r][c-1] += board[r][c]
                    board[r][c] = 0
                    visit[r][c] = False

    elif direction == 'up':
        for r in range(n):
            for c in range(n):
                if board[r][c-1] == 0:
                    board[r][c-1] += board[r][c]
                    board[r][c] = 0
                elif board[r][c-1] and board[r][c] and board[r][c-1] == board[r][c]:
                    board[r][c-1] += board[r][c]
                    board[r][c] = 0
                    visit[r][c] = False
    elif direction == 'down':



T = int(input())
for t in range(1, T+1):
    # 바둑판 크기, 방향
    N, direction = input().split()
    n = int(N)

    # 게임판 만들기
    board = [list(map(int, input().split())) for _ in range(n)]
    visit = [[False]*n for _ in range(n)]

    res_arr = game(n, direction, board)
    print(visit)