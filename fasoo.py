nums = ["1-2-3-456789012","582845-385823","48572-39485-89012","4-5-2-593328484","4958-39-2945123-","49582039415423","7-3-7-000000000","485723-693812","39482746582734","1-1-1-111111111","A4944-5095-4951","4851293412223"]
temp = []
for i in range(len(nums)):
    cnt_num = 0
    cnt_dash = 0

    for j in range(len(nums[i])):
        # 규칙 1
        if not nums[i][j].isdecimal() and nums[i][j] != '-':
            break
        # 규칙 2
        if nums[i][j].isdecimal():
            cnt_num += 1
        # 규칙 3
        if nums[i][j] == '-':
            cnt_dash += 1
        # 규칙 4
        if nums[i][j] == '-':
            if j == 0 or j == len(nums[i])-1 or nums[i][j+1] == '-':
                break
    if cnt_dash > 3 or (11 > cnt_num or cnt_num > 14) or (j == 0 and nums[i][j] == '-') or nums[i][-1] == '-' or (nums[i][j] == '-' and  nums[i][j+1] == '-'):
        continue
    else:
        temp.append(nums[i])
print(temp)
form = []

for i in range(len(temp)):
    cnt = 0
    temp1 = []
    for j in range(len(temp[i])):
        if temp[i][j].isdecimal():
            cnt += 1
        elif temp[i][j] == '-':
            temp1.append(cnt)
            cnt = 0
        if j == len(temp[i])-1:
            temp1.append(cnt)
    form.append( [temp1, 0] )
print(form)
ans = []

while form:
    bank = 1
    compare = form[0]
    for j in range(1, len(form)):
        if compare == form[j] and compare[1] == 0:
            bank += 1
            form[j][1] = 1
        if compare[1] == 1:
            break
    if compare[1] == 0:
        ans.append(bank)
    del form[0]

print(ans)