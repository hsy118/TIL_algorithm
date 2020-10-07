def heappush(value):
    global heapcount
    heapcount += 1
    heap[heapcount] = value
    cur = heapcount
    parent = cur // 2

    # 루트가 아니고, if 부모노드값 > 자식노드 => swap
    while parent and heap[parent] > heap[cur]:
        heap[parent], heap[cur] = heap[cur], heap[parent]
        cur = parent
        parent = cur // 2


def heappop():
    global heapcount
    retValue = heap[1]
    heap[1] = heap[heapcount]
    heapcount -= 1
    heap[heapcount] = 0
    heapcount -= 1

    parent = 1
    child = parent * 2

    if child + 1 <= heapcount: #오른쪽 자식 존재
        if heap[child] > heap[child+1]:
            child = child + 1
    # 자식 노드가 존재하고, 부모 노드 > 자식노드 => swap
    while child <= heapcount and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2
        if child + 1 <= heapcount:  # 오른쪽 자식 존재
            if heap[child] > heap[child + 1]:
                child = child + 1
    return retValue

# 최소합
heapcount = 0
temp = [2,3,4,5,1,9,8]
N = len(temp)
heap = [0] * (N+1)
for i in range(N):
    heappush(temp[i])
heappop()
# for i in range(N):
#     print(heappop(), end=" ")
heappush(7)
heappop()
heappush(1)
print()
