# Day 05 · 列表 list

> 日期：2026-09-06（周日） ｜ 用时：2h ｜ 状态：✅ 完成

---

## 今天做到了什么

- [x] 理解列表的创建与索引（**下标从 0 开始**）
- [x] 掌握切片 `[a:b]`（含头不含尾）
- [x] 掌握增删改查：`append/insert/remove/pop/del`
- [x] 会用 `len/in/index` 查询
- [x] 掌握 `max/min/sum/sorted` 等常用函数
- [x] 拿下今天的**核心模式**：遍历列表并按下标修改元素

**里程碑**：接触第一个真正的数据结构。列表 = JSON 里的数组，之前理解过的概念，今天用代码实现了。

---

## 核心概念

### 索引：下标从 0 开始

```python
scores = [85, 92, 78, 90, 66]
#         0   1   2   3   4

scores[0]     →  85    # 第一个
scores[2]     →  78    # 第三个
scores[-1]    →  66    # 最后一个（负索引从尾部数）
scores[-2]    →  90    # 倒数第二个
```

> **下标最大是 `len(列表) - 1`**。`scores[5]` 会 `IndexError`（只有 5 个元素，下标 0~4）。

### 切片：含头不含尾（跟 range 同一套规则）

```python
scores[1:3]    →  [92, 78]      # 下标 1、2，不含 3
scores[:3]     →  [85, 92, 78]  # 从头到下标 2
scores[2:]     →  [78, 90, 66]  # 下标 2 到结尾
scores[:]      →  整个列表的副本
scores[::2]    →  [85, 78, 66]  # 步长 2，隔一个取一个
```

### 列表允许重复元素

```python
cart = ["苹果", "牛奶", "面包", "苹果"]    # 合法，两个苹果
```

**由此引出的坑**：`remove()` 只删除**第一个**匹配的。

```python
cart.remove("苹果")
print(cart)     # ['牛奶', '面包', '苹果']  ← 第二个苹果还在
```

> 想全部删掉得用循环，或者用**集合 set**（第 6 天学，自动去重）。

---

## 语法速查

### 增删改查

```python
# 增
scores.append(88)       # 末尾追加
scores.insert(1, 99)    # 在下标 1 处插入

# 删
scores.remove(92)       # 删除第一个值为 92 的元素
scores.pop()            # 删除并返回最后一个
scores.pop(0)           # 删除下标 0 的元素
del scores[0]           # 删除下标 0

# 改
scores[0] = 100         # 直接赋值

# 查
len(scores)             # 元素个数
92 in scores            # True/False，判断是否存在（最常用）
scores.index(92)        # 值为 92 的元素下标
scores.count(92)        # 92 出现了几次
```

### 常用函数

```python
max(scores)                  # 最高分
min(scores)                  # 最低分
sum(scores)                  # 总和
sum(scores)/len(scores)      # 平均分
sorted(scores)               # 返回新列表，原列表不变
scores.sort()                # 直接改原列表，返回 None
scores.reverse()             # 反转
```

### ⚠️ sorted() vs .sort()（今天的重点坑）

| 写法 | 作用 | 返回值 |
|---|---|---|
| `sorted(列表)` | 排序，**原列表不动** | 返回一个**新列表** |
| `列表.sort()` | 排序，**直接改原列表** | 返回 `None` |

```python
scores = [85, 92, 55, 78]

new = sorted(scores)
print(scores)     # [85, 92, 55, 78]  ← 原列表没变
print(new)        # [55, 78, 85, 92]  ← 新列表

scores.sort()
print(scores)     # [55, 78, 85, 92]  ← 原列表被改了

x = scores.sort()
print(x)          # None  ← 大坑！别这么写
```

**从大到小**（两个都加 `reverse=True`）：

```python
sorted(scores, reverse=True)
scores.sort(reverse=True)
```

> **口诀**：`sorted()` 有返回值要接；`.sort()` 没返回值别接。
> 判断方法：列表在括号里 → "给我一个排序版本"；列表在前面 → "你自己去排好"。

### 遍历的两种方式

```python
# 只要元素
for score in scores:
    print(score)

# 要下标 + 元素（enumerate）
for i, score in enumerate(scores):
    print(f"第{i+1}个：{score}")

# 需要按下标修改（必须用 range + len）
for i in range(len(scores)):
    scores[i] = ...
```

---

## 今天的代码

**`scores.py`** —— 成绩管理器

```python
scores = [85, 92, 55, 78, 90]

print(scores)
print(f"最高分：{max(scores)}")
print(f"最低分：{min(scores)}")
print(f"平均分：{sum(scores)/len(scores):.1f}")

# 把低于 60 的改成 60（今天的核心模式）
for i in range(len(scores)):
    if scores[i] < 60:
        scores[i] = 60

print(f"调整后：{scores}")
print(f"排序后：{sorted(scores)}")
```

输出：
```
[85, 92, 55, 78, 90]
最高分：92
最低分：55
平均分：80.0
调整后：[85, 92, 60, 78, 90]
排序后：[60, 78, 85, 90, 92]
```

**`shopping.py`** —— 购物车（核心是删除前先判断）

```python
cart = ["苹果", "牛奶", "面包"]

for i, item in enumerate(cart):
    print(f"{i+1}. {item}")

add = input("请输入要添加的商品：")
cart.append(add)

name = input("请输入要删除的商品：")
if name in cart:               # ← 先判断，否则 remove 会报错
    cart.remove(name)
    print(f"已删除{name}")
else:
    print("购物车里没有这个商品")

print(f"购物车：{cart}，共 {len(cart)} 件商品")
```

**`numbers.py`** —— 数字筛选

```python
nums = [12, 45, 8, 33, 21, 60, 17, 99, 5, 40]

# 筛选模式：空列表 + 循环 + 条件 + append
evens = []
for n in nums:
    if n % 2 == 0:
        evens.append(n)
print(evens)

big = []
for n in nums:
    if n > 30:
        big.append(n)
print(big)

# 计数模式
count = 0
for n in nums:
    if 20 <= n <= 50:          # 链式写法
        count += 1
print(count)

print(sorted(nums, reverse=True))
```

**正确答案：**

| 问题 | 答案 |
|---|---|
| 偶数 | `[12, 8, 60, 40]` |
| 大于 30 | `[45, 33, 60, 99, 40]` |
| 20~50 有几个 | **4 个**（45、33、21、40） |
| 从大到小 | `[99, 60, 45, 40, 33, 21, 17, 12, 8, 5]` |

---

## 三个必须记住的模式

### 模式 1：筛选（空列表 + append）

```python
result = []
for item in data:
    if 条件:
        result.append(item)
```

> 后面 pandas 的筛选、SQL 的 WHERE，本质都是这回事。

### 模式 2：计数

```python
count = 0
for item in data:
    if 条件:
        count += 1
```

### 模式 3：遍历并修改（必须按下标）

```python
for i in range(len(data)):
    if 条件:
        data[i] = 新值
```

> ⚠️ **不能写成 `for item in data: item = 新值`** —— 这样改的只是临时变量，列表本身不会变。这是新手高频错误。

---

## 踩坑记录

### 🐛 坑 1：remove 不存在的元素会崩

```python
cart.remove("西瓜")     # ValueError: list.remove(x): x not in list
```

**解法**：删除前先 `in` 判断（今天你做对了 ✅）

```python
if name in cart:
    cart.remove(name)
else:
    print("购物车里没有这个商品")
```

### 🐛 坑 2：sorted() 结果没接住

```python
sorted(scores)      # ❌ 白排，结果没保存
```

**解法**：`new = sorted(scores)` 或直接嵌进 print。

### 🐛 坑 3：把 .sort() 的返回值赋给变量

```python
x = scores.sort()
print(x)            # None
```

**解法**：`.sort()` 不用接，直接调用后原列表就变了。

### 🐛 坑 4（提前预告）：遍历中误改列表

```python
for item in data:
    if 条件:
        item = 新值      # ❌ 列表不会变
```

**解法**：用 `for i in range(len(data))` 按下标改。

---

## 自检清单

- [x] `list[1:3]` 取的是下标 1 和 2，不是 1、2、3
- [x] `append` 末尾追加；`insert` 指定位置插入
- [x] `sorted()` 返回新列表、原列表不变；`.sort()` 直接改原列表、返回 `None`
- [x] 下标从 0 开始，最大下标是 `len-1`

---

## 一句话记住

> **下标从 0 开始，切片含头不含尾，`sorted()` 要接、`.sort()` 别接。**

---

## 明天预告

**Day 06 · 字典 dict 与集合 set**
dict 键值读写、嵌套字典（对应 JSON 对象）、遍历 dict、元组 tuple、集合 set 去重。

产出：dict 练习 10 道 + 三层嵌套结构

> 字典 = JSON 里的对象 `{...}`，和列表一起构成 JSON 的两大结构。
