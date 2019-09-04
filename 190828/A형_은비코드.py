import sys
sys.stdin = open('input_Atest.txt', 'r')



def dec(x, c):
    L = collections.deque()
    R = collections.deque()
    temp = collections.deque()
    if x >= N //2:
        for i in range(0, (N//2)):
            R.append(c[i])
        for i in range((N//2), N):
            L.append(c[i])
        x = N-x-1
    else:
        for j in range(0, (N//2)):
            L.append(c[i])
        for i in range((N//2), N):
            R.append(c[i])
    for i in range((N//2)-x):
        temp.append(L.popleft())
    for i in range(x):
        temp.append(R.popleft())
        temp.append(L.popleft())
    temp.extend(R)
    return temp

def shuffle(card, count):
    global result
    scard = []












    T = int(input())

    for t in range(1, T + 1):
        N = int(input())
        Min = 0xfffff
        cards = list(map(int, input().split()))
        cards_s = sorted(cards)
        cards_r = sorted(cards, reverse=True)