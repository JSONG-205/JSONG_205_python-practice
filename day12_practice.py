# age = int(input("年龄： "))
# print(f"你 {age} 岁")

# try:
#     age = int(input("年龄： "))
#     print(f"你 {age} 岁")
# except ValueError:
#     print("年龄必须是数字")

# a = float(input("第一个数："))
# b = float(input("第二个数："))
# print(a / b)

# a = float(input("第一个数："))
# b = float(input("第二个数："))
# try:
#     print(a / b)
# except ZeroDivisionError:
#     print("除数不能为 0")

# try:
#     with open("不存在的文件.txt", "r", encoding="utf-8") as f:
#         content = f.read()
# except FileNotFoundError:
#     print("文件不存在")

# d = {"name": "张三"}
# try:
#     print(d["age"])
# except KeyError:
#     print("键不存在")
#
# lst = [1, 2, 3]
# try:
#     print(lst[10])
# except IndexError:
#     print("下标越界")

try:
    a = float(input("第一个数："))
    b = float(input("第二个数："))
    print(f"结果：{a / b}")
except ValueError:
    print("输入必须是数字")          # ← 你填
except ZeroDivisionError:
    print("除数不能为 0")          # ← 你填
finally:
    print("程序结束")          # ← 你填
