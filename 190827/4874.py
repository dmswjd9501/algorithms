import sys
sys.stdin = open('input_4874.txt', 'r')

tc = int(input())

for t in range(1, tc+1):
    arr = list(input().split())
    stack = []
    print('#{}'.format(t), end=' ')
    for element in arr:
        if element in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            stack.append(int(element))
        elif element == '+' and len(stack) >= 2:
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif element == '-' and len(stack) >= 2:
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif element == '*' and len(stack) >= 2:
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        elif element == '/' and len(stack) >= 2:
            b = stack.pop()
            a = stack.pop()
            stack.append(a // b)
        elif element == '.' and len(stack) == 1:
            print(stack.pop())
        else:
            print('error')
            break