import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input()) # 테스트 케이스 번호
    arr = [list(map(int, input().split())) for _ in range(100)]


    Max = 0 # 최대값(답)

    # 행우선 순회
    for i in range(100):
        S = 0
        for j in range(100):
            S += arr[i][j]
        Max = max(Max, S)

    # 열우선 순회
    for i in range(100):
        S = 0
        for j in range(100):
        S=0
        for j in range(100):
            S += arr[j][i]
        Max = max(Max, S)


    # 대각 순회
    S = 0
    for i in range(100):
        S += arr[i][i]
    Max= max(Max, S)

    S = 0
    for i in range(100):
        S += arr[i][99-i]
    Max = max(Max, S)

