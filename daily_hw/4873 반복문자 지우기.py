T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    stack = []
    for i in range(len(arr)):
        if len(stack) != 0 and arr[i] == stack[-1]:
            stack.pop()
        elif len(stack) == 0 or arr[i] != stack[-1]:
            stack.append(arr[i])

    print(f'#{tc} {len(stack)}')


