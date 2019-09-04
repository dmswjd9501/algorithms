import sys
sys.stdin = open('4837.txt', 'r')

tc = int(input())
A = [i for i in range(1, 13)]

# 함수 선언
def subset_sum(num, A):
    n = len(A) # 집합 A의 길이
    cnt = 0 # 합과 같을때의 카운트
    for i in range(2**n):
        list1 = []
        for j in range(n):
            subset = i & (2**j)
            if subset:
                list1.append(A[j])
        if len(list1) == num[0]:
            if sum(list1) == num[1]:
                cnt +=1
    return cnt

for tc in range(1, tc + 1):
    num = list(map(int, input().split()))
    result = 0
    result = subset_sum(num, A)
    print('#{} {}'.format(tc, result))