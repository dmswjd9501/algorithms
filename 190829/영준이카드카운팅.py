import sys
sys.stdin = open('input_card.txt', 'r')

tc = int(input())
for t in range(1, tc+1):
    words = input()
    result = ''
    S_card = [[] for _ in range(13)]
    D_card = [[] for _ in range(13)]
    H_card = [[] for _ in range(13)]
    C_card = [[] for _ in range(13)]
    print('#{}'.format(t), end=' ')

    for i in range(len(words)):
        if not i % 3:
            if not 1 <= int(words[i+1:i+3]) <= 13:
                result = 'ERROR'
                break
            if words[i] == 'S':
                S_card[int(words[i+1:i+3])].append(1)
            elif words[i] == 'D':
                D_card[int(words[i+1:i+3])].append(1)
            elif words[i] == 'H':
                H_card[int(words[i+1:i+3])].append(1)
            elif words[i] == 'C':
                C_card[int(words[i+1:i+3])].append(1)

    s_cnt, d_cnt, h_cnt, c_cnt = 0, 0, 0, 0
    if result == 'ERROR':
        print('ERROR')
    else:
        for i in range(13):
            if S_card[i].count(1) > 1 or D_card[i].count(1) > 1 or H_card[i].count(1) > 1 or C_card[i].count(1) > 1:
                result = 'ERROR'
                print('ERROR')
                break
            else:
                if S_card[i] == []:
                    s_cnt += 1
                if D_card[i] == []:
                    d_cnt += 1
                if H_card[i] == []:
                    h_cnt += 1
                if C_card[i] == []:
                    c_cnt += 1

    if result != 'ERROR':
        print(s_cnt, end=' ')
        print(d_cnt, end=' ')
        print(h_cnt, end=' ')
        print(c_cnt, end='')
        print()


