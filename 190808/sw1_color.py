import sys
sys.stdin = open('input1.txt', 'r')

tc = int(input()) # 테스트 케이스 번호

for t in range(1, tc+1):
    N = int(input()) # 색칠할 사각형 갯수
    arr1 = [[0] * 10 for _ in range(10)]  # 10x10 격자 만들기
    cnt = 0 # 보라색 세어줄 변수

    for num in range(N):
        arr2 = []
        arr2 = list(map(int, input().split()))

        if arr2[-1] == 1:  # arr2의 배열의 마지막 값으로 색깔 확인. 만약에 빨간색이라면
            for x in range(arr2[0], arr2[2]+1): # x좌표
                for y in range(arr2[1], arr2[3]+1): # y좌표
                    arr1[x][y] += 1 
        else:  # 만약 파랑색이라면
            for x in range(arr2[0], arr2[2]+1):
                for y in range(arr2[1], arr2[3]+1):
                    arr1[x][y] += 2

    for i in range(10):
        cnt += arr1[i].count(3) # 2차원배열이므로 for문으로 하나씩 값에 접근해줘야한다.
                                # 3인 애들의 갯수

    print('#{} {}'.format(t, cnt))