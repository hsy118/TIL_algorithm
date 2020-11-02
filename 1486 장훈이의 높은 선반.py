"""
def dfs(idx, cur_sum):
    if idx == N:
        results.append(cur_sum)
        return
    dfs(idx + 1, cur_sum)
    cur_sum += shelves[idx]
    dfs(idx + 1, cur_sum)


T = int(input())
for t in range(1, T + 1):
    N, B = map(int, input().split())
    shelves = list(map(int, input().split()))
    results = []
    dfs(0, 0)
    min_result = abs(B - results[0])
    for result in results:
        if result >= B and abs(result - B) < min_result:
            min_result = abs(result - B)
    print('#{} {}'.format(t, min_result))
"""
#===================================================
def find(i, N, s, B): # i번 사람 고려, N 사람 수, s (i-1)사람까지 고려한 탑 높이, B 선반 높이
    if i == N: # 모든 사람에 대한 고려가 끝나면
        results.append(s)
        return
    else:
        find(i+1, N, s+workers[i], B) # i사람이 탑에 참여한 경우
        find(i+1, N, s, B) # i 사람이 참여하지 않는 경우

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    workers = list(map(int, input().split()))
    results = []
    find(0, N, 0, B)
    minV = results[0]
    for i in len(results):
        if results[i] >= B and i - B < minV:
            minV = i- B
    print(f"#{tc} {minV}")
