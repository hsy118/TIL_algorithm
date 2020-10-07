# 최소합만 지원
import heapq
heap = [7,2,5,3,4,6]  # list
heapq.heapify(heap)
print(heap)

heapq.heappush(heap, 1)
print(heap)

while heap:
    print(heapq.heappop(heap), end=" ")
print()
"""
        1
    3       2
  7   4    6   5

"""
temp = [7,2,5,3,4,6]
heap2= []
for i in range(len(temp)):
    heapq.heappush(heap2, (-temp[i], temp[i]] ))
heapq.heappush(heap2, (-1, 1))
print(heap2)
while heap2:
    print(heapq.heappop(heap2)[1], end=" ")
