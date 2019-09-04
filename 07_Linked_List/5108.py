import sys
sys.stdin = open('5108.txt', 'r')
from linkedlist1 import Node, List


T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    mylist = List()
    arr = list(map(int, input().split()))

    for element in arr:
        mylist.insertlast(Node(element))

    add = [list(map(int, input().split())) for _ in range(M)]

    for i in range(len(add)):
        k = add[i][0]
        mylist.insertAt(k, Node(add[i][1]))

    print('#{}'.format(t), end=' ')
    tmp = mylist.printlist()
    print(tmp[L])