def change(n):
    line.append(numbering[n])
    ticket = lotto[n]
    lucky_guy = numbering[n]
    # 로또에 수만큼, 있던 자리 지우고, 자리 옮기고
    del line[n]
    line.insert((n - ticket), lucky_guy)
N = int(input())
# 표 리스트
lotto = list(map(int, input().split()))
# 학생 위치
numbering = list(range(1, N+1))
line = [1]
for i in range(1, N):
    if lotto[i] == 0:
        continue
    else:
        change(i)

for k in line:
    print(k, end=' ')
#===============
N = int(input())
student = list(range(1, N+1))
num = list(map(int, input().split()))
for i, e in enumerate(num):
    student.insert(i-e, student.pop(i))
for e in student:
    print(e, end=' ')