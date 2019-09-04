arr = [69, 10, 30, 2, 16, 8, 31, 22]
# index : 0 ~ 7까지

tmp = [0] * len(arr)
# 공간을 미리 만들어 놓고

def mergeSort(lo, hi):
    if lo >= hi:
        return

    mid = (lo + hi) >> 1
    mergeSort(lo, mid)
    mergeSort(mid + 1, hi)

    # i: 왼쪽의 시작위치
    # j: 오른쪽의 시작위치
    # k : 새로 옮겨줄 tmp 시작위치
    i, j, k = lo, mid + 1, lo
    while i <= mid and j <= hi:
        # 만약 앞 < 뒤
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            # 그 다음을 가르키게 해야함
            k, i = k + 1, i + 1
        else:
            tmp[k] = arr[j]
            k, j = k + 1, j + 1

    # 왼쪽이 남아있으면
    while i <= mid:
        tmp[k] = arr[i]
        k, i = k + 1, i + 1

    # 오른쪽이 남아있으면
    while j <= hi:
        tmp[k] = arr[j]
        k, j = k + 1, j + 1

    # tmp에 적어놨던것을 arr에 복사
    for i in range(lo, hi + 1):
        arr[i] = tmp[i]

mergeSort(0, len(arr) - 1)
print(arr)
