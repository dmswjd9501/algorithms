import sys
sys.stdin = open('input3.txt', 'r')

tc = int(input())
for t in range(1, tc+1):
    arr = list(map(int, input().split()))
    start = 1
    end = arr[0]
    A_cnt, B_cnt = 0, 0

    while start <= end:
        mid = int((start + end)/ 2)
        A_cnt += 1
        if arr[1] == mid:
            break
        elif arr[1] > mid:
            start = mid
        else:
            end = mid

    start = 1
    end = arr[0]
    while start <= end:
        mid = int((start + end) / 2)
        B_cnt += 1
        if arr[2] == mid:
            break
        elif arr[2] > mid:
            start = mid
        else:
            end = mid

    if A_cnt > B_cnt:
        win = 'B'
    elif A_cnt == B_cnt:
        win = '0'
    else:
        win = 'A'

    print('#{} {}'.format(t, win))
