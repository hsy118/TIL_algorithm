
def push(item):
    global top
    if top > 100 - 1:
        return
    else:
        top += 1
        stack[top] = item

def pop():
    global top
    if top == 1:
        print("stack is Empty!")
        return
    else:
        result = stack[top]
        top -= 1
        return result

stack = [0] * 100
top = -1

push(1)
push(2)
push(3)
print(pop())
print(pop())
