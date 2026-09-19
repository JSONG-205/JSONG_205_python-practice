s1 = "Python"
print(s1[0])
print(s1[-1])
print(s1[:3])
print(s1[3:])
print(s1[::-1])
s2 = "Hello World"
print(s2.upper())
print(s2.lower())
print("HELLO WORLD".lower() == s2.lower())
s3 = "   hello   "
print(len(s3.strip()))
print(len(s3))
print(s3.strip())
# 4.拆分字符串
# 练习 4
line = "2026-09-19,张三,85,90,78"
parts = line.split(",")
print(parts)         # 全部
print(parts[0])      # 日期
print(parts[1])      # 姓名
print(parts[2:])     # 所有分数

# 练习 5：合并字符串
fruits = ["apple", "banana", "orange"]
s = ",".join(fruits)
print(s)
s = "-".join(fruits)
print(s)
s = "".join(fruits)
print(s)

#练习 6：替换
s = "I like cats and cats are cute"
new_s = s.replace("cat","dog")
print(new_s)
new_s = s.replace(" ","")
print(new_s)
new_s = s.replace("I","YOU")
print(new_s)
#继续练习 7：判断开头结尾
files = ["report.pdf", "data.csv", "notes.txt", "image.png", "backup.csv"]
for s in files:
    if s.endswith(".csv"):
        print(s)
for s in files:
    if s.startswith("data"):
        print(s)
for s in files:
    if "e" in s:
        print(s)
#练习 8
s = "hello world, hello python, hello everyone"
print(s.count("hello"))
print(s.find("o"))
print(s.find("z"))
print(s.count("z"))
#练习 9：综合处理
raw = "  apple , banana , orange ,  "
raw = raw.strip()
s = raw.split(",")
print(s)
ss = []
for i in s:
    ss.append(i.strip())
print(ss)
print("-".join(ss))

name = "张三"
score = 92.567
count = 1234567
rate = 0.856
print(f"{score:.2f}")
print(f"{count:,}")
print(f"{rate:.1%}")
print(f"{name:^10}")



