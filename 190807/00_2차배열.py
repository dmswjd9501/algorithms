list1 = [[0]*3] * 3
list1[0][0] = 1
print(list1)


list2 = [[0]*3 for _ in range(3)]
list2[0][0] = 1
print(list2)