import sys
sys.stdin = open('input2.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    k, n ,m = map(int, input().split()) # 최대 이동정류장, 종점번호, 설치정류장갯수
    arr = list(map(int, input().split())) # 충전기 리스트
    # print(arr)
    cnt = 0
    fuel = k
    distance = 0

    for i in range(len(arr)): # 정류장마다 체크해주는거야 남은 연료를!!
        distance = (arr[i] - arr[i-1]) if i != 0 else arr[i]
        fuel -= distance

        if arr[i] + k >= n and fuel > -1: # 연료 계산해서 종점을 넘는다? 충분히 갈 수 있다. fuel > -1?????
            print('#{} {}'.format(tc, cnt + 1))
            break

        elif fuel > 0:# 연료가 남았네? 얼만큼 남았는지 확인해야지
            if fuel - (arr[i+1]-arr[i]) >= 0: # 만약 다음 정류장까지 갈 수 있으면 그냥 가자
                continue
            else: # 아니면 지금 충전해야지
                fuel = k
                cnt += 1
        elif fuel == 0: # 연료가 마침 떨어졌다면
            fuel = k # 연료에 k 충전
            cnt += 1 # 연료 충전횟수 += 1
        elif fuel < 0: # 연료가 마이너스 ? => 불가능 0
            print('#{} {}'.format(tc, 0))
            break
        continue