def bfs(s, N):  #1~N번 노드가 존재하는 그래프 ㅏㅌㅁ색
    q = [s]   # 큐 생성, 시작점 enq
    v = [0] * (N+1)
    v[s] = 1 # 시작 노드 방문 표시
    while q:
        t = q.pop(0)
        #여기서 t 노드에 대한 처리

        for i in range(1, N+1):
            if adj[t][i]==1 and v[i]==0:
                q.append(i)
                v[i] = v[t] + 1 #  방문표시

