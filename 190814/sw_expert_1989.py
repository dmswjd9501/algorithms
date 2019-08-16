import sys
sys.stdin = open('input1.txt', 'r')

tc = int(input())

for t in range(1, tc+1):
    word = input()
    result = 0

    N = len(word)
    for i in range(N//2):
        if word[i] == word[N-1-i]:
            result = 1
        else:
            result = 0
            break
    print('#{} {}'.format(t, result))
