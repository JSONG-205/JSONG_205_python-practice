import os

# 切换到本文件所在目录，保证下面的相对路径在任何位置运行都能找到
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("data/day10_test.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
    f.write("第三行\n")
# 第 1 种：read()
with open("data/day10_test.txt", "r", encoding="utf-8") as f:
    s1 = f.read()
print(s1)

# 第 2 种：readlines()
with open("data/day10_test.txt", "r", encoding="utf-8") as f:
    s2 = f.readlines()
print(s2)

# 第 3 种：逐行
with open("data/day10_test.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

with open("data/day10_test.txt", "r", encoding="utf-8") as f:
    s1 = f.read()
    print(s1)

    f.seek(0)              # 指针回到开头
    s2 = f.readlines()
    print(s2)

    f.seek(0)              # 再回到开头
    for line in f:
        print(line.strip())

with open("data/day10_test.txt","a",encoding="UTF-8") as f:
    f.write("第四行")
    f.seek(0)
with open("data/day10_test.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(line.strip())

scores = [85, 92, 78, 60, 55]
total = 0
count = 0
# 写
with open("data/scores.txt","w",encoding="utf-8") as f:
    for i in range(len(scores)):
        f.write(str(scores[i])+"\n")
with open("data/scores.txt","w",encoding="utf-8") as f:
    for i in scores:
        f.write(f"{i}\n")
with open("data/scores.txt","r",encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        total += int(line)
        count += 1
    print(f"平均分：{total / count:.1f}")  # 平均分：74.0
count = 0
str1 = []
with open("data/day10_test.txt","r",encoding="utf-8") as f:
    print(f.read())
    f.seek(0)
    for s in f:
        count += 1
        print(f"{count}:{s.strip()}")
    f.seek(0)
    for i,line in enumerate(f,start=1):
        str1.append(f"\n{i}:{line.strip()}")
        print(f"{i}:{line.strip()}")

with open("data/day10_test.txt", "r", encoding="utf-8") as f_in, \
     open("data/day10_copy.txt", "w", encoding="utf-8") as f_out:
    for i, line in enumerate(f_in, start=1):
        f_out.write(f"{i}: {line.strip()}\n")

























