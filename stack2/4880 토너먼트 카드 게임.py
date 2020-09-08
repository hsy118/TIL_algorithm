def win(p1, p2):
    #a 승 True  패 False
    if p1 == 1 and p2 == 2:
        return False
    elif p1 == 1 and p2 == 3:
        return True
    elif p1 == 2 and p2 == 1:
        return True
    elif p1 == 2 and p2 == 3:
        return False
    elif p1 == 3 and p2 == 1:
        return False
    elif p1 == 3 and p2 == 2:
        return True
    else:
        return True

def f1(students):
    if len(students) < 2:
        return students[0]
    team1, team2 = [], []
    for i in range(len(students)):
        if i <= (len(students)-1)//2:
            team1.append(students[i])
        else:
            team2.append(students[i])
    s1 = f1(team1)
    s2 = f1(team2)
    if win(s1[0], s2[0]):
        return s1
    else:
        return s2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mans = list(map(int, input().split()))
    mans = [(key, value) for value, key in enumerate(mans)]
    result = f1(mans)
    print(f'#{tc} {result[1]+1}')
