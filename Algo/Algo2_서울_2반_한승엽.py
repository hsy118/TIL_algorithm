
def find(t,s, i, N, M):
    # i 가 건너는 돌 인덱스 위치 , s가 (i-1)번 돌까지 고려한 점수 합
    if t == M:
        results.append(s)
        return
    else:
        if i+1 < N:
            find(t+1, s+arr[i], i+1, N, M) # i번째 돌
        if i+2 < N:
            find(t+1, s+arr[i+2], i+2, N, M) # i번 돌 X


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    results = []
    find(0,0, 0, N, M)
    maxV = 0
    for i in range(len(results)):
       if results[i] > maxV:
           maxV = results[i]
    print(maxV)