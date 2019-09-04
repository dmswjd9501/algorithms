import sys
sys.stdin = open('input_4873.txt', 'r')

def remove(words, long):
    tmp = ''
    for i in range(long-1):
        if words[i] == words[i+1]:
            tmp = words[:i] + words[i+2:long]
            return remove(tmp, len(tmp))
    return words

T = int(input())
for t in range(1, T+1):
    words = input()
    result = remove(words, len(words))

    print('#{} {}'.format(t, len(result)))


