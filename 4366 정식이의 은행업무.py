"""
1010
212

"""

T = int(input())
for tc in range(1, T+1):
    bin = list(input())
    tri = list(input())
    # 찾았을 때 1 아니면 0
    status = 0
    # 하나씩 바꿔보면서 계속 체크
    # 각 자리에 이진법은 2씩, 3진법은 3가지 경우의 수
    for i in range(len(bin)*2):
        #원본이 바뀌면 안되서
        new_bin = bin[:]
        # 자릿수 모든 경우의 수
        new_bin[i//2] = str(i % 2)
        # 비교를 위한
        a = ''.join(new_bin)
        for j in range(len(tri)*3):
            # 복사
            new_tri = tri[:]
            # 각 자릿수 경우의 수
            new_tri[j//3] = str(j%3)
            # 비교
            b = ''.join(new_tri)
            if int(a, 2) == int(b, 3):
                print("#{} {}".format(tc, int(a,2)))
                status = 1
                break
        # 찾고, 반복문 나가기 위한 상태 체크
        if status == 1:
            break
# print(0//3)
# print(1//3)
# print(2//3)
# print(3//3)
# print(4//3)
# print(2%3)
# print(1%3)
# a = [1,2,3]
# new_a = a[:]
# new_a.remove(1)
# print(new_a)
# print(a)

# print(int('11', 2))