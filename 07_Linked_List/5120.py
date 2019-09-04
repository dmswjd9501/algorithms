import sys
sys.stdin = open('5120.txt', 'r')
from linkedlist3 import Node, List

T = int(input())
for t in range(1, T+1):
    # n개 숫자, m번째칸, k회 반복
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    # print(arr)
    tmp2 = arr
    mylist = List()
    for element in arr:
        mylist.insertlast(Node(element))

    i, j = 0, m

    while i < k:
        if len(tmp2) > j:
            tmp = arr[j-1] + arr[j]
            tmp2 = mylist.insertAt(j, Node(tmp))
        else:
            diff = j - len(tmp2)
            tmp = arr[diff-1] + arr[diff]
            tmp2 = mylist.insertAt(diff, Node(tmp))
        j += m
        i += 1


    tmp2 = tmp2[::-1]
    print(tmp2)


