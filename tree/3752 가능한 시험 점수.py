for tc in range(1, int(input())+1):
    N = int(input())
    score = list(map(int, input().split()))

    visit = [0] * (sum(score)+1)   # 마지막에 중복을 제거

    def dfs(k, s):
        if k == N:
            visit[s] = 1
        else:
            dfs(k+1, s)   # k번 문제를 틀린경우
            dfs(k+1, s + score[k])   # k번 문제 맞은 경우

    dfs(0, 0)
    print(f"#{tc} {sum(visit)}")
    #=============================
for tc in range(1, int(input())+1):
    N = int(input())
    score = list(map(int, input().split()))

    visit = [0] * (sum(score)+1)
    Q = [[0,0]]  # k, s
    while Q:
        k, s = Q.pop(0)
        if k == N:
            visit[s] = 1
        else:
            Q.append([k+1, s])
            Q.append([k+1, s+ score[k]])
    print(f"#{tc} {sum(visit)}")
    #=====================================
for tc in range(1, int(input()) + 1):
    N = int(input())
    score = list(map(int, input().split()))

    visit = [0] * (sum(score) + 1)

    Q = [0]

    for val in score:
        for i in range(len(Q)):
            if visit[Q[i] + val]: continue
            visit[Q[i] + val] = 1
            Q.append(Q[i] + val)
    ans = len(Q)
    print(f"#{tc} {ans}")