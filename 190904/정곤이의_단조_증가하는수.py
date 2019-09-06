import sys
sys.stdin = open('정곤이.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split())) # 순열 사용

    result = []

    for i in range(N):
        for j in range(N):
            if i == j: continue
            elif i != j and i < j:
                result.append(num[i]*num[j])

    print(result)

    compare = []

    for element in result:
        for i in range(len(str(element))): # 0 1
            while j != len(str(element))-1:




                j += 1




    #     if element == element.sorted():
    #         compare.append(element)
    #
    # if len(compare) == 0:
    #     print(-1)
    # else:
    #     print(max(compare))
