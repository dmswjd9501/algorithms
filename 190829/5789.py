import sys
sys.stdin = open('5789.txt', 'r')

for t in range(1, int(input())+1):
    N, Q = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(Q)]
    box = [0] * N
    print('#{}'.format(t), end=' ')
    for i in range(Q):
        L = arr[i][0]
        R = arr[i][1]
        for j in range(L-1, R):
            box[j] = i+1
    for i in range(len(box)):
        print(box[i]) if i == len(box)-1 else print(box[i], end=' ')

for t in range(1, int(input()) + 1):
    N, Q = map(int, input().split())
    nums = [0] * N
    for i in range(1, Q + 1):
        l, r = map(int, input().split())
        for j in range(l, r + 1):
            nums[j - 1] = i
    res = ' '.join(list(map(str, nums)))

    print('#{} {}'.format(t, res))