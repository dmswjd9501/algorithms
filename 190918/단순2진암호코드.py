import sys
sys.stdin = open('단순2진암호코드.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    tmp = 0
    odd = even = 0
    sum = result = 0
    decode = {'0001101': 0, '0011001': 1, '0010011': 2,
              '0111101': 3, '0100011': 4, '0110001': 5,
              '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

    # 암호 열 찾기
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '1':
                tmp = i
                break

    # 마지막 1을 찾은뒤, 암호 56자리 추출
    start = arr[tmp][::-1].find('1')
    line = arr[tmp][M-(start+56):-start]

    for i in range(0, 56, 7):
        if i % 2:
            odd += decode[line[i:i+7]]

        else:
            even += decode[line[i:i+7]]
        sum += decode[line[i:i+7]]

    result = (odd*3) + even

    if not result % 10:
        res = 0
    else:
        res = sum

    print('#{} {}'.format(t, res))
