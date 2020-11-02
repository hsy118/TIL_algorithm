"""
0.5 -1
0.25 -2
0.125 -3
0.0625 -4
"""
def bin(num):
    global result, cnt
    while True:
        next_num = num *2
        result += str(int(next_num))
        num = next_num - int(next_num)
        cnt += 1
        if num == 0.0:
            return
        if cnt > 13:
            return
"""
0.625

1.25 -- 1
1.25 - 1 = 0.25

0.5 
0
0.5

1.0
1
0.0

"""
T = int(input())
for tc in range(1, T+1):
    N = float(input())
    result = ''
    cnt = 0
    bin(N)
    if cnt > 13:
        print("#{} overflow".format(tc))
    else:
        print("#{} {}".format(tc, result))