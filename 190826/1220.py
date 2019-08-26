import sys
sys.stdin = open('input_1220.txt', 'r')

#
# def partition(a, begin, end):
#     pivot = (begin + end) // 2
#     L = begin
#     R = end
#     while L < R:
#         while a[L] < a[pivot] and L < R:
#             L += 1
#         while a[R] >= a[pivot] and L < R:
#             R -= 1
#         if L < R:
#             if L == pivot:
#                 pivot = R
#             a[L], a[R] = a[R], a[L]
#     a[pivot], a[R] = a[R], a[pivot]
#     return R
#

#
#     for element in compare:
#         stack = []
#         if element != 0:
#             stack.append(element)
#     result = partition(compare, begin, end)
#
#
# print('#{} {}'.format(tc, result))

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    middle = N // 2

    for column in range(N):
        for row in range(middle):
            begin = arr[row][column]
            end = arr[N - row - 1][column]
        arr1, arr2 = [], []
        if begin == 2 and len(arr1) == 0:
            arr[row][column] = 0
        elif begin != 0:
            arr1.append(begin)
    ​
        if end == 1 and len(arr2) == 0:
            arr[N - row - 1][column] = 0
        elif end != 0:
            arr2.append(end)
​
        arr2.reverse()
        arr1.extend(arr2)
​
        tmp = 0
        for i in tmp1:
            if tmp == 0 and i == 1:
                tmp = 1
            elif tmp == 1 and i == 2:
                tmp = 0
                cnt += 1
        print('#{} {}'.format(t, cnt))
