import sys
sys.stdin = open('input2.txt', 'r')

tc = int(input())

for t in range(1, tc+1):
    num = int(input())
    result = ''

    for _ in range(num):
        string = input()
        result += string[0]*int(string[2:4])
    print('#{}'.format(t), end='')

    for i in range(len(result)):
        if i % 10 == 0:
            print()
        print(result[i], end='')
    print()



