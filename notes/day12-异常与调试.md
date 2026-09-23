# Day 12 · 异常与调试

> 日期：2026-09-23（周三）｜ 用时：约 2.5h ｜ 状态：✅ 完成

---

## 今天做到了什么

- [x] 理解"为什么需要异常处理"
- [x] 认识常见异常类型
- [x] `try / except` 基础语法
- [x] 多个 `except` 捕获不同类型
- [x] `finally` 无论如何都执行
- [x] 会看报错堆栈，定位到行
- [x] 亲手触发了 5 种异常
- [x] 完成 5 道练习

**里程碑**：程序不会因为一个错误直接崩掉，能优雅处理问题。这是所有生产级代码的基本要求。

---

## 核心概念

### 1. 为什么需要异常处理

**没有异常处理：**

```python
a = float(input("第一个数："))
b = float(input("第二个数："))
print(a / b)
```

输入 `b = 0`，程序**直接崩**：

```
ZeroDivisionError: division by zero
```

**有异常处理：**

```python
try:
    print(a / b)
except ZeroDivisionError:
    print("除数不能为 0")
```

程序**不崩**，给用户友好提示，继续往下跑。

### 2. 常见异常类型

| 异常 | 触发场景 | 例子 |
|---|---|---|
| `TypeError` | 类型不对 | `"abc" + 123` |
| `ValueError` | 值不对 | `int("abc")` |
| `NameError` | 变量不存在 | 用了未定义的变量 |
| `IndexError` | 下标越界 | `[1,2,3][10]` |
| `KeyError` | 键不存在 | `{"a":1}["b"]` |
| `AttributeError` | 方法/属性不存在 | `"abc".push()` |
| `ZeroDivisionError` | 除以 0 | `1 / 0` |
| `FileNotFoundError` | 文件不存在 | `open("没有.txt")` |

### 3. `try / except` 语法

```python
try:
    # 可能出错的代码
    危险操作
except 异常类型:
    # 出错后的处理
    处理代码
```

**执行流程：**

| 情况 | 结果 |
|---|---|
| `try` 里正常 | 跳过 `except`，继续往下 |
| `try` 里出错 | **跳过剩余代码**，跳到 `except` |
| `except` 处理完 | 继续执行 `try/except` 之后的代码 |

### 4. 多个 `except`

```python
try:
    a = float(input("第一个数："))
    b = float(input("第二个数："))
    print(f"结果：{a / b}")
except ValueError:
    print("输入必须是数字")
except ZeroDivisionError:
    print("除数不能为 0")
```

**从上到下匹配，命中第一个就跳出去。**

### 5. `finally` —— 无论如何都执行

```python
try:
    ...
except ValueError:
    ...
finally:
    print("程序结束")
```

**不管是否出错，`finally` 里的代码都执行。**

**典型用途**：关闭文件、释放资源、打印日志。

### 6. `except Exception as e` —— 兜底捕获

```python
try:
    ...
except Exception as e:
    print(f"出错了：{e}")
```

`Exception` 是所有异常的父类，能捕获所有。`e` 是具体的错误对象。

**不推荐在正式项目里用**（会吞掉所有错误，不好排查）。**只在调试时用。**

### 7. 看报错堆栈的三步

```
Traceback (most recent call last):
  File "day12_practice.py", line 9, in <module>
    age = int(input("年龄： "))
          ~~~~~^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: '阿斯顿发射点'
```

| 步骤 | 看什么 |
|---|---|
| 1 | **最后一行**：什么错（`ValueError`） |
| 2 | **倒数第二三行**：哪一行（`line 9`） |
| 3 | 打开文件跳到那一行 |

---

## 语法速查

### 基础结构

```python
try:
    ...
except 异常类型:
    ...
```

### 多个 except

```python
try:
    ...
except ValueError:
    ...
except ZeroDivisionError:
    ...
```

### 一个 except 多种异常

```python
try:
    ...
except (ValueError, ZeroDivisionError):
    print("输入有误")
```

### finally

```python
try:
    ...
except 异常类型:
    ...
finally:
    print("结束")
```

### 兜底

```python
try:
    ...
except Exception as e:
    print(f"错误：{e}")
```

### 看报错

```python
# 从最后一行读：什么错
# 倒数第二三行：哪一行
```

---

## 今天的代码

**`day12_practice.py`**

```python
# 练习 1：ValueError
# 裸写版（故意让它崩）
# age = int(input("年龄： "))
# print(f"你 {age} 岁")

try:
    age = int(input("年龄："))
    print(f"你 {age} 岁")
except ValueError:
    print("年龄必须是数字")

# 练习 2：ZeroDivisionError
# 裸写版
# a = float(input("第一个数："))
# b = float(input("第二个数："))
# print(a / b)

try:
    a = float(input("第一个数："))
    b = float(input("第二个数："))
    print(a / b)
except ZeroDivisionError:
    print("除数不能为 0")

# 练习 3：FileNotFoundError
# 裸写版
# with open("不存在的文件.txt", "r", encoding="utf-8") as f:
#     content = f.read()

try:
    with open("不存在的文件.txt", "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print("文件不存在")

# 练习 4：KeyError 和 IndexError
d = {"name": "张三"}
try:
    print(d["age"])
except KeyError:
    print("键不存在")

lst = [1, 2, 3]
try:
    print(lst[10])
except IndexError:
    print("下标越界")

# 练习 5：除法计算器（综合）
try:
    a = float(input("第一个数："))
    b = float(input("第二个数："))
    print(f"结果：{a / b}")
except ValueError:
    print("输入必须是数字")
except ZeroDivisionError:
    print("除数不能为 0")
finally:
    print("程序结束")
```

**练习 5 三种情况全部通过 ✅**

```
第一个数：10
第二个数：0
除数不能为 0
程序结束
```

---

## 踩坑记录

### 🐛 坑 1：异常类型写错，捕获不到

```python
try:
    x = int("abc")
except ZeroDivisionError:      # ❌ 类型不匹配
    print("出错了")
# 结果：还是崩，报 ValueError
```

**原因**：`int("abc")` 抛的是 `ValueError`，`except` 写 `ZeroDivisionError` 接不住。

**解法**：`except` 的类型要和实际抛出的**完全一致**。

### 🐛 坑 2：`try` 范围太小或太大

**范围太小**：出错行没包住。

```python
a = float(input("第一个数："))    # ← 在 try 外面
try:
    print(a / 0)
except ValueError:
    print("输入错")              # 接不住 ValueError
```

**范围太大**：把不该捕获的也包了。

**建议**：**只包可能出错的部分**，逻辑清晰。

### 🐛 坑 3：只捕获一种，漏了另一种

```python
try:
    a = float(input("第一个数："))
    b = float(input("第二个数："))
    print(a / b)
except ZeroDivisionError:      # 只处理除 0
    print("除数不能为 0")
```

**输入 `abc`** → `ValueError` 漏出去，程序崩。

**解法**：用多个 `except` 或 `except (ValueError, ZeroDivisionError)`。

### 🐛 坑 4：`finally` 里放返回值

```python
def f():
    try:
        return 1
    finally:
        return 2      # ← 会覆盖上面的 return，返回 2
```

**`finally` 里的 `return` 会覆盖 `try` 里的。**

**规则**：`finally` 只做"收尾"（关文件、打日志），**不要 `return`**。

### 🐛 坑 5：报错信息只看第一行

```
Traceback (most recent call last):    ← 这行没信息
  File "...", line 9                  ← 有用
    age = int(...)                    ← 有用
ValueError: invalid literal...        ← 最有用的在这
```

**从下往上读，最后一行才是根本原因。**

---

## 自检清单

- [x] 知道为什么要异常处理
- [x] 认识至少 5 种异常类型
- [x] 会用 `try / except`
- [x] 会用多个 `except` 捕获不同异常
- [x] 会用 `finally`
- [x] 知道 `except Exception as e` 的用途
- [x] 会看报错堆栈（最后一行 + 行号）
- [x] 亲手触发了 5 种异常
- [x] 完成 5 道练习

---

## 一句话记住

> **`try` 包危险代码，`except` 接错误，`finally` 做收尾；**
> **异常类型要对得上；**
> **看报错从最后一行读——什么错 + 哪一行。**

---

## 明天预告

**Day 13 · 模块与包**

- `import` 机制
- 标准库 `os / datetime / random`
- `pip` 安装第三方库
- `requirements.txt`

产出：用 `requests` 调用公开 API

---

## 附：当天工作记录（不属于课程笔记）

### 仓库状态（2026-09-23 17:15 核实）

- 最新提交：`bcd9c77 feat: Day11 JSON 数据练习 + 笔记 + 知识点手册更新`
- 本地与远程**完全同步**（`## main...origin/main` 无 ahead）——老大笔记里"Day 9/10/11/12 共 4 个待推"的信息已过时，Day 9~11 上一轮就推上去了
- `day12_practice.py` 已暂存待提交
- **`.gitignore` 里 `student.json` / `students.json` 老大自己已经补了**，笔记里那条"待补"可以划掉 👍

### 实测校验

用 Python 3.13 跑了练习 5（输入 `10` / `0`），输出：

```
第一个数：第二个数：除数不能为 0
程序结束
```

**与预期完全一致**，`except ZeroDivisionError` 正常接住，`finally` 正常执行。

### 待办

- `day12_practice.py` 提交推送
- 更新 `大数据开发学习规划-每日清单.xlsx`：第 12 天 → 2026-09-23 / 已完成
- README 进度只到 Day09，Day10~Day12 三行没补
