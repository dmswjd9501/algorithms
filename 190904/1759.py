import sys
sys.stdin = open('1759.txt', 'r')
#
# pwd = []
# alpha = ('a', 'e', 'i', 'o', 'u')
# def backtrack(k, mo, ja):
#     if len(pwd) == L:
#         print(pwd)
#         return
#     if k == C:
#         return
#     pwd.append(words[k])
#     a = b = 0
#     if words[k] in alpha:
#         a = 1
#     else:
#         b = 1
#     backtrack(k+1, mo+a, ja+b) # k번째 요소를 포함하는 경우
#     pwd.pop()
#     backtrack(k+1) # k번째 요소를 포함하지 않는 경우
#
# L, C = map(int, input().split())
# words = list(input().split())
# words.sort() # 정렬


# # 부분집합 만들기
# backtrack(0, 0, 0)
#
# # 중복순열 3파이2
# words = 'ABC'
# N = len(words)
# for i in range(N):
#     for j in range(N):
#         print(words[i], words[j])
#
# # 순열 3P2
# for i in range(N):
#     for j in range(N):
#         if i == j: continue
#         print(words[i], words[j])
#
# # 조합 3C2
# for i in range(N):
#     for j in range(i+1, N):
#         if i == j: continue
#         print(words[i], words[j])
#
# # 중복조합 3H2 ((3+2-1)C2)
# for i in range(N):
#     for j in range(i+1, N):
#         for k in range(j+1, N):
#             print(words[i], words[j], words[k])

arr = 'ABCDE'
N = len(arr)
N, R = 5, 3
choose = []

def comb(k, start):
    if k == R:
        print(choose)
        return

    for i in range(start, N):
        # i번째 정보를 저장
        choose.append(arr[i])
        comb(k+1, i+1)
        choose.pop()

comb(0, 0)