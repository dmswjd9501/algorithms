import sys
sys.stdin = open('5122.txt', 'r')

from listedlist4 import Node, List

T = int(input())
for t in range(1, T+1):
    n, m, l = map(int, input().split())
    arr = list(map(int, input().split()))
    mylist = List()
    for elem in arr:
        mylist.insertlast(Node(elem))
    plus = list(input().split() for _ in range(m))

    for i in range(m):
        if plus[i][0] == 'I':
            mylist.insertAt(int(plus[i][1]), Node(int(plus[i][2])))
        elif plus[i][0] == 'D':
            mylist.deleteAt(int(plus[i][1]))
        elif plus[i][0] == 'C':
            mylist.changeAt(int(plus[i][1]), Node(int(plus[i][2])))

    print('#{}'.format(t), end=' ')
    tmp = mylist.printlist()
    if not tmp or l > len(tmp):
        print('-1')
    else:
        print(tmp[l])

