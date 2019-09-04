import sys
import pprint
sys.stdin = open('4861.txt', 'r')

tc = int(input())
for t in range(1, tc+1):
   list1 = []
   result = []
   test, pattern = map(int, input().split())

   for i in range(test):
       list1.append(input().split()) # 들어온 input값들을 2차원리스트에 넣어줌

   # test길이 = pattern길이일 때, 가로 줄 찾기
   for each_list in list1:
       for element in each_list:
           if element[:] == element[::-1]:
               print(element)

   # test길이 != pattern길이일 때, 가로 줄 찾기
   for each_list in list1:
       str = each_list[0]
       for j in range(len(str)): # 0~19
           if str[-1] == str[j] and j != len(str)-1 and len(str[j:]) == pattern:
               if str[j:] == str[:j-1:-1]:
                   print(str[j:])

   # test길이 = pattern길이일 때, 세로 줄 찾기
   for each_list in list1:
       my_list = []
       list2 = []
       for element in each_list:
           for k in range(len(element)):
               my_list.append(element[k])
           pprint.pprint(my_list)
           list2.append(my_list)
   pprint.pprint(list2)
       #     list2.append(my_list)
       # pprint.pprint(list2)
       #         list2.append(my_list)
       # pprint.pprint(list2)
       # pprint.pprint(list2)
           # 행의 좌표 x
           # 열의 좌표 y
           # for i in range(len(my_list))

# a = 'asdff'
# my_list = []
# for i in range(len(a)):
#     my_list.append(a[i])
# print(my_list)


   # list2 =

