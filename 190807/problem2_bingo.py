import sys
sys.stdin = open('input2.txt', 'r')

arr1 = [list(map(int, input().split())) for _ in range(5)] # 빙고판
arr2 = [list(map(int, input().split())) for _ in range(6, 11)] # 사회자가 부르는 숫자

for i in range(5): # 총 5개의 열
    for row_value in arr2[i]: # 행에서 값 하나하나 추출
        if row_value in arr1: # 그 값이 arr1에 들어있다면
             # arr1에서 그 값을 빼거라

        for row in range(5):
            if not arr1[row][row]: # 만약 arr1의 대각선이 비어있다면,
                cnt = 1


    for row in range(len(arr2[0])): #
        cross1 += arr[row][row]
        # [0][0] ~ [100][100]
        sum_list.append(cross1)

        cross2 += arr[row][-row]
        # [0][100] ~ [100][0]
        sum_list.append(cross2)









