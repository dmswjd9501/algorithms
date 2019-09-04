import sys
sys.stdin = open('input3.txt', 'r')

tc = int(input())
for t in range(1, tc+1):
    pattern = input()
    test = input()

    # pattern의 알파벳 갯수세기
    count = {}
    for element in pattern:
        if element not in count:
            count[element] = 1
        else:
            count[element] += 1

    # test 문자열에서 위에서 만든 딕셔너리 key 빈도수 찾기
    result = {}
    for key in count:
        for element2 in test:
            if element2 in key and key not in result:
                result[element2] = 1
            elif element2 in key:
                result[element2] += 1

    # 그 값중에 가장 큰 값
    print(max(result.values()))
