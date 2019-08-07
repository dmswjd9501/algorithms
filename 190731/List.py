import sys
sys.stdin = open('input2.txt', 'r')

# view 문제
for tc in range(1, 11): # 1부터 10까지 tc 반복
    N = int(input()) # 테스트케이스의 길이
    arr = list(map(int, input().split()))

    result = 0
    for i in range(2, len(arr)-2):
        if arr[i] > arr[i-2] and arr[i] > arr[i-1] and arr[i] > arr[i+1] and arr[i] > arr[i+2]:
            result += arr[i] - max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])




    print('#{} {}'.format(tc, result))
