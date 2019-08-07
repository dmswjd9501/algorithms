def binarySearch(arr, key):
    lo, hi = 0, len(arr) -1
    # lo = 범위의 시작인덱스, hi = 범위의 끝 인덱스

    while lo <= hi:
        mid = (lo + hi) >> 1
        # >>1 의미: %2
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            # 왼쪽 구간 검색
            hi = mid - 1
        else:
            # 오른쪽 구간 검색
            lo = mid + 1
    return False

# 재귀함수 이용
def binarySearch2(arr, lo, hi, key):
    if lo > hi: return False

    mid = (lo + hi) >> 1

    if arr[mid] == key:
        return True
    elif arr[mid] > key:
        return binarySearch2(arr, lo, mid - 1, key)
    else:
        return binarySearch2(arr, mid + 1, hi, key)

