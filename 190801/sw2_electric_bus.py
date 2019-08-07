import sys
sys.stdin = open('input2.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    k, n ,m = map(int, input().split()) # 최대 이동정류장, 종점번호, 설치정류장갯수
    arr = list(map(int, input().split())) # 충전기 리스트

    cnt = 0
    fuel = k
    distance = 0

    for i in range(len(arr)):
        distance = (arr[i] - arr[i-1]) if i != 0 else arr[i]
        fuel -= distance

        if arr[i] + k >= n and fuel > -1:
            print('#{} {}'.format(tc, cnt + 1))
            break

        elif fuel > 0:
            if fuel - (arr[i+1]-arr[i]) >= 0:
                continue
            else:
                fuel = k
                cnt += 1
        elif fuel == 0:
            fuel = k
            cnt += 1
        elif fuel < 0:
            print('#{} {}'.format(tc, 0))
            break
        continue
#
#
#     for x in range(n): # 내 현재 위치
#         if street[x] == 1:
#             cnt += 1  # 충전소가 마침 연료 떨어질때있으면, 카운트 + 1
#             print('if {}'.format(cnt))
#         : # 충전소가 없으면
#             while street[x-1] != 1: # 뒤로 하나씩 빼면서 1일때를 찾아
#                 x -= 1
#             cnt += 1
#             print('else {}'.format(cnt))
#         if x >= n:
#             break
#
# # print('#{} {}'.format(tc, result))