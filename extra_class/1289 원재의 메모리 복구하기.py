# for tc in range(1, int(input())+1):
#     count = 0
#     flag = "0"
#     num = input()
#
#     for j in range(len(num)):
#         if num[j] != flag:
#             count += 1
#             flag = num[j]
#
#     print("#" + str(tc) + " " + str(count))
#=============================================
def convert(value, start):
    for i in range(start, len(arr)):
        arr1[i] = value

T = int(input())
for tc in range(T):
    arr = list(map(int, input()))
    arr1 = [0] * len(arr)
    cnt = 0

    if arr[0] == 1:
        cnt += 1
        arr1 = [1] * len(arr)

    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            continue

        if arr[i] == 1:
            convert(0, i+1)
        else:
            convert(1, i+1)
        cnt += 1
    print(f"{tc+1} {cnt}")
#======================================
