import sys

sys.stdin = open('input5.txt', 'r')

tc = int(input()) # 테스트케이스 개수

for t in range(1, tc+1):
    n = int(input()) # 원형 금속 막대의 개수
    arr = list(map(int, input().split())) # 굵기
    a = []
    b = []

    for i in range(0, 2*n, 2): # 그룹으로 묶기
        a.append([arr[i], arr[i+1]])

    b.append(a.pop(0)) # a의 첫번째 값을 제거하여 b 리스트에 넣기

    for index in range(len(a)):
        if b[0][1] == a[index][0]:
            b.append(a.pop(index))
        elif b[0][0] == a[index][1]:
            b.insert(0, a.pop(index))
        else:
            break

    print(a)
    print(b)


