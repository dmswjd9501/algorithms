import sys
sys.stdin = open('input_5185.txt', 'r')


T = int(input())
for t in range(1, T+1):
    N, hexa = input().split()
    n = int(N)
    # 16진수를 10진수로 먼저 바꾼다
    d = int('0x'+hexa, 16)
    # 10진수를 2진수로 바꿔준다
    result = format(d, 'b')

    # 4로 떨어지지 않으면 0 추가
    if len(result) % 4 == 3:
        res = '0' + result
    elif len(result) % 4 == 2:
        res = '00' + result
    elif len(result) % 4 == 1:
        res = '000' + result
    else:
        res = result

    print('#{} {}'.format(t, res))

