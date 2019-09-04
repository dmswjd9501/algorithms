import sys

sys.stdin = open('electric_stick.txt', 'r')

tc = int(input())
 
for t in range(1, tc + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    num = []
    i = 0
    a = ''
    b = ''
     
    for _ in range(N):
        num.append(arr[i:i+2])
        i += 2
    a += str(num[0].pop(0)) + ' ' + str(num[0].pop(0))
    num.pop(0)
     
    while len(num) > 0:
        j = 0
        while len(num) > 0:
            if int(a[-2:]) == num[j][0]:
                a += ' ' + str(num[j].pop(0))+ ' ' +str(num[j].pop(0))
                num.pop(j)
                break
            elif int(a[0:2]) == num[j][1]:
                b += (str(num[j].pop(0)) + ' ' + str(num[j].pop(0)) + ' ' + a)
                a = b
                num.pop(j)
                b = ''
                break
            j += 1
 
    print('#{} {}'. format(t, a))

