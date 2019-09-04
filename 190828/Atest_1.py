import sys
sys.stdin = open('input_Atest1.txt', 'r')

def shuffle_O_Matic(N, arr):
    tmp1 = sorted(arr) # 오름차순
    tmp2 = sorted(arr, reverse=True) # 내림차순
    L = arr[:N//2] # 절반잘라서 왼쪽
    R = arr[N//2+1:] # 절반잘라서 오른쪽
    hole = [] # 구멍
    mid = N//2
    for x in range(N): # 다이얼이 지정될 수 있는 범위
        if x = 0:
    for i in range(mid):
        hole.append(L[i])
    for j in range(mid):
        hole.append(R[j])
    if hole == tmp1 or hole == tmp2:
        return 0
    else:
    # x=1
        hole[mid-1], hole[mid] = hole[mid], hole[mid-1]
        if hole == tmp1 or hole == tmp2:
            return 1
        else:
        # x = 2
            hole[mid-(mid-1)], hole[mid-(mid-2)], hole[mid], hole[mid+(mid-2)] = hole[mid-(mid-2)], hole[mid-(mid-1)], hole[mid+(mid-2)], hole[mid]
            if hole == tmp1 or hole == tmp2:
                return 2
            else:
            # x = 3
                hole[mid-mid], hole[mid-(mid-1)] = hole[mid-mid], hole[mid-(mid-1)]
                hole[mid-(mid-2)], hole[mid] = hole[mid], hole[mid-(mid-2)]
                hole[mid+(mid-2)], hole[mid-(mid-2)] = hole[mid-(mid-2)], hole[mid+(mid-2)]
                if hole == tmp1 or hole == tmp2:
                    return 3
                else:
                # x = 4
                    hole[mid-(mid-1)], hole[mid-(mid-2)] = hole[mid-(mid-2)], hole[mid-(mid-1)]
                    hole[mid], hole[mid+(mid-2)] = hole[mid+(mid-2)], hole[mid]
                    if hole == tmp1 or hole == tmp2:
                        return 4
                    else:
                    # x = 5
                        hole[mid-(mid-2)], hole[mid] = hole[mid], hole[mid-(mid-2)]
                        if hole == tmp1 or hole == tmp2:
                            return 5
                        else:
                            return -1

tc = int(input())
for t in range(1, tc+1):
    N = int(input())
    card = list(map(int, input().split()))
    print(card)
    result = shuffle_O_Matic(N, card)

    print('#{} {}'.format(t, result))