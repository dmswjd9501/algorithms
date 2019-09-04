import sys
sys.stdin = open('5105.txt', 'r')

def BFS(x, y, n):
   Q = []
   visit[x][y]= True
   D[x][y] = 0
   Q.append([x, y])

   while Q:
       x, y = map(int, Q.pop(0))
       for c, r in zip([0,0,-1,1], [-1,1,0,0]):
           if x+c > n-1 or y+r > n-1 or x+c <0 or y+r < 0: # over
               continue

           elif data[x + c][y + r] == '3':
               return D[x][y]

           elif visit[x+c][y+r] == False and data[x+c][y+r] == '0':
               Q.append([x+c, y+r])
               visit[x+c][y+r] = True
               D[x+c][y+r] = D[x][y] + 1
   return 0

T = int(input())
for t in range(1, T+1):
   N = int(input())
   data = [input() for _ in range(N)]
   visit = [[False]*N for _ in range(N)]
   D = [[0] * N for _ in range(N)]
   # print(data)

   for row in range(N):
       for column in range(N):
           if data[row][column] == '2':
               x = row
               y = column
               break

   result = BFS(x, y, N)
   print('#{} {}'. format(t, result))