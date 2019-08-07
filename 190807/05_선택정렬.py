arr = [64, 25, 10, 22, 11]
n = len(arr)

for i in range(n-1): # 0 ~ n-2
    minIdx = i
    for j in range(i+1, n):
        if arr[minIdx] > arr[j]:
            minIdx = j
    arr[i], arr[minIdx] = arr[minIdx], arr[i]

print(arr)

