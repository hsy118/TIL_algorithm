N = int(input()) #100
result = []

for i in range(1, N+1):
    check = 0
    i = str(i)
    for j in range(len(i)):
        if '3' in i[j]:
            check += 1
        if '6' in i[j]:
            check += 1
        if '9' in i[j]:
            check += 1
    if check == 1:
        i = '-'
    if check == 2:
        i = '--'
    result.append(i)
answer = ' '.join(result)
print(answer)
#====================================================
def check(num):
    digit = 0
    count = 0 # 3,6,9의 횟수
    while num:
        digit = num % 10
        num = num // 10
        if digit != 0 and digit % 3 == 0:
            count += 1
    return count


N = int(input())
for i in range(1, N+1):
    ans = check(i)

    if ans:
        for _ in range(ans):
            print("-", end="")
        print(" ", end="")
    else:
        print(i, end=" ")