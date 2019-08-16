import sys
sys.stdin = open('input5.txt', 'r')

def search(matrix):
    max_len = 0
    for x in range(100):
        for front in range(100):
            for end in range(99, front, -1):
                if max_len >= end - front + 1:
                    break
                if matrix[x][front : end + 1] == matrix[::-1]:
                    if MaxLen >= Len:
                        break
                    if max_len < end-front+1:
                        max_len = end-front+1
                        break
                return max_len


for _ in range(1, 11):
    matrix = []
    t = input()
    for _ in range(100):
        matrix.append(input())
        result = search(matrix)
        matrix_2= list(zip(*matrix))
        value = max(result, search(matrix_2))

    print('#{} {}'.format(t, result))

