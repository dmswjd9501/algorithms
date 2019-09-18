import sys
sys.stdin = open('5186_input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = float(input())
    binary_str = ''
    i = 1

    while N > 0:
        if N >= 2**(-i):
            N -= 2**(-i)
            binary_str = binary_str + '1'
        else:
            binary_str = binary_str + '0'
        i += 1
        if len(binary_str) == 13:
            binary_str = 'overflow'
            break
        else:
            continue

    print('#{} {}'.format(t, binary_str))








    # while N != 0:
    #     if N >= 2**(-i):
    #         N -= 2**(-i)
    #         binary_str = binary_str + '1'
    #     else:
    #         binary_str = binary_str + '0'
    #     i += 1
    #
    # if i <=12 :
    #     result = binary_str
    # else:
    #     result = 'overflow'
    #
    # print('#{} {}'.format(t, result))
