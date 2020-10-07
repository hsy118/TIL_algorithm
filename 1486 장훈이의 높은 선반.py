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