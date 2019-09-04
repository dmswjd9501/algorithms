import sys
sys.stdin = open('input_1220.txt', 'r')

for t in range(1, 11):
    board = []
    count = 0
    N = int(input())
    for _ in range(N):
        board.append(list(map(int, input().split())))

    for column in range(N):
        tmp = 0
        for row in range(N):
            if board[row][column] == 1 and tmp == 2:
                tmp == 1
            elif board[row][column] == 2 and tmp == 1:
                count += 1
                tmp = 0
    print('#{} {}'.format(t, count))
