import sys
sys.stdin = open('othello.txt', 'r')

def othello(n, m, board):
    cnt_A = cnt_B = 0 # 플레이어
    for i in range()





T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    # print(arr)

    # 초기 게임판 완성
    mid = n//2
    board = [[]*n for _ in range(n)]
    board[mid-1][mid-1], board[mid][mid-1] = 2 # 백돌
    board[mid-1][mid], board[mid][mid] = 1 # 흑돌


    result = othello(n, board)
    print('#{} {}'.format(t, result))