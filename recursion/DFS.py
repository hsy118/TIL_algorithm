# '''
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# '''
# def dfs(v):
#     # 방문체크
#     visited[v] = 1
#     print(v, end=' ')
#     # v의 인접한 정점 중에서 방문 안한 정점을 재귀 호출
#     for w in range(1, N+1):
#         if G[v][w] == 1 and visited[w] == 0:
#             dfs(w)
#
#
# #정점, 간선
# N, E = map(int, input().split())
# # 간선들...
# temp = list(map(int, input().split()))
# #인접 행렬
# G = [[0] * (N+1) for _ in range(N+1)]
# #방문체크
# visited = [0] * (N+1)
# #간선들을 인접행렬에 저장
# for i in range(E):
#     s, e = temp[2*i], temp[2*i+1]
#     G[s][e] = 1
#     G[s][e] = 1
#
# dfs(1)
#위에는 youtube로 한내용
#아래는 웹엑스
'''
7 8
1 2 1 3 2 4 2 5 3 5 4 6 5 6 6 7
'''
def dfs(s, V): # 반복구조의 깊이우선탑색
    # 초기화, 스택생성, visited[] 생성 및 초기화
    visited = [0]*(V+1) # visited[] 생성
    #stack = [s]  # 스택생성, 시작노드 push()
    stack = []
    stack.append(s) # push()
    visited[s] = 1
    while stack: # 스택이 비어있지 않으면 반복
        n = stack.pop() # 탐색할 노드 선택. pop()
        print(n)
        for i in range(1, V+1): # n에 인접하고 방문안한 노드 찾기
            if adj[n][i]==1 and visited[i] == 0: # i가 n에 인접하고 미방문이면
                stack.append(i)
                visited[i] = 1



V, E = map(int, input().split()) # V 정점 개수, E 간선 개수
adj = [[0]*(V+1) for _ in range(V+1)] # 인접행렬
tmp = list(map(int, input().split())) # E개의 간선 정보
for i in range(E): # 인접행렬 기록
    n1 = tmp[i*2]
    n2 = tmp[i*2+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1 # 무방향 그래프인 경우

dfs(1, V)
