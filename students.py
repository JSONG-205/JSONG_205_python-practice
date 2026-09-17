students = [
    {"name": "张三", "age": 20, "score": 85},
    {"name": "李四", "age": 21, "score": 92},
    {"name": "王五", "age": 19, "score": 78},
    {"name": "赵六", "age": 22, "score": 60},
    {"name": "钱七", "age": 20, "score": 55}
]

# 1. 找最高分（打擂台）
top = students[0]
for s in students:
    if s['score'] > top['score']:
        top = s
print(f"最高分：{top['name']} {top['score']}")

# 2. 平均分
total = 0
for s in students:
    total += s['score']
print(f"平均分：{total / len(students):.1f}")

# 3. 及格人数
pass_count = 0
for s in students:
    if s["score"] >= 60:
        pass_count += 1
print(f"及格人数：{pass_count}")

# 4. 不及格名单
failed = []
for s in students:
    if s["score"] < 60:
        failed.append(s["name"])
print(f"不及格：{failed}")