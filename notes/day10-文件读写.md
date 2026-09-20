# Day 10 · 文件读写

> 日期：2026-09-20（周日）｜ 用时：约 3h ｜ 状态：✅ 完成

---

## 今天做到了什么

- [x] `open()` 基础用法
- [x] `with` 语句（自动关闭文件）
- [x] 三种模式：`r` / `w` / `a`
- [x] `encoding="utf-8"` 防乱码
- [x] 三种读法：`read()` / `readlines()` / 逐行
- [x] 两种写法：`write()` / `writelines()`
- [x] 文件指针概念（读一次走一次）
- [x] `seek(0)` 回到开头
- [x] `enumerate(序列, start=1)` 遍历时带序号
- [x] 完成 5 道练习

**里程碑**：数据能持久化了。程序重启后数据不丢——这是后面所有大数据处理的基础。

---

## 核心概念

### 1. 为什么需要文件读写

内存里的数据（列表、字典）**程序一关就没了**。想永久保存，就写到文件。

| 场景 | 需要文件读写 |
|---|---|
| 程序重启后数据不丢 | ✅ |
| 保存配置 | ✅ |
| 读取日志 | ✅ |
| 处理 CSV 数据 | ✅ |

**大数据的核心工作：读数据 → 处理 → 写结果。**

### 2. `with` 语句（推荐写法）

```python
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Hello")
```

**好处**：离开代码块时**自动关闭文件**。

| 写法 | 要不要 close |
|---|---|
| `f = open(...)` ... `f.close()` | 手动，容易忘 |
| `with open(...) as f:` | **自动，推荐** |

**口诀：文件操作一律用 `with`。**

### 3. 三个核心模式

```python
open("文件", "模式", encoding="utf-8")
```

| 模式 | 含义 | 文件不存在 | 文件已存在 |
|---|---|---|---|
| `"r"` | 读（默认） | ❌ 报错 | ✅ 读取 |
| `"w"` | 写 | ✅ 新建 | ⚠️ **清空重写** |
| `"a"` | 追加 | ✅ 新建 | ✅ 末尾追加 |

**⚠️ `"w"` 是危险模式**：打开就清空原内容。想保留原内容用 `"a"`。

### 4. `encoding="utf-8"` 防乱码

**中文一定要加。**

```python
# ❌ 可能乱码
with open("data.txt", "w") as f:
    f.write("你好")

# ✅ 保险写法
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("你好")
```

**原因**：Windows 默认 GBK，Linux/Mac 用 UTF-8，不加 `encoding` 换电脑读就乱码。

**口诀：凡是涉及中文，`encoding="utf-8"` 不能省。**

### 5. 读文件的三种方式

| 方法 | 返回 | 适合 |
|---|---|---|
| `f.read()` | 一个整字符串 | 小文件、配置文件 |
| `f.readlines()` | 列表，元素带 `\n` | 需要按行处理 |
| `for line in f` | 一行一行 | **大文件（推荐）** |

**`readlines()` 的元素带 `\n`**：

```python
['第一行\n', '第二行\n', '第三行\n']
```

**逐行读时用 `strip()` 去掉**：

```python
for line in f:
    print(line.strip())
```

### 6. 写文件的两种方式

```python
# write() —— 写字符串，不自动换行
f.write("第一行\n")
f.write("第二行\n")

# writelines() —— 写列表，也不自动换行
lines = ["第一行\n", "第二行\n"]
f.writelines(lines)
```

**⚠️ 都不会自动加 `\n`**，要自己写。

### 7. 文件指针（重点坑）

**文件有一个"读指针"，读一次往前走一次，不会自动回头。**

```python
with open("data.txt", "r", encoding="utf-8") as f:
    s1 = f.read()         # 读到末尾
    s2 = f.readlines()    # 从末尾读，返回 []
    for line in f:        # 从末尾读，什么都不输出
        print(line)
```

**改法 1：每次重新打开文件（推荐）**

```python
with open("data.txt", "r", encoding="utf-8") as f:
    s1 = f.read()

with open("data.txt", "r", encoding="utf-8") as f:
    s2 = f.readlines()
```

**改法 2：用 `seek(0)` 回到开头**

```python
with open("data.txt", "r", encoding="utf-8") as f:
    s1 = f.read()
    f.seek(0)              # 回到开头
    s2 = f.readlines()
```

**口诀：一个 `with` 里读操作只做一次。想再读，重开文件。**

### 8. `enumerate(序列, start=1)` —— 遍历带序号

**不用手写 `count += 1`**：

```python
fruits = ["apple", "banana", "orange"]

for i, f in enumerate(fruits, start=1):
    print(f"{i}: {f}")

# 输出：
# 1: apple
# 2: banana
# 3: orange
```

| 写法 | 序号 |
|---|---|
| `enumerate(lst)` | 0, 1, 2 |
| `enumerate(lst, start=1)` | 1, 2, 3 |

**遍历文件对象也能用**：

```python
with open("data.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}: {line.strip()}")
```

**原理**：`enumerate` 每次产出 `(序号, 元素)` 元组，`for i, x in ...` 拆包。

---

## 语法速查

### 打开文件

```python
with open("文件名", "模式", encoding="utf-8") as f:
    ...
```

### 读

```python
f.read()              # 整块字符串
f.readlines()         # 列表（元素带 \n）
for line in f:        # 逐行（推荐）
```

### 写

```python
f.write("内容\n")     # 写字符串
f.writelines(lst)     # 写列表
```

### 其他

```python
f.seek(0)             # 指针回到开头
line.strip()          # 去掉行尾的 \n
enumerate(lst, start=1)   # 遍历带序号
```

---

## 今天的代码

**`day10_practice.py`**

```python
# 练习 1：写文件
with open("day10_test.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
    f.write("第三行\n")

# 练习 2：三种读法
with open("day10_test.txt", "r", encoding="utf-8") as f:
    s1 = f.read()
print(s1)

with open("day10_test.txt", "r", encoding="utf-8") as f:
    s2 = f.readlines()
print(s2)

with open("day10_test.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# 练习 3：追加
with open("day10_test.txt", "a", encoding="utf-8") as f:
    f.write("第四行\n")

with open("day10_test.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# 练习 4：读 + 算平均
scores = [85, 92, 78, 60, 55]

with open("scores.txt", "w", encoding="utf-8") as f:
    for s in scores:
        f.write(f"{s}\n")

total = 0
count = 0
with open("scores.txt", "r", encoding="utf-8") as f:
    for line in f:
        total += int(line.strip())
        count += 1
print(f"平均分：{total / count:.1f}")

# 练习 5：文件复制加行号
with open("day10_test.txt", "r", encoding="utf-8") as f_in, \
     open("day10_copy.txt", "w", encoding="utf-8") as f_out:
    for i, line in enumerate(f_in, start=1):
        f_out.write(f"{i}: {line.strip()}\n")
```

**生成的文件：**

```
day10_test.txt     # 4 行内容
scores.txt         # 5 个分数
day10_copy.txt     # 带行号的复制
```

---

## 踩坑记录

### 🐛 坑 1：同一个 with 块连续读多次

```python
with open("data.txt", "r", encoding="utf-8") as f:
    s1 = f.read()
    s2 = f.readlines()    # []（指针已到末尾）
    for line in f:        # 什么都不输出
        print(line)
```

**原因**：文件指针读一次走一次。

**解法**：每个读操作用独立的 `with`，或 `f.seek(0)` 回开头。

**⚠️ 踩了两次**（练习 2 和练习 5 各一次）。

### 🐛 坑 2：`"a"` 模式下读文件

```python
with open("data.txt", "a", encoding="utf-8") as f:
    f.write("新内容")
    f.seek(0)
    for line in f:        # ❌ io.UnsupportedOperation: not readable
        print(line)
```

**原因**：`"a"` 只能写，不能读。

**解法**：读和写分开，用两个 `with`。

### 🐛 坑 3：`write()` 传入非字符串

```python
f.write(85)              # ❌ TypeError: write() argument must be str, not int
```

**解法**：用 f-string 转：

```python
f.write(f"{85}\n")
```

### 🐛 坑 4：`\n` 裸露在引号外

```python
f.write(str(scores[i])\n)     # ❌ SyntaxError
```

**解法**：转义字符必须在引号里：

```python
f.write(f"{scores[i]}\n")     # ✅
f.write(str(scores[i]) + "\n") # ✅
```

### 🐛 坑 5：`read()` 处理数据行不方便

```python
data = f.read()          # 一整块字符串
# data = "85\n92\n78\n"
# 还得自己拆
```

**解法**：处理数据用逐行读：

```python
for line in f:
    total += int(line.strip())
```

### 🐛 坑 6：`str` 当变量名

```python
str.append(...)          # ❌ AttributeError
```

**原因**：`str` 是内置类型，不是列表。

**解法**：换名字，如 `lines_out`。

**同类坑**：`int`、`list`、`sum`、`max`、`min` 都别当变量名。

### 🐛 坑 7：用 `"w"` 模式写两次

```python
with open("x.txt", "w") as f:
    f.write("A")

with open("x.txt", "w") as f:    # 又清空
    f.write("B")
# 最终只有 B
```

**原因**：`"w"` 打开就清空。

**解法**：想保留用 `"a"`，或合并成一次写。

---

## 自检清单

- [x] 知道 `with` 自动关闭文件
- [x] 知道 `r/w/a` 三个模式区别
- [x] 中文写入加 `encoding="utf-8"`
- [x] 会用 `read / readlines / for line in f`
- [x] 知道 `readlines` 元素带 `\n`
- [x] 会用 `write` 写文件
- [x] 知道文件指针读一次走一次
- [x] 会用 `seek(0)` 或重开文件再读
- [x] 会用 `enumerate(序列, start=1)`
- [x] 知道 `write()` 只收字符串
- [x] 知道 `\n` 要写在引号里
- [x] 知道 `str` 不能当变量名
- [x] 完成 5 道练习

---

## 一句话记住

> **文件操作一律用 `with`；中文加 `encoding="utf-8"`；**
> **`"w"` 清空、`"a"` 追加、`"r"` 读；**
> **一个 `with` 读一次，再读就重开；**
> **`enumerate` 遍历带序号，从 1 开始用 `start=1`。**

---

## 明天预告

**Day 11 · JSON 数据**

- `json.dumps()` 和 `json.loads()`
- 读写 JSON 文件
- JSON 与 Python 字典互转
- 为什么大数据离不开 JSON

产出：`data.json` 读写程序

---

## 附：当天工作记录（不属于课程笔记）

### 仓库状态（2026-09-20 19:40 核实）

- 最新提交：`5cc3989 feat: Day10 文件读写练习 5 道`
- 生成文件 `day10_test.txt` / `scores.txt` / `day10_copy.txt` 已随提交入库
- 工作区干净（`git status` 无输出）

### 待办

- `git push` 把本地 5 个提交推上去
- 更新 `大数据开发学习规划-每日清单.xlsx`：第 10 天日期改为 2026-09-20
- 目标：`day10_test.txt` / `scores.txt` / `day10_copy.txt` 属于运行时生成物，可考虑加入 `.gitignore`
