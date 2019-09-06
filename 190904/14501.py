N = int(input())
arr = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
def backstrack():
