# Day 09 · 字符串

> 日期：2026-09-19（周六）｜ 用时：约 2.5h ｜ 状态：✅ 完成

---

## 今天做到了什么

- [x] 字符串的索引和切片（和列表一样）
- [x] 理解"字符串不可变"
- [x] `upper / lower` 大小写
- [x] `strip` 去首尾空白
- [x] `split` 拆分字符串
- [x] `join` 合并列表成字符串
- [x] `replace` 替换
- [x] `startswith / endswith` 判断开头结尾
- [x] `find / count` 查找和计数
- [x] f-string 进阶格式（精度、宽度、千分位、百分比）
- [x] 完成 10 道字符串练习

**里程碑**：字符串系统学完。后面处理数据，80% 的时间都在跟字符串打交道。

---

## 核心概念

### 1. 字符串的索引和切片

**和列表一模一样**，因为字符串就是"字符的列表"。

```python
s = "Python"
#    012345

s[0]      # 'P'
s[1]      # 'y'
s[-1]     # 'n'（最后一个）
s[1:4]    # 'yth'（下标 1、2、3）
s[:3]     # 'Pyt'
s[3:]     # 'hon'
s[::-1]   # 'nohtyP'（反转）
```

**数位的时候空格也算：**

```
H  e  l  l  o     W  o  r  l  d
0  1  2  3  4  5  6  7  8  9  10
```

### 2. 字符串不可变（重点）

```python
s = "Python"
s[0] = "J"       # ❌ TypeError: 'str' object does not support item assignment
```

**字符串不能改单个字符！** 想要改，只能重建：

```python
s = "J" + s[1:]    # 'Jython'
```

**所有字符串方法都返回新字符串，原字符串不动：**

```python
s = "  hello  "
s.strip()          # 返回 'hello'，但 s 本身还是 "  hello  "
```

**对比列表：**

| | 列表 | 字符串 |
|---|---|---|
| 能改吗 | ✅ `lst[0] = x` | ❌ 不能改 |
| 方法效果 | 原地修改（如 `append`） | 返回新字符串 |
| 处理方式 | 直接改 | 用变量接返回值 |

### 3. `upper() / lower()` —— 大小写

```python
s = "Hello World"
s.upper()      # 'HELLO WORLD'
s.lower()      # 'hello world'
```

**用途**：用户输入不区分大小写时：

```python
cmd = input("输入命令：")
if cmd.lower() == "quit":
    print("退出")
```

### 4. `strip()` —— 去首尾空白

```python
s = "  hello  \n"
s.strip()       # 'hello'（去两端空格和换行）
s.lstrip()      # 'hello  \n'（只去左）
s.rstrip()      # '  hello'（只去右）
```

**⚠️ 关键**：`strip()` 不改变原字符串，返回新字符串。

```python
s = "  hello  "
print(len(s.strip()))    # 5（去空格后的长度）
print(len(s))            # 11（原长度）
print(s.strip())         # hello
```

**用途**：用户输入经常带多余空格：

```python
name = input("姓名：").strip()
```

### 5. `split()` —— 拆分字符串

```python
s = "apple,banana,orange"
s.split(",")     # ['apple', 'banana', 'orange']

s2 = "hello world foo"
s2.split()       # ['hello', 'world', 'foo']（默认按空格拆）
```

**用途**：处理 CSV、日志。

```python
line = "2026-09-19,张三,85,90,78"
parts = line.split(",")
print(parts[0])       # 2026-09-19
print(parts[1])       # 张三
print(parts[2:])      # ['85', '90', '78']
```

### 6. `join()` —— 合并列表成字符串

```python
fruits = ["apple", "banana", "orange"]
",".join(fruits)       # 'apple,banana,orange'
"-".join(fruits)       # 'apple-banana-orange'
"".join(fruits)        # 'applebananaorange'
```

**用法**：`分隔符.join(列表)`

**⚠️ join 是"分隔符"调用，不是列表调用：**

```python
",".join(fruits)       # ✅
fruits.join(",")       # ❌
```

**记忆**：**分隔符在前，列表在后。**

### 7. `replace()` —— 替换

```python
s = "I like cats"
s.replace("cats", "dogs")    # 'I like dogs'
s.replace(" ", "")           # 'Ilikedogs'（去掉所有空格）
```

**用途**：清洗数据（去空格、去特殊符号）。

**⚠️ 返回新字符串，原字符串不变：**

```python
s = "I like cats"
s.replace("cats", "dogs")     # 返回 'I like dogs'
print(s)                       # 还是 'I like cats'

s = s.replace("cats", "dogs") # 要用变量接
print(s)                       # 现在才是 'I like dogs'
```

### 8. `startswith() / endswith()` —— 判断开头结尾

```python
s = "hello.py"
s.startswith("hello")   # True
s.endswith(".py")       # True
s.endswith(".txt")      # False
```

**用途**：判断文件类型、URL 前缀。

```python
files = ["report.pdf", "data.csv", "notes.txt"]
for f in files:
    if f.endswith(".csv"):
        print(f)              # data.csv
```

### 9. `find() / count()` —— 查找和计数

```python
s = "hello world"
s.find("o")          # 4（第一次出现的下标）
s.find("z")          # -1（找不到返回 -1，不报错）
s.count("l")         # 3
s.count("z")         # 0（找不到返回 0）
```

**对比：**

| 方法 | 找不到时 | 返回 |
|---|---|---|
| `s.find("z")` | 返回 `-1` | 下标或 -1 |
| `s.index("z")` | **报错 ValueError** | 下标 |
| `s.count("z")` | 返回 `0` | 次数 |

**⚠️ 大坑**：`if s.find("e"):` 不能用！

因为 `find` 返回 -1 时，`-1` 也是"真值"，会误判为"找到了"。

```python
if s.find("e"):        # ❌ 有 bug
if "e" in s:           # ✅ 推荐
if s.find("e") != -1:  # ✅ 也可以
```

### 10. `in` —— 判断子串在不在

```python
"py" in "python"       # True
"Py" in "python"       # False（大小写敏感）
"z" in "python"        # False
```

### 11. f-string 进阶格式

```python
name = "张三"
score = 92.567
count = 1234567
rate = 0.856
```

| 写法 | 作用 | 输出 |
|---|---|---|
| `f"{score:.2f}"` | 保留 2 位小数 | `92.57` |
| `f"{score:.0f}"` | 取整 | `93` |
| `f"{count:,}"` | 千分位 | `1,234,567` |
| `f"{rate:.1%}"` | 百分比 1 位小数 | `85.6%` |
| `f"{rate:.2%}"` | 百分比 2 位小数 | `85.60%` |
| `f"{name:>10}"` | 右对齐宽 10 | `        张三` |
| `f"{name:<10}"` | 左对齐宽 10 | `张三        ` |
| `f"{name:^10}"` | 居中宽 10 | `   张三   ` |
| `f"{x:010.2f}"` | 补零宽 10，2 位小数 | `0000092.57` |

**格式说明符的完整结构：**

```python
f"{变量:[填充][对齐][宽度][.精度][类型]}"
```

| 部分 | 作用 | 例子 |
|---|---|---|
| 填充 | 用什么字符填充 | `0`、`*` |
| 对齐 | `<` 左 `>` 右 `^` 居中 | `<` |
| 宽度 | 总共占几个字符 | `10` |
| **.精度** | 小数点后几位 | `.2` |
| **类型** | `f` 小数、`%` 百分比、`,` 千分位 | `f` |

**⚠️ 记忆要点：**

- **精度前面必须有点**：`.2f`、`.1%`
- **宽度不需要点**：`10`、`^10`
- `.2` 不是"保留 2 位小数"，是"保留 2 位有效数字"

---

## 语法速查

### 索引和切片

```python
s[0]           # 第 1 个字符
s[-1]          # 最后 1 个
s[1:4]         # 下标 1、2、3
s[:3]          # 前 3 个
s[3:]          # 从 3 到结尾
s[::-1]        # 反转
```

### 常用方法

```python
s.upper()              # 全大写
s.lower()              # 全小写
s.strip()              # 去首尾空白
s.lstrip()             # 去左边
s.rstrip()             # 去右边
s.split(",")           # 按逗号拆成列表
",".join(lst)          # 用逗号合并列表
s.replace("a", "b")    # 替换
s.startswith("x")      # 以 x 开头？
s.endswith(".py")      # 以 .py 结尾？
s.find("x")            # 第一次出现的下标，找不到 -1
s.count("x")           # 出现次数
"x" in s               # 包含吗？
```

### f-string 格式

```python
f"{x:.2f}"             # 2 位小数
f"{x:,}"               # 千分位
f"{x:.1%}"             # 百分比 1 位小数
f"{x:^10}"             # 居中宽 10
f"{x:>10}"             # 右对齐宽 10
f"{x:<10}"             # 左对齐宽 10
```

---

## 今天的代码

**`day09_practice.py`**（10 道练习）

```python
# 练习 1：索引
s = "Python"
print(s[0])
print(s[-1])
print(s[:3])
print(s[3:])
print(s[::-1])

# 练习 2：大小写
s2 = "Hello World"
print(s2.upper())
print(s2.lower())
print("HELLO WORLD".lower() == s2.lower())

# 练习 3：去空白
s3 = "   hello   "
print(len(s3.strip()))
print(len(s3))
print(s3.strip())

# 练习 4：拆分
line = "2026-09-19,张三,85,90,78"
parts = line.split(",")
print(parts)
print(parts[0])
print(parts[1])
print(parts[2:])          # 注意下标：85 在 2

# 练习 5：合并
fruits = ["apple", "banana", "orange"]
print(",".join(fruits))
print("-".join(fruits))
print("".join(fruits))

# 练习 6：替换
s6 = "I like cats and cats are cute"
print(s6.replace("cats", "dogs"))
print(s6.replace(" ", ""))
print(s6.replace("I", "You"))

# 练习 7：开头结尾
files = ["report.pdf", "data.csv", "notes.txt", "image.png", "backup.csv"]
for f in files:
    if f.endswith(".csv"):
        print(f)
for f in files:
    if f.startswith("data"):
        print(f)
for f in files:
    if "e" in f:
        print(f)

# 练习 8：查找计数
s8 = "hello world, hello python, hello everyone"
print(s8.count("hello"))
print(s8.find("o"))
print(s8.find("z"))
print(s8.count("z"))

# 练习 9：综合处理
raw = "  apple , banana , orange ,  "
raw = raw.strip()
parts = raw.split(",")
cleaned = []
for item in parts:
    item = item.strip()
    if item:                  # 过滤空字符串
        cleaned.append(item)
print("-".join(cleaned))

# 练习 10：f-string 格式化
name = "张三"
score = 92.567
count = 1234567
rate = 0.856
print(f"{score:.2f}")
print(f"{count:,}")
print(f"{rate:.1%}")
print(f"{name:^10}")
```

---

## 踩坑记录

### 🐛 坑 1：`replace` 后原字符串没变

```python
s = "I like cats"
s.replace("cats", "dogs")     # 白调用了，返回值丢了
print(s)                       # 还是 "I like cats"
```

**原因**：字符串不可变，`replace` 返回新字符串。

**解法**：用变量接住返回值：

```python
s = s.replace("cats", "dogs")
```

**同类坑**：`strip`、`upper`、`lower`、`split` 都一样。

### 🐛 坑 2：`if s.find("e"):` 判断错误

```python
if s.find("e"):        # ❌ 有 bug
    print(s)
```

**原因**：`find` 返回下标或 -1，而 `-1` 是"真值"。

```python
if -1:
    print("会执行")    # 会执行！非 0 都是真
```

**解法**：

```python
if "e" in s:               # ✅ 推荐
if s.find("e") != -1:      # ✅ 也可以
```

### 🐛 坑 3：`for i in len(s)`

```python
for i in len(s):        # ❌ TypeError: 'int' object is not iterable
```

**原因**：`len` 返回整数，`for` 不能跟数字。

**解法**：

```python
for i in range(len(s)):    # ✅
for item in s:             # ✅ 更简洁
```

**⚠️ 这是第二次踩了**（Day 6 的 C3 也踩过），务必记牢。

### 🐛 坑 4：`f"{x:.2}"` 不是保留 2 位小数

```python
print(f"{92.567:.2}")      # 9.3e+01（科学计数法！）
```

**原因**：`.2` 是"保留 2 位有效数字"，不是小数。

**解法**：加 `f` 表示定点小数：

```python
print(f"{92.567:.2f}")     # 92.57
```

### 🐛 坑 5：`f"{x:1%}"` 不是百分比 1 位小数

```python
print(f"{0.856:1%}")       # 85.600000%（1 是宽度，不是精度）
```

**原因**：`1` 是字段宽度，不影响小数位。

**解法**：用 `.1%`：

```python
print(f"{0.856:.1%}")      # 85.6%
```

**规律**：**精度前面必须有点，宽度不需要。**

### 🐛 坑 6：`join` 谁调用搞反

```python
fruits.join(",")           # ❌ AttributeError
",".join(fruits)           # ✅
```

**记忆**：**分隔符在前，列表在后。**

---

## 自检清单

- [x] 字符串索引和切片，和列表一样
- [x] 字符串不可变，方法返回新字符串
- [x] 会 `upper / lower / strip`
- [x] 会 `split / join`
- [x] 会 `replace / startswith / endswith`
- [x] 会 `find / count`，知道找不到时的返回值
- [x] 知道 `if s.find("e"):` 有 bug，要用 `in`
- [x] 知道 `for i in range(len(s))` 或直接遍历元素
- [x] f-string 格式：`.2f` 保留小数、`.1%` 百分比、`,` 千分位
- [x] 知道格式说明符的"点"不能省

---

## 一句话记住

> **字符串不可变，方法返回新字符串；**
> **`split` 拆、`join` 合（分隔符在前）；**
> **`find` 找不到 -1、`count` 找不到 0；**
> **f-string 精度前面必须有点：`.2f`、`.1%`。**

---

## 明天预告

**Day 10 · 文件读写**

- `open()` 读写 txt
- `with` 语句
- 模式 r / w / a
- `encoding="utf-8"` 防乱码

产出：txt 读写程序

---

## 本地状态

| 项目 | 状态 |
|---|---|
| `day09_practice.py` | ✅ 已创建，10 道练习全过 |
| commit | ✅ `ald43ac` |
| push | ⏳ 网络问题，待重试 |

**明天开工第一件事：**

```bash
cd D:\dev\python-practice
git status
git push
```
