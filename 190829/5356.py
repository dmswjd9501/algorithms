import sys
sys.stdin = open('5356.txt', 'r')

T = int(input())
for t in range(1, T+1):
    max = 0
    words = []
    for _ in range(5):
        word = input()
        words.append(word)
        if len(word) > max:
            max = len(word)

    print('#{}'.format(t), end=' ')
    for c in range(max):
        for r in range(5):
            if len(words[r]) <= c: continue
            else:
                print(words[r][c], end='')
    print()