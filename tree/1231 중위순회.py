def in_order(n):
    global ans
    if n:
        in_order(tree[n][0])
        ans += letter[n]  # 왼쪽 자식에서 리턴을 받을 때
        in_order(tree[n][1])


for tc in range(1, 11):
    V = int(input())
    E = V - 1
    letter = [0] * (V+1)
    tree = [[0] * 2 for _ in range(V+1)]
    for i in range(V):
        # 인풋값을 배열로 만들고,
        temp = list(input().split())
        # letter 리스트에 인덱스에 맞게 알파벳 저장
        letter[int(temp[0])] = temp[1]
        # 자식이 두개 이상 인풋되면 저장
        if len(temp) > 3:
            tree[int(temp[0])][0] = int(temp[2])
            tree[int(temp[0])][1] = int(temp[3])
        # 자식이 한개만 인풋 되면 저장
        elif len(temp) == 3:
            tree[int(temp[0]) ][0] = int(temp[2])
    ans = ""  # 정답 모으기 위해
    in_order(1)
    print(f"#{tc} {ans}")

"""
        f(n)
        유효 노드면
        왼쪽 방ㅇ문
        오른쪽 방문
        
        if n <=V:  #마지막 노드번호 이내면
        f(n*2)
        t[n]
        f(n*2+1)
"""