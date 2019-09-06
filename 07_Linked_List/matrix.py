import sys
sys.stdin = open('matrix_search.txt', 'r')

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    col = [0] * (n+1)