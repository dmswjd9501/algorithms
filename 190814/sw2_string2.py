import sys
sys.stdin = open('input3.txt', 'r')

tc = int(input())

for t in range(1, tc+1):
    num = int(input())

    print('#{} {}'.format(t), end='')
