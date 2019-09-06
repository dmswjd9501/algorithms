import sys
sys.stdin = open('othello.txt', 'r')

def othello(n, r, c, color):

    # 현재 바둑알로 다음 순서 정하기
    if color == 1:
        next = 2
    else:
        next = 1

    # 좌표 : -1 0 1 (대각선까지 포함)
    for x in range(-1, 2):
        for y in range(-1, 2):
            i = 1
            # 바둑판을 넘지 않고, 다음 순서 확인
            while (0 <= r+(x*i) < n) and (0 <= c+(y*i) < n) and board[r+(x*i)][c+(y*i)] == next:
                if (0 <= r+(x*(i+1)) < n) and (0 <= c+(y*(i+1)) < n) and board[r+(x*(i+1))][c+(y*(i+1))] == color:
                    for j in range(1, i+2):
                        board[r+x*j][c+y*j] = color
                i += 1


T = int(input())
for t in range(1, T+1):
    # 보드 한변의 길이, 돌을 놓는 횟수
    n, m = map(int, input().split())
    # 돌을 놓을 위치와 색깔
    arr = [list(map(int, input().split())) for _ in range(m)]

    # 초기 게임판 완성
    mid = n//2
    board = [[0]*n for _ in range(n)]
    board[mid-1][mid-1] = board[mid][mid] = 2 # 백돌
    board[mid-1][mid] = board[mid][mid-1] = 1 # 흑돌

    # 좌표 받아서 색칠 -> 함수로 색칠가능한지 확인
    for i in range(m):
        r, c, color = arr[i][0], arr[i][1], arr[i][2]
        board[r-1][c-1] = color
        othello(n, r-1, c-1, color)

    # 바둑돌 개수 카운트
    w_cnt = b_cnt = 0
    for i in range(n):
        w_cnt += board[i].count(2)
        b_cnt += board[i].count(1)
    print('#{} {} {}'.format(t, b_cnt, w_cnt))


