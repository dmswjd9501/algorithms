# import random
#
# list1 = [[0]*5 for i in range(5)]
# for a in range(5):
#     list1.append(random.sample(range(1, 26), 5))
#         for j in range(5):
#             list
#             print('{}'.format()end='')
#             print()
#

# arr = 'ABC'
# bits = [0] * 3
#
# # 첫번째 원소를 부분집합에 포함할건지 말건지
# for i in range(2):
#     bits[0] = i
#     # 두번째 원소를 부분집합에 포함할건지 말건지
#     for i in range(2):
#         bits[1] = i
#         # 세번쨰 원소를 부분집합에 포함할건지 말건지
#         for i in range(2):
#             bits[2] = i
#             print(bits, end='> ')
#             for i in range(len(bits)):
#                 if bits[i]: print(arr[i], end=' ')
#             print()
#
#
arr = [3, 6, 7, 1, 5, 4]

for i in range(len(arr)):
    for j in range(len(arr)):
        if i & (1 << j):
            print(arr[j], end=', ')

    print()