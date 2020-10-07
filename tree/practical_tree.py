"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""

def pre_order(n):
    if n>0:
        print(n, end=' ')
        pre_order(ch1[n])
        pre_order(ch2[n])

def inorder(n):
    if n>0:
        inorder(ch1[n])
        print(n, end=' ')
        inorder(ch2[n])

def postorder(n):
    if n>0:
        postorder(ch1[n])
        postorder(ch1[n])
        print(n, end= ' ')

V = int(input())
E = V - 1
tree = [[0] * 3 for _ in range(V+1)]
edge = list(map(int, input().split()))
ch1 = [0] * (V+1)
ch2 = [0] * (V+1)

for i in range(E):
    n1, n2 = edge[i*2], edge[i*2 + 1]
    if ch1[n1] == 0:
        ch1[n1] = n2
    else:
        ch2[n1] = n2

pre_order(1)
print()
inorder(1)
print()
postorder(1)
