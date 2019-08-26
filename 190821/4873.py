import sys
sys.stdin = open('input_4873.txt', 'r')


tc = int(input())
for t in range(1, tc+1):
    string = input()
    res = search(string)

    print('#{} {}'.format(t, res))