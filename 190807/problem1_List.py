import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input()) # 테스트 케이스 번호
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 100 x 100 2차 배열 리스트

    sum_list = []
    for row in arr: # 2차 배열이므로 뽑으면 한 행씩(list) 추출된다.
        sum_list.append(sum(row)) # 행을 다 더해서 sum_list에 더해준다

    for column in range(len(arr[0])): # 행의 길이만큼 열 list를 뽑는다
        sum_value = 0
        for row in range(len(arr[0])):
            sum_value += arr[row][column]

        sum_list.append(sum_value) # 열을 다 더해서 sum_list에 더해준다.

    cross1 = 0 # 대각선1
    cross2 = 0 # 대각선2

    for row in range(len(arr[0])):
        cross1 += arr[row][row]
        # [0][0] ~ [100][100]
        sum_list.append(cross1)

        cross2 += arr[row][-row]
        # [0][100] ~ [100][0]
        sum_list.append(cross2)

    print('#{} {}'.format(tc, max(sum_list)))





