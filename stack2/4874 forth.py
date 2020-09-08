T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    stack = []

    for i in range(len(arr)):
        result = 0
        if arr[i] == "+":
            if len(stack) <= 1:
                status = 'error'
                break
            cal1 = stack.pop()
            cal2 = stack.pop()
            result = cal2 + cal1
            stack.append(result)
        elif arr[i] == "-":
            if len(stack) <= 1:
                status = 'error'
                break
            cal1 = stack.pop()
            cal2 = stack.pop()
            result = cal2 - cal1
            stack.append(result)
        elif arr[i] == "*":
            if len(stack) <= 1:
                status = 'error'
                break
            cal1 = stack.pop()
            cal2 = stack.pop()
            result = cal2 * cal1
            stack.append(result)
        elif arr[i] == "/":
            if len(stack) <= 1:
                status = 'error'
                break
            cal1 = stack.pop()
            cal2 = stack.pop()
            result = cal2 // cal1
            stack.append(result)
        elif arr[i] == ".":
            status = stack.pop()
        else:
            stack.append(int(arr[i]))

    if len(stack) != 0:
        status = "error"
    print(f'#{tc} {status}')