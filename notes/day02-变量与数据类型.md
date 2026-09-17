# Day 02 · 变量与数据类型

> 日期：2026-09-03（周四） ｜ 用时：2h ｜ 状态：✅ 完成

---

## 今天做到了什么

- [x] 理解变量的本质与命名规则
- [x] 掌握 str / int / float / bool 四种类型
- [x] 会用 `input` 接收输入、`print` 格式化输出
- [x] 掌握类型转换，理解为什么 `input` 的结果要转
- [x] 完成三个练习脚本

---

## 核心概念

### 变量 = 贴了标签的盒子

```python
name = "张三"
age = 20
```

`=` 不是"等于"，是**把右边的值装进左边的盒子**。

**命名三条铁律：**
1. 只能用字母、数字、下划线，**不能用数字开头**
2. **区分大小写**：`age` 和 `Age` 是两个不同变量
3. 不能用 Python 关键字（`print`、`if`、`for` 等）

### 四种基础类型

| 类型 | 英文 | 例子 | 说明 |
|---|---|---|---|
| 字符串 | str | `"张三"` | **必须加引号** |
| 整数 | int | `20` | 不带小数 |
| 浮点数 | float | `3.14` | 带小数 |
| 布尔 | bool | `True` / `False` | **首字母大写** |

### 💥 新手第一大坑：数字和字符串是两回事

```python
"20" + "20"   →  "2020"    # 字符串拼接
20 + 20       →  40        # 数字相加
"20" + 20     →  💥 TypeError
```

> **引号里的都是文字**，哪怕长得像数字。

### 💥 新手第二大坑：input 拿到的永远是字符串

```python
age = input("请输入年龄：")   # 输入 20，age 是 "20"
print(age + 1)                # 💥 报错
```

---

## 语法速查

### 类型转换

| 函数 | 作用 | 例子 |
|---|---|---|
| `int(x)` | 转成整数 | `int("20")` → `20` |
| `float(x)` | 转成小数 | `float("3.14")` → `3.14` |
| `str(x)` | 转成字符串 | `str(20)` → `"20"` |

紧凑写法：`age = int(input("请输入年龄："))`

### f-string（最推荐的输出方式）

```python
name = "张三"
age = 20
print(f"我叫{name}，今年{age}岁")
```

**字符串前加 `f`，变量扔进 `{}`** —— 不管什么类型都不用管转换，Python 自动处理。

### 控制小数位数

```python
print(f"{3.14159:.2f}")    # 3.14（保留 2 位）
print(f"{3.14159:.1f}")    # 3.1（保留 1 位）
print(f"{3.14159:.0f}")    # 3（不保留）
```

### 查看类型

```python
type(name)    →  <class 'str'>
type(age)     →  <class 'int'>
```

---

## 今天的代码

**`intro.py`** —— 自我介绍

```python
name = input("请输入你的名字：")
age = int(input("请输入你的年龄："))
city = input("请输入你的城市：")

print(f"我叫{name}，今年{age}岁，来自{city}")
```

**`calc.py`** —— 四则运算

```python
a = float(input("请输入第一个数字："))
b = float(input("请输入第二个数字："))

print(f"和为{a+b:.2f}")
print(f"差为{a-b:.2f}")
print(f"积为{a*b:.2f}")
print(f"商为{a/b:.2f}")
```

> 💡 用 `float` 而不是 `int`，这样 `3.5 + 2.1` 也能算，不会被截断。

**`bmi.py`** —— BMI 计算

```python
height = float(input("请输入身高（米）："))
weight = float(input("请输入体重（公斤）："))
bmi = weight / (height ** 2)
print(f"你的BMI为{bmi:.1f}")
```

> `**` 表示次方：`height ** 2` 就是身高平方。

---

## 踩坑记录

### ❌ 坑 1：TypeError 类型拼接

```
TypeError: can only concatenate str (not "int") to str
```

**原因**：用 `+` 拼接字符串时，混进了整数。

```python
print("我叫" + name + "，今年" + age + "岁")   # ❌ age 是 int
```

**三种解法：**

```python
# 解法 1：临时转字符串
print("我叫" + name + "，今年" + str(age) + "岁")

# 解法 2：用逗号（自动处理类型、自动加空格）
print("我叫" + name + "，今年", age, "岁")

# 解法 3：f-string（⭐ 最推荐）
print(f"我叫{name}，今年{age}岁")
```

### ❌ 坑 2：SyntaxError 语法错误

**原因**：中文标点混进代码。

| 错误 | 正确 |
|---|---|
| 中文引号 `""` | 英文引号 `""` |
| 中文冒号 `：` | 英文冒号 `:` |
| 中文括号 `（）` | 英文括号 `()` |

> **写 Python 时输入法保持英文状态，标点全部用英文半角。**

### ⚠️ 坑 3：PEP 8 格式警告

```
E225 missing whitespace around operator
```

**原因**：`=` 两边没加空格。

```python
name=input("...")      # ❌
name = input("...")    # ✅
```

**一键修复**：PyCharm 里按 **`Ctrl + Alt + L`** 自动格式化整个文件。

> 为什么要在意？代码是给人看的。`total=price*qty+ship-discount` 挤成一团，`total = price * qty + ship - discount` 一眼看清结构。**PEP 8 是全世界 Python 程序员的通用规范。**

---

## 自检清单

- [x] 能说出 3 条变量命名规则
- [x] 能用 `type()` 判断变量类型
- [x] 知道 `input()` 的结果要转换才能计算
- [x] 会写 f-string 并控制小数位数

---

## 一句话记住

> **引号里的是文字，引号外的是数据。** 混在一起用，Python 就罢工。

---

## 明天预告

**Day 03 · 条件判断**
`if/elif/else`、比较与逻辑运算符、`=` 与 `==` 的区别、边界值测试。

产出：`bmi.py`升级版 / `judge.py` / `grade.py`
