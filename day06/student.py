student = {
    "name": "赵俊淞",
    "age": 20,
    "city": "南京",
    "scores": {"语文": 85, "数学": 92, "英语": 78}
}

# 1. 打印基本信息
print(f"姓名：{student['name']}，年龄：{student['age']}，城市：{student['city']}")

# 2. 打印数学成绩（嵌套，两层）
print(f"数学：{student['scores']['数学']}")

# 3. 平均分
scores = student["scores"]
avg = sum(scores.values()) / len(scores)
print(f"平均分：{avg:.1f}")

# 4. 新增 grade
student["grade"] = "大二"

# 5. 改城市
student["city"] = "北京"

# 6. 遍历 items
for key, value in student.items():
    print(f"{key} = {value}")

# 7. get 取 phone
phone = student.get("phone", "未填写")
print(f"电话：{phone}")