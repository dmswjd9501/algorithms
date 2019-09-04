import sys
sys.stdin = open('input_4881.txt', 'r')

# 순열로 푸는게 맞는 방법 -> 모든 경우의 수를 따져봐야함
def perm(k, n, used, cursum): # 각행마다 골라야하기 때문에 n
    global MIN
    if cursum >= MIN: return

    if k == n:
        MIN = min(MIN, cursum)
        return

    for i in range(n):
        if used & (1 << i): continue

        pern(k+1, n, used | (1 << i), cursum + arr[k][i])

tc = int(input())
for t in range(1, tc+1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
