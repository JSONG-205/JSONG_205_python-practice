# 四件事：
# #
# # 找出所有偶数 → 装进新列表
# # 找出所有大于 30的 → 装进新列表
# # 统计 20~50 之间（含 20 和 50）有几个
# # 从大到小排序输出

nums = [12, 45, 8, 33, 21, 60, 17, 99, 5, 40]
new_nums = []
for i in range(len(nums)):
    if nums[i]%2 == 0:
        new_nums.append(nums[i])
print(new_nums)

for i in range(len(nums)):
    if nums[i] > 30 :
        new_nums.append(nums[i])
print(new_nums)

count = 0
for i in range(len(nums)):
    if nums[i] > 20 and nums[i] < 50 :
        count += 1
print(count)

print(sorted(nums,reverse = True))
