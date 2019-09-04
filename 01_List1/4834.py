import sys
sys.stdin = open('4834.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 카드 장수
    arr = list(map(int, input()))

    max_value = max(arr) # 최대값
    num = 0
    cnt = [0] * (max_value + 1) # 최대값 + 1해서 인덱스 빈방 만들기

    for val in arr: # 배열에서 값 하나씩 읽어오기
        cnt[max_value - val] += 1 # cnt[]에 하나씩 더하기
    print(cnt)

    for i in range(len(cnt)):
        if cnt[i] == max(cnt):
            num = max_value - i
            break

    print('#{} {} {}'.format(tc, num, cnt[max_value - num]))


