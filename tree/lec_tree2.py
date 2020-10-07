"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""

def pre_order(node):
    global cnt
    if node:
        print(node, end=' ')
        cnt += 1
        pre_order(tree[node][0])
        pre_order(tree[node][1])

def inorder(node):
    if node:
        inorder(tree[node][0])
        print(node, end=' ')
        inorder(tree[node][1])

def postorder(node):
    if node:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end= ' ')

V = int(input())
E = V - 1
tree = [[0] * 3 for _ in range(V+1)]
temp = list(map(int, input().split()))
cnt = 0

for i in range(E):
    p, c = temp[i*2], temp[i*2 + 1]
    if tree[p][0] == 0:
        tree[p][0] = c
    else:
        tree[p][1] = c
    tree[c][2] = p

pre_order(1)
"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""