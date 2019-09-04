import sys
sys.stdin = open('input_4880.txt', 'r')

# def game(a, b):
#     if card[a] == card[b]:
#         return a
#     elif card[a] == 1:
#         return b if card[b] == 2 else a
#     elif card[a] == 2:
#         return a if card[b] == 1 else b
#     elif card[a] == 3:
#         return b if card[b] == 1 else a
#
#
# def tournament(arr):
#     if len(arr) == 1:  # 만약 최종 1인이라면
#         return arr[0]
#     # 최종 1인이 아니라면 다시 절반으로 슬라이싱해서 가위바위보
#     # 여기서 인덱스는 1부터 시작
#     return game(tournament(arr[:(len(arr) + 1) // 2]), tournament(arr[(len(arr) + 1) // 2:]))
#
#
# tc = int(input())
# for t in range(1, tc + 1):
#     N = int(input())
#     card = list(map(int, input().split()))
#     # 번호판
#     i = list(range(N))
#
#     print('#{} {}'.format(t, tournament(i) + 1))

win = {1:3, 2:1, 3:2} # 가위바위보가 이기는 상대 값을 저장해놓음

def play(lo, hi):
    if lo == hi: return lo
    mid = (lo+hi) >> 1
    l = play(lo, mid)
    r = play(mid+1, hi)

    if cards[i] == cards[r] or win[cards[l]] == cards[r]:
        return l
    return r
