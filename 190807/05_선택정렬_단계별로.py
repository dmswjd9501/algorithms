arr = [64, 25, 10, 22, 11]
n = len(arr)

minIdx = 0
for j in range(1,len(arr)):
    if arr[minIdx] > arr[j]:
        minIdx = j

arr[0], arr[minIdx] = arr[minIdx], arr[0]

minIdx = 1
for j in range(2,len(arr)):
    if arr[minIdx] > arr[j]:
        minIdx = j

arr[1], arr[minIdx] = arr[minIdx], arr[1]


minIdx = 2
for j in range(3,len(arr)):
    if arr[minIdx] > arr[j]:
        minIdx = j

arr[2], arr[minIdx] = arr[minIdx], arr[2]


minIdx = 3
for j in range(4,len(arr)):
    if arr[minIdx] > arr[j]:
        minIdx = j

arr[3], arr[minIdx] = arr[minIdx], arr[3]

minIdx = 4
for j in range(5,len(arr)):
    if arr[minIdx] > arr[j]:
        minIdx = j

arr[4], arr[minIdx] = arr[minIdx], arr[4]



print(arr)