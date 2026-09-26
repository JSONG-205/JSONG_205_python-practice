import json
import os

# 切换到本文件所在目录，保证下面的相对路径在任何位置运行都能找到
os.chdir(os.path.dirname(os.path.abspath(__file__)))


student = {
    "name": "张三",
    "age": 20,
    "city": "南京"
}

s = json.dumps(student,ensure_ascii=False,indent=2)
print(s)
print(type(s))

json_str = '{"name": "李四", "age": 21, "city": "北京"}'
s = json.loads(json_str)
print(s)
print(type(s))
print(s["name"])

student = {
    "name": "王五",
    "age": 22,
    "scores": {"语文": 88, "数学": 95}
}

student = {
    "name": "王五",
    "age": 22,
    "scores": {"语文": 88, "数学": 95}
}
with open("data/student.json","w",encoding="utf-8") as f_in:
    json.dump(student,f_in,ensure_ascii=False,indent=2)

# 练习 4
with open("data/student.json","r",encoding="utf-8") as f:
    new_student = json.load(f)
    print(new_student)
    print(new_student["name"])
    print(new_student["scores"]["数学"])
for key,value in new_student.items():
    print(f"{key}={value}")


# 练习 5
students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78}
]

# 第 1 步：转字符串打印
json_str = json.dumps(students, ensure_ascii=False, indent=2)
print(json_str)

# 第 2 步：写到文件
with open("data/students.json", "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False, indent=2)

# 第 3 步：读回来
with open("data/students.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

# 第 4 步：遍历打印
for s in loaded:
    print(f"{s['name']} {s['score']}")