import sys
sys.stdin = open('4864.txt', 'r')

tc = int(input())

def search(pattern, test):
    i = 0 # test word의 인덱스
    j = 0 # pattern word의 인덱스
    M = len(test)
    N = len(pattern)
    while i < M and j < N:
        if test[i] != pattern[j]: # 불일치가 발생한다면
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == N: # 결과를 찾았을 때,
        return 1
    else:
        return 0

for t in range(1, tc+1):
    pattern = input()
    test = input()
    value = search(pattern, test)
    print(f'#{t} {value}')
