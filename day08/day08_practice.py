# -*- coding: utf-8 -*-
"""
day08_practice.py
C1: 算术函数（热身）
C2: 列表工具（重点，不许用 max/min/sum）
C3: 学生成绩系统（综合）
"""

# ==================== C1: 算术函数 ====================

def square(n):
    """返回 n 的平方"""
    return n * n


def cube(n):
    """返回 n 的立方"""
    return n * n * n


def power(n, exp=2):
    """返回 n 的 exp 次方，默认平方"""
    return n ** exp


# ==================== C2: 列表工具 ====================

def max_of(lst):
    """返回列表最大值"""
    if not lst:
        raise ValueError("空列表没有最大值")
    m = lst[0]
    for x in lst[1:]:
        if x > m:
            m = x
    return m


def min_of(lst):
    """返回列表最小值"""
    if not lst:
        raise ValueError("空列表没有最小值")
    m = lst[0]
    for x in lst[1:]:
        if x < m:
            m = x
    return m


def sum_of(lst):
    """返回列表求和"""
    total = 0
    for x in lst:
        total += x
    return total


def average_of(lst):
    """返回列表平均值"""
    if not lst:
        raise ValueError("空列表无法求平均")
    return sum_of(lst) / len(lst)


# ==================== C3: 学生成绩系统 ====================

def find_top(students):
    """找最高分的学生（字典）"""
    if not students:
        return None
    top = students[0]
    for s in students[1:]:
        if s["score"] > top["score"]:
            top = s
    return top


def find_low(students):
    """找最低分的学生（字典）"""
    if not students:
        return None
    low = students[0]
    for s in students[1:]:
        if s["score"] < low["score"]:
            low = s
    return low


def count_pass(students, threshold=60):
    """统计及格人数，默认及格线 60"""
    cnt = 0
    for s in students:
        if s["score"] >= threshold:
            cnt += 1
    return cnt


def find_by_score(students, min_score):
    """找分数 >= min_score 的所有学生姓名"""
    result = []
    for s in students:
        if s["score"] >= min_score:
            result.append(s["name"])
    return result


def class_report(students):
    """打印全班报告，内部调用上面 4 个函数，不重写逻辑"""
    top = find_top(students)
    low = find_low(students)
    passed = count_pass(students)          # 用默认 60
    above_90 = find_by_score(students, 90)

    print("===== 班级报告 =====")
    print(f"最高分：{top['name']} {top['score']}")
    print(f"最低分：{low['name']} {low['score']}")
    print(f"及格人数：{passed}")
    print(f"90分以上：{above_90}")


# ==================== 测试 ====================

if __name__ == "__main__":
    # C1 测试
    print("--- C1 ---")
    print(square(4))      # 16
    print(cube(3))        # 27
    print(power(2))       # 4
    print(power(2, 5))    # 32

    # C2 测试
    print("\n--- C2 ---")
    nums = [3, 1, 4, 1, 5, 9, 2, 6]
    print(max_of(nums))       # 9
    print(min_of(nums))       # 1
    print(sum_of(nums))       # 31
    print(average_of(nums))   # 3.875

    # C3 测试
    print("\n--- C3 ---")
    students = [
        {"name": "张三", "score": 85},
        {"name": "李四", "score": 92},
        {"name": "王五", "score": 78},
        {"name": "赵六", "score": 60},
        {"name": "钱七", "score": 55},
    ]
    class_report(students)