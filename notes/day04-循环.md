# Day 04 · 循环（for / while）

> 日期：2026-09-05（周六） ｜ 用时：2h ｜ 状态：✅ 完成

---

## 今天做到了什么

- [x] 掌握 `for` + `range()`，`while` + `while True`
- [x] 理解 `break` 与 `continue` 的区别
- [x] 拿下**循环嵌套**（今天的难点）
- [x] 会用 `random` 生成随机数
- [x] 完成九九乘法表 + 猜数字游戏

**里程碑**：写出第一个真正"像游戏"的程序。从"打印一句话"到"能反复交互"，只用了 4 天。

---

## 核心概念

### for 循环：知道重复多少次时用

```python
for 变量 in 序列:
    重复执行的代码
```

### 🔑 range() 含头不含尾（头号坑）

| 写法 | 产生的数字 |
|---|---|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(1, 10, 2)` | 1, 3, 5, 7, 9（步长 2） |

```python
for i in range(1, 101):   # 实际是 1~100，不是 1~101
```

> **记法**：`range(a, b)` 从 a 开始，到 **b 的前一个**结束。

### while 循环：不知道重复多少次时用

```python
while 条件:
    条件成立就一直执行
```

**必须有让条件最终变 False 的出口**，否则死循环（卡死时按 `Ctrl + C`）。

### 嵌套循环：外层走一步，内层走一圈

```python
for i in range(1, 4):        # 外层走 3 步
    for j in range(1, 4):    # 每步内层走 3 圈
        print(i, j)
```

输出 9 行：`1 1 / 1 2 / 1 3 / 2 1 / 2 2 / 2 3 / 3 1 / 3 2 / 3 3`

> **类比时钟**：分针转一整圈（内层），时针才走一格（外层）。

---

## 语法速查

### break 与 continue

| 关键字 | 作用 |
|---|---|
| `break` | 立刻结束**整个循环**，跳到循环外 |
| `continue` | 跳过**这一轮**剩下的代码，进入下一轮 |

```python
for i in range(1, 11):
    if i == 5:
        break          # 输出 1 2 3 4，遇到 5 直接停

for i in range(1, 11):
    if i == 5:
        continue       # 输出 1 2 3 4 6 7 8 9 10，只跳过 5
```

### while True + break（猜数字这类场景的标准套路）

```python
while True:                  # 条件永远成立
    ...
    if 猜中了:
        break                # ← break 是唯一出口
```

> 适合"不知道要玩几轮"的场景。退出逻辑集中在 `break` 一处，比在 while 后面写条件更清楚。

### 随机数

```python
import random
secret = random.randint(1, 100)      # 生成 1~100 的随机整数
```

### print 不换行

```python
print("a")            # 输出 a 然后换行
print("a", end="")    # 输出 a，不换行
print("a", end="  ")  # 输出 a，后面跟两个空格
```

### 计数简写

```python
count += 1     # 等价于 count = count + 1
```

---

## 今天的代码

**`multiplication.py`** —— 九九乘法表

```python
for i in range(1, 10):           # 外层：行号 1~9
    for j in range(1, i + 1):    # 内层：第 i 行有 i 个算式
        print(f"{j}×{i}={i*j}", end="  ")
    print()                      # 一行结束，换行
```

**三个关键点：**
1. `range(1, 10)` 只到 9 —— 不是 `range(1, 9)`（会丢第 9 行）
2. 内层 `i + 1` —— 含头不含尾的正确写法。写 `range(1, i)` 会导致第 1 行空、第 9 行少一个
3. 内层 `end="  "` 不换行，外层空 `print()` 换行

**`guess.py`** —— 猜数字游戏（推荐写法）

```python
import random

secret = random.randint(1, 100)
count = 0

while True:
    num = int(input("来猜一个数（1-100）："))
    count += 1

    if num < secret:
        print("太小了")
    elif num > secret:
        print("太大了")
    else:
        print(f"猜对了！用了{count}次")
        break

    if count >= 7:
        print(f"机会用完了！答案是{secret}")
        break
```

---

## 踩坑记录

### 🐛 坑 1：次数检查写在比大小之前（同 Day03 的顺序类 bug）

```python
# ❌ 错误顺序
if count >= 7:
    print("机会用完了")
    break
if num < secret:      # 第 7 次根本走不到这里
    ...
```

**后果**：**第 7 次正好猜中，也会被告知"机会用完了"** —— 玩家明明赢了，程序说他输了。

**正确顺序**：**先判猜中，再判次数**

```python
if num < secret:
    ...
elif num > secret:
    ...
else:
    print("猜对了")
    break           # 猜中优先退出

if count >= 7:      # 只有没猜中才会走到这
    print("机会用完了")
    break
```

> 与 Day03 的 `BMI < 27.9 and BMI > 27.9` 是同一类问题：**语法合法、运行不报错、但结果错误。**

### 🐛 坑 2：无用变量

```python
flag = 1    # 定义了但从头到尾没用过
```

**危害**：让读代码的人困惑"这变量干嘛的"。**没用的变量就删掉。**

### 🐛 坑 3（Git 相关）：在 GitHub 网页上改文件导致 push 冲突

```
! [rejected] main -> main (fetch first)
```

**原因**：在 GitHub 网页上直接编辑/上传文件 → 远程产生了一次**本地没有的提交** → 两边历史分叉 → push 被拒绝。

**解法**：

```bash
git checkout --ours 文件名.py     # 保留本地版本
git add 文件名.py
git commit -m "merge: 保留本地版本"
git push
```

**根本预防**：

> ⚠️ **代码只从本地 git 命令推，不要在 GitHub 网页上改文件。网页只用来"看"，不用来"改"。**

**另记**：**永远不要用 `git push --force`** —— 它会把远程那些你本地没有的提交直接抹掉。

---

## 自检清单

- [x] `range(1, 10)` 循环几次？为什么？（答：9 次，含头不含尾）
- [x] 能说清 `break` 和 `continue` 的区别
- [x] 能解释"外层走一步、内层走一圈"
- [x] 知道嵌套循环里 `range(1, i+1)` 为什么是 i+1

---

## 一句话记住

> **`range(a, b)` 数到 b 的前一个；`break` 是 while True 唯一的出口。**

---

## 明天预告

**Day 05 · 列表 list**
创建与索引（从 0 开始）、切片 `[a:b]`、`append/insert/remove/pop`、`len/in`、`max/min/sum/sorted`、遍历并修改元素。

产出：`scores.py`（成绩管理）/ `shopping.py`（购物车）/ `numbers.py`（数字筛选）

> 列表 = JSON 里的数组，你之前理解过的概念，明天要用代码实现了。
