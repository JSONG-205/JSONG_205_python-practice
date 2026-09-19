#scores = [85, 92, 55, 78, 90]
# 1. 打印列表
# 2. 输出最高分、最低分、平均分（保留 1 位小数）
# 3. 把低于 60 的改成 60
# 4. 再打印一次，确认改成功
def average(lst):
    total = 0
    for n in lst:
        total += n
    return total / len(lst)

scores = [85,92,55,78,90]
print(scores)
print(f"最高分:{max(scores)}")
print(f"最低分:{min(scores)}")
print(f"平均分：{average(scores):.1f}")

for i in range(len(scores)):
    if scores[i] < 60:
        scores[i] = 60

print(f"调整后：{scores}")
print(f"排序后：{sorted(scores)}")