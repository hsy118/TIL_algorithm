N = int(input())
campus = [[0]*100 for _ in range(100)]
points = [] # 튜플로 인풋 값을 받고
for _ in range(N):
    (a, b) = map(int, input().split())
    points.append((a,b))
# 인풋값들을 돌리면서 겹치면 걍 패스, 안겹치면 1 마크
for p in range(len(points)):
    for i in range(points[p][1], (points[p][1] + 10)):
        for j in range(points[p][0], (points[p][0]+10)):
            if campus[i][j] == 0:
                campus[i][j] = 1
# 1 마크된 애들 카운트
cnt = 0
for r in range(100):
    for c in range(100):
        if campus[r][c] == 1:
            cnt += 1
print(cnt)