import sys
sys.stdin = open('input5.txt', 'r')

for tc in range(1, 11):
    N = int(input()) # 제한 덤프 횟수
    arr = list(map(int, input().split())) # 박스 높이

    arr.sort()


    for i in range(N):
        if arr[-1] - arr[0] > 1:
            arr[-1] -= 1
            arr[0] += 1
            arr.sort()

        else:
            break

    print('#{} {}'.format(tc, arr[-1] - arr[0]))
