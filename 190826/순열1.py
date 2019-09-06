# 1. 중복순열 - 모든 자리에서 중복 검사없이 추출
# arr = 'ABC'
# N = len(arr)
# for i in range(N):
#     for j in range(N):
#         for k in range(N):
#             print(arr[i], arr[j], arr[k])

# 2. 순열
arr = 'ABC'
N = len(arr)
for i in range(N):
    for j in range(N):
        if i == j: continue
        for k in range(N):
            if i == k or k == j: continue
            print(arr[i], arr[j], arr[k])

# 2. solution2
# arr = 'ABC'
# N = len(arr)
# used = [0] * N # 지금까지 선택한 원소들의 집합
# order = [0] * N # 실제 요소들의 순서(index를 기록)
#
# def perm(k, n):
#     if k == n:
#         for i in range(N):
#             print(arr[order[i]], end=' ')
#         print()
#         return
#     used = [False] * N
#     for i in range(k): # 지금까지 선택한 k개의 원소를 확인
#         used[order[i]] = True
#
#     for i in range(N): # 선택하지 않은 요소들에 대해
#         if used[i]:
#             continue
#         order[k] = i
#         perm(k+1, n)
#
# perm(0, N)

# solution3 :
# arr = 'ABC'
# N = len(arr)
# order = [0] * N # 원소의 인덱스의 순서를 지정

# def perm(k, n, used): # 하나의 순열을 생성
#     if k == n:
#         for i in range(n):
#             print(arr[order[i]], end=' ')
#         print()
#         return

#     for i in range(n): # 선택하지 않은 요소들에 대해
#         if used & (1 << i): continue
#         order[k] = i
#         perm(k+1, n, used | (1 << i))

# perm(0, N, 0)