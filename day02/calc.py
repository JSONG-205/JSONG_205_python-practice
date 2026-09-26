def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


# 主流程
a = float(input("请输入第一个数字："))
b = float(input("请输入第二个数字："))

print(f"和为{add(a, b)}，差为{subtract(a, b)}，积为{multiply(a, b)}，商为{divide(a, b):.2f}")