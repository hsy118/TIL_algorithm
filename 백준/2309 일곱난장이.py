# 리스트로 키 받는다
arr = []
for i in range(9):
    arr.append(int(input()))
total = sum(arr)
# 키순서로 정렬
arr.sort()
for i in range(9):
    for j in range(9):
        # 중복되지 않게 찾기 위해
        if i == j:
            continue
        else:
            # 만약 총 키- 난쟁이 두명의 합이 100이면
            temp = arr[i] + arr[j]
            if total - temp == 100:
                # 그 두명 색출해서
                kill1 = arr[i]
                kill2 = arr[j]
# 마피아 사형
arr.remove(kill1)
arr.remove(kill2)
# 날이 밝고 선량한 시민이 이겼습니다
for i in arr:
    print(i)