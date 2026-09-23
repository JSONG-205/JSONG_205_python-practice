# Day 11 · JSON 数据

> 日期：2026-09-23（周三）｜ 用时：约 3h ｜ 状态：✅ 完成

---

## 今天做到了什么

- [x] 理解 JSON 是什么、为什么需要
- [x] `json.dumps()` Python → JSON 字符串
- [x] `json.loads()` JSON 字符串 → Python
- [x] `json.dump()` 写到 JSON 文件
- [x] `json.load()` 从 JSON 文件读
- [x] `ensure_ascii=False` 中文正常显示
- [x] `indent=2` 格式化输出
- [x] 完成 5 道练习

**里程碑**：掌握了"数据持久化 + 跨语言交换"的标准格式。后面所有配置、API、数据交换都靠它。

---

## 核心概念

### 1. 为什么需要 JSON

列表、字典是 Python 的内存结构，**程序关掉就没了**。

存成文件需要"字符串化"，但 `str(dict)` 出来的不是标准格式：

```python
str({"name": "张三"})       # "{'name': '张三'}"  ← 单引号，别的语言读不了
```

**JSON 是跨语言的标准格式**——Python、Java、JavaScript 都能读。

| Python | JSON |
|---|---|
| `{"name": "张三"}` | `{"name": "张三"}` |
| 单双引号都行 | **只允许双引号** |
| `True` / `False` | `true` / `false` |
| `None` | `null` |

### 2. 四兄弟对照

| 方法 | 方向 | 跟谁打交道 | 参数 | 返回 |
|---|---|---|---|---|
| `dumps` | Python → JSON | **字符串** | 对象 | **字符串** |
| `dump` | Python → JSON | **文件** | 对象 + 文件 | None |
| `loads` | JSON → Python | **字符串** | 字符串 | **字典/列表** |
| `load` | JSON → Python | **文件** | 文件 | **字典/列表** |

**口诀**：

- **有 `s` 跟字符串，无 `s` 跟文件**
- **`d` 开头是写，`l` 开头是读**

### 3. `ensure_ascii=False` —— 中文显示

```python
json.dumps({"name": "张三"})
# '{"name": "\\u5f20\\u4e09"}'    ← 乱码

json.dumps({"name": "张三"}, ensure_ascii=False)
# '{"name": "张三"}'                ← 正常
```

**中文场景必须加。**

### 4. `indent=2` —— 格式化

```python
json.dumps(data, indent=2)
```

输出：

```json
{
  "name": "张三",
  "age": 20
}
```

**不加的话全挤一行。**

### 5. JSON 只有 6 种类型

| JSON | Python |
|---|---|
| object `{}` | dict |
| array `[]` | list |
| string `""` | str |
| number | int / float |
| boolean | bool |
| null | None |

**不能直接转的**：set、datetime、自定义类。需要先手动转成上面 6 种。

### 6. 能传 / 不能传

| 类型 | 能传？ | 说明 |
|---|---|---|
| dict / list / str / int / float / bool / None | ✅ | 直接转 |
| tuple | ⚠️ | 变成 array（读回来是 list） |
| set | ❌ | 需先 `list(set_data)` |
| datetime | ❌ | 需先 `str(dt)` |
| 自定义类 | ❌ | 需手动转 dict |

---

## 语法速查

```python
import json

# 转字符串
s = json.dumps(obj, ensure_ascii=False, indent=2)

# 解析字符串
d = json.loads(s)

# 写文件
with open("f.json", "w", encoding="utf-8") as f:
    json.dump(obj, f, ensure_ascii=False, indent=2)

# 读文件
with open("f.json", "r", encoding="utf-8") as f:
    d = json.load(f)
```

---

## 今天的代码

**`day11_practice.py`**（5 道练习）

```python
import json

# 练习 1：dumps 转字符串
student = {"name": "张三", "age": 20, "city": "南京"}
s = json.dumps(student, ensure_ascii=False)
print(s)
print(type(s))

# 练习 2：loads 转回字典
json_str = '{"name": "李四", "age": 21, "city": "北京"}'
data = json.loads(json_str)
print(data)
print(type(data))
print(data["name"])

# 练习 3：写到 JSON 文件
student_data = {
    "name": "王五",
    "age": 22,
    "scores": {"语文": 88, "数学": 95}
}
with open("student.json", "w", encoding="utf-8") as f:
    json.dump(student_data, f, ensure_ascii=False, indent=2)

# 练习 4：从 JSON 文件读
with open("student.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded["name"])
print(loaded["scores"]["数学"])
for k, v in loaded.items():
    print(f"{k} = {v}")

# 练习 5：列表转 JSON
students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78}
]

# 第 1 步：转字符串打印
json_str = json.dumps(students, ensure_ascii=False, indent=2)
print(json_str)

# 第 2 步：写到文件
with open("students.json", "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False, indent=2)

# 第 3 步：读回来
with open("students.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

# 第 4 步：遍历打印
for s in loaded:
    print(f"{s['name']} {s['score']}")
```

**生成的文件：**

```
student.json     # 单个学生（嵌套字典）
students.json    # 学生列表（列表套字典）
```

实测输出（已跑通，全部正确）：

```
{"name": "张三", "age": 20, "city": "南京"}
<class 'str'>
{'name': '李四', 'age': 21, 'city': '北京'}
<class 'dict'>
李四
{'name': '王五', 'age': 22, 'scores': {'语文': 88, '数学': 95}}
王五
95
name=王五
age=22
scores={'语文': 88, '数学': 95}
张三 85
李四 92
王五 78
```

**注意一个关键对比**：第 1 行 `json.dumps` 出来的字符串里是**双引号**（`"name": "张三"`），而第 3 行 `json.loads` 解析之后的 `print` 结果是**单引号**（`'name': '李四'`）。这不是 bug——前者是 JSON 格式的字符串，后者是 Python 字典被 `print` 出来的样子。**同一份数据，在不同阶段长相不同，这就是 JSON 和 Python 的分界线。**

---

## 踩坑记录

### 🐛 坑 1：`dump` 少了文件对象

```python
json.dump(student, ensure_ascii=False)      # ❌ 少了 f
json.dump(student, f, ensure_ascii=False)   # ✅
```

**`dump` 必须传两个参数：对象 + 文件对象。**

### 🐛 坑 2：`load` 参数写反

```python
json.load(new_student, f)          # ❌
new_student = json.load(f)         # ✅
```

**`load` 只接收文件对象，返回字典，用 `=` 接住。**

### 🐛 坑 3：单复数变量名混淆

```python
json.dump(student, f)      # student 是单个字典
json.dump(students, f)     # students 是列表
```

**写错不报错，但内容错。** 命名时要清楚。

### 🐛 坑 4：文件名混淆

```python
student.json       # 练习 3 的单个学生
students.json      # 练习 5 的学生列表
```

### 🐛 坑 5：`"a"` 模式导致 JSON 文件不合法

```python
with open("students.json", "a", ...)    # ❌ 追加，文件格式乱
with open("students.json", "w", ...)    # ✅ 重写
```

**JSON 文件必须用 `"w"`。**

### 🐛 坑 6：两个 `with` 嵌套用错

```python
with open("x.json", "w") as f_in:
    open("x.json", "w") as f_out:      # ❌ 少了 with
        ...
```

**同时打开两个文件用逗号，不嵌套。**

### 🐛 坑 7：`d.key` 访问字典

（Day 6 老坑重现）

```python
d.name         # ❌ 字典没有属性 name
d["name"]      # ✅ 字典用方括号
```

---

## 自检清单

- [x] 知道 JSON 是什么、为什么需要
- [x] 会 `dumps` 转字符串
- [x] 会 `loads` 解析字符串
- [x] 会 `dump` 写文件
- [x] 会 `load` 读文件
- [x] 知道 `dumps` 和 `dump` 的区别（有 s / 无 s）
- [x] 知道 `loads` 和 `load` 的区别
- [x] 会用 `ensure_ascii=False`
- [x] 会用 `indent=2`
- [x] 知道 JSON 只有 6 种类型
- [x] 完成 5 道练习

---

## 一句话记住

> **有 `s` 跟字符串，无 `s` 跟文件；**
> **`d` 开头是写，`l` 开头是读；**
> **中文加 `ensure_ascii=False`，格式加 `indent=2`；**
> **JSON 字符串必须双引号。**

---

## 明天预告

**Day 12 · 异常与调试**

- 常见异常类型（`TypeError` / `ValueError` / `KeyError` / `IndexError` / `FileNotFoundError`）
- `try / except`
- 看报错堆栈定位行号
- 故意制造并修复 5 种错误

产出：5 种错误修复练习

---

## 附：当天工作记录（不属于课程笔记）

### 仓库状态（2026-09-23 13:00 核实）

- 最新提交：`0205cc2 docs: 添加 Day10 文件读写笔记 + 更新知识点手册（Day01-10）`
- 本地与远程**完全同步**（Day 9/10/11 的提交都已推送，老大笔记里"3 个待推"的状态已过时）
- `day11_practice.py` 已暂存待提交
- **`.gitignore` 老大自己补了 Day10 测试文件和 Day11 的两个 json**，做得好 👍

### 实测校验

`day11_practice.py` 用 Python 3.13 跑了一遍，**输出与预期完全一致**，两道 JSON 文件读写、列表遍历都没问题。

### 待办

- `day11_practice.py` 提交（`.gitignore` 的改动也一起提）
- 更新 `大数据开发学习规划-每日清单.xlsx`：第 11 天日期改为 2026-09-23
- README 进度只到 Day09，Day10、Day11 两行没补
