import sys
sys.stdin = open('5110.txt', 'r')
from linkedlist2 import Node, List

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    mylist = List()
    arr = [list(map(int, input().split())) for _ in range(M)]
    print(arr)

    for element in arr:
        mylist.insertlast(Node(element))
    tmp = arr[0]
    for i in range(1, M): # 1 ~ 3
        for j in range(len(tmp)): # 0 ~ 3
            if arr[i][0] < tmp[j]: # 다음 순열 첫글자 < tmp
                tmp2 = tmp[:j]
                tmp3 = tmp[j:]
                tmp = []
                tmp = tmp2 + arr[i] + tmp3
                break
            elif j == len(tmp) - 1 and arr[i][0] >= tmp[j]:# 끝까지 왔는데도 큰 숫자가 없으면
                tmp = tmp + arr[i]

    print('#{}'.format(t), end=' ')

    tmp = tmp[::-1]
    for k in range(10):
        print(tmp[k], end=' ')
    print()

