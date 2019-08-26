import sys
sys.stdin = open('input_4837.txt', 'r')

def subset(k, n):
    global N, K, ans
    if k == n:
        cnt = S = 0
        for i in range(n):
            if bits[i]:
                cnt, S = cnt + 1, S + (i+1)
        if cnt == N and S == K:
            ans += 1
    else:
        bits[k] = 1; subset(k+1, n)
        bits[k] = 0; subset(k + 1, n)

# solution2
#
# def subset(k, n, cnt, cur_sum): # cnt = 현재 선택한 원소수, cur_sum : 원소들합
#
#     global ans, N, K
#     if cnt > N or cur_sum > K: return
#     if k == n:
#         if cnt == N and cur_sum == K: ans += 1
#         return
#     subset(k+1, n, cnt+1, cur_sum + k)
#     subset(k+1, n, cnt, cur_sum)

T = int(input())
for tc in range(1, T +1 ):
    N, K = map(int, input().split())
    ans = 0
    subset(1, 13, 0, 0)
    print('#{} {}'.format(tc, ans))
