import sys
sys.stdin = open('input_4866.txt', 'r')

def check_paren(words):
    stack = []
    for word in words:
        if word == '(' or word == '{':
            stack.append(word)
        elif word == ')':
            if len(stack) == 0:
                return False
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
        elif word == '}':
            if len(stack) == 0:
                return False
            else:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        else:
            continue
    if len(stack) != 0:
        return False
    return True

tc = int(input())
for t in range(1, tc+1):
    print('#{}'.format(t), end=' ')
    words = input()
    if check_paren(words):
        print('1') 
    else:
        print('0')


