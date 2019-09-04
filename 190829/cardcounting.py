import sys
sys.stdin = open('input_card.txt', 'r')

tc = int(input())
for t in range(1, tc+1):
    cards = input()
    print('#{}'.format(t), end=' ')
    # print(cards)
    s_cnt, d_cnt, h_cnt, c_cnt = 13, 13, 13, 13
    tmp = 0
    card = [cards[i:i+3] for i in range(0, len(cards), 3)]

    for i in range(len(card)):
        for j in range(len(card)):
            if i != j:
                if card[i] == card[j]:
                    tmp = 1
                    break
        if tmp == 1:
            break
        elif card[i][0] == 'S':
            s_cnt -= 1
        elif card[i][0] == 'D':
            d_cnt -= 1
        elif card[i][0] == 'H':
            h_cnt -= 1
        elif card[i][0] == 'C':
            c_cnt -= 1
    if tmp:
        print('ERROR')
    else:
        print(s_cnt, end=' ')
        print(d_cnt, end=' ')
        print(h_cnt, end=' ')
        print(c_cnt, end='')
        print()
