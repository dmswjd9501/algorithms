import sys
sys.stdin = open('input4.txt', 'r')

tc = int(input()) # 테스트 케이스 갯수
result = []

# 버블 정렬 함수 선언
def BubbleSort(a):
    for i in range(len(a) - 1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


for t in range(1, tc+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 이 리스트 복사본 하나를 갖자
    copy = list(arr)
    # 버블정렬로 오름차순 정렬 완료
    BubbleSort(copy)

    # pop 메소드로 하나씩 추출
    for i in range(10):
        if i % 2 == 0:
            result.append(copy.pop(-1))
        else:
            result.append(copy.pop(0))

    print('#{}'.format(t), end=' ')
    for element in result:
        print('{}'.format(element), end=' ')
    result=[]
    print()

