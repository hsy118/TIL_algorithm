"""
print('{} {}'.format(1, 2))
N, M = map(int, input().split())
print('#{} {}'.format(tc, find())
"""
def check(string):
    result = []
    for i in range(len(text)):
        if string[i] == '(' or string[i] == '{':
            result.append(string[i])
        elif string[i] == ')':
            if len(result) == 0 or result[-1] != '(':
                return 0
            else:
                result.pop()
        elif string[i] == '}':
            if len(result) == 0 or result[-1] != '{':
                return 0
            else:
                result.pop()
    if len(result) > 0:
        return 0
    else:
        return 1

T = int(input())
for tc in range(1, T+1):
    text = input()
    print(f'#{tc} {check(text)}')
