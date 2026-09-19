def find_top(students):
    """打擂台找最高分学生"""
    top = students[0]
    for s in students:
        if s["score"] > top["score"]:
            top = s
    return top


def average_score(students):
    """返回平均分"""
    total = 0
    for s in students:
        total += s["score"]
    return total / len(students)


def count_pass(students):
    """统计及格人数"""
    count = 0
    for s in students:
        if s["score"] >= 60:
            count += 1
    return count


def find_failed(students):
    """返回所有不及格的学生姓名列表"""
    failed = []
    for s in students:
        if s["score"] < 60:
            failed.append(s["name"])
    return failed


# 主流程
students = [
    {"name": "张三", "age": 20, "score": 85},
    {"name": "李四", "age": 21, "score": 92},
    {"name": "王五", "age": 19, "score": 78},
    {"name": "赵六", "age": 22, "score": 60},
    {"name": "钱七", "age": 20, "score": 55}
]

top = find_top(students)
print(f"最高分：{top['name']} {top['score']}")
print(f"平均分：{average_score(students):.1f}")
print(f"及格人数：{count_pass(students)}")
print(f"不及格：{find_failed(students)}")