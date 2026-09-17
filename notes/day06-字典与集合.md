# Day 06 · 字典 dict 与集合 set

> 日期：2026-09-17（周四）｜ 用时：约 2.5h ｜ 状态：✅ 完成（正式收官）

---

## 今天做到了什么

- [x] 理解字典是什么，为什么需要它
- [x] 字典创建、取值、增、改、删
- [x] `[]` 和 `get()` 的区别
- [x] `in` 判断的是键，不是值
- [x] 嵌套字典取值（一层一层剥）
- [x] 列表套字典（Excel 表格形态）
- [x] `items()` / `keys()` / `values()` 遍历
- [x] 集合 set 去重：`list(set(...))`
- [x] 元组 tuple 认识
- [x] 三种核心模式：打擂台 / 计数器 / 筛选收集

**里程碑**：字典 = JSON 里的对象 `{...}`。到今天为止，JSON 的两大结构（数组、对象）你都在代码里实现了。

---

## 核心概念

### 1. 为什么需要字典？

列表存学生信息：

```python
student = ["赵俊淞", 20, "南京", 85]
```

三天后你回来看，问自己：`student[2]` 是城市还是成绩？**列表靠位置记数据，人脑记不住位置。**

字典靠**名字**记数据：

```python
student = {
    "name": "赵俊淞",
    "age": 20,
    "city": "南京"
}
```

**一句话：列表靠数，字典靠叫。**

### 2. 字典的结构

```python
student = {
    "name": "赵俊淞",     # ← 一对
    "age": 20
}
```

| 部分 | 例子 | 说明 |
|---|---|---|
| 键 key | `"name"` | 一般是字符串，必须唯一 |
| 值 value | `"赵俊淞"` | 任意类型 |
| 冒号 | `:` | 连接键和值 |
| 逗号 | `,` | 分隔每一对 |
| 花括号 | `{ }` | 整个字典 |

### 3. 取值：用键

```python
student = {"name": "赵俊淞", "age": 20}

student["name"]   # 赵俊淞
student["age"]    # 20
```

**列表用下标，字典用键。**

```python
names = ["赵俊淞", "张三"]
names[0]            # 靠位置
student["name"]     # 靠名字
```

### 4. `[]` vs `get()`——今天的第一个重点

```python
student = {"name": "赵俊淞", "age": 20}

student["city"]                    # ❌ KeyError: 'city'
student.get("city")                # ✅ None
student.get("city", "未知")         # ✅ "未知"
```

| 写法 | 键不存在时 | 适合场景 |
|---|---|---|
| `student["city"]` | **直接报错** | 确定一定有 |
| `student.get("city")` | 返回 `None` | 不确定有没有 |
| `student.get("city", "未知")` | 返回默认值 | 不确定，还想给退路 |

**为什么重要？** 大数据里读配置、读 JSON，字段经常缺。用 `[]` 会崩，用 `get()` 稳。

### 5. 增、改、删

```python
student = {"name": "赵俊淞", "age": 20}

student["grade"] = "大二"   # 增
student["age"] = 21         # 改
student.pop("grade")        # 删
del student["age"]          # 删（另一种写法）
```

**增和改写法一样，怎么区分？**

> 看这个键**以前有没有**。没有就是增，有就是改。

⚠️ **字典没有 `append`**（那是列表的方法）。字典新增 = 直接赋值。

### 6. 判断键在不在

```python
student = {"name": "赵俊淞", "age": 20}

"name" in student       # True
"city" in student       # False
```

⚠️ **`in` 判断的是键，不是值。**

```python
"赵俊淞" in student      # False！值不算

# 想判断值，用 values()
1 in student.values()    # 判断值
```

### 7. 长度

```python
len(student)    # 2，键值对的个数
```

### 8. 遍历字典

| 方法 | 拿到什么 | 场景 |
|---|---|---|
| `.items()` | (键, 值) 一对 | 遍历打印（推荐） |
| `.keys()` | 键 | 检查有哪些字段 |
| `.values()` | 值 | 求和、求平均 |

```python
# 推荐：items()
for key, value in student.items():
    print(f"{key}: {value}")

# 只要键
for key in student.keys():
    print(key)

# 只要值
for value in student.values():
    print(value)
```

### 9. 嵌套字典——对应 JSON 对象

```python
student = {
    "name": "赵俊淞",
    "scores": {              # ← 值是另一个字典
        "语文": 85,
        "数学": 92,
        "英语": 78
    }
}
```

**怎么取数学成绩？一层一层剥：**

```python
student["scores"]           # {"语文": 85, "数学": 92, "英语": 78}
student["scores"]["数学"]   # 92
```

理解方式：

```
先打开大袋子 → 再打开里面的小袋子 → 拿出东西
```

⚠️ **两个方括号并排，不是嵌套：**

```python
student["scores"]["数学"]    # ✅
student["scores"["数学"]]    # ❌ 括号位置错了
```

**为什么重要？** JSON 就是这个结构。以后读配置文件、调 API，全是套娃。

**字典套列表也常见：**

```python
product = {"tags": ["数码", "办公", "热销"]}
product["tags"][2]    # "热销"，先取键，再取列表下标
```

### 10. 列表套字典——数据集标准形态

```python
students = [
    {"name": "张三", "age": 20, "score": 85},
    {"name": "李四", "age": 21, "score": 92},
    {"name": "王五", "age": 19, "score": 78}
]
```

**像 Excel 表格：**

| 行 | name | age | score |
|---|---|---|---|
| 1 | 张三 | 20 | 85 |
| 2 | 李四 | 21 | 92 |
| 3 | 王五 | 19 | 78 |

每一行是字典，一堆行放进列表。

**取值：先定位到行，再拿字段。**

```python
students[1]           # {"name": "李四", "age": 21, "score": 92}
students[1]["score"]  # 92
```

**遍历：一行一行处理。**

```python
for s in students:
    print(f"{s['name']} 考了 {s['score']} 分")
```

⚠️ **f-string 引号冲突**：外层双引号，里面就用单引号。

```python
f"{s['name']}"    # ✅
f"{s["name"]}"    # ❌ 引号打架
```

### 11. 集合 set——自动去重

```python
nums = [1, 2, 2, 3, 3, 3]
unique = set(nums)
print(unique)    # {1, 2, 3}
```

**集合两大特点：**

1. **不重复**（自动去重）
2. **没顺序**（不能 `s[0]`）

**最常见的用法——去重：**

```python
tags = ["Python", "SQL", "Python", "Linux"]
unique = list(set(tags))   # 去重后变回列表
```

**记住这个组合：`list(set(...))` = 去重。**

**集合运算（了解即可）：**

```python
a = {1, 2, 3}
b = {2, 3, 4}

a | b   # 并集 {1, 2, 3, 4}
a & b   # 交集 {2, 3}
a - b   # 差集 {1}
```

### 12. 元组 tuple——认识即可

```python
point = (10, 20)
print(point[0])   # 10
point[0] = 5      # ❌ TypeError，不可变
```

| | 列表 list | 元组 tuple |
|---|---|---|
| 括号 | `[1, 2, 3]` | `(1, 2, 3)` |
| 可变 | ✅ 可以改 | ❌ 不能改 |
| 场景 | 数据会变 | 数据不会变（坐标、日期） |

### 13. `count()` —— 数元素出现几次

```python
tags = ["Python", "SQL", "Python", "Linux", "SQL", "Python"]

tags.count("Python")   # 3
tags.count("SQL")      # 2
tags.count("Java")     # 0（没有返回 0，不报错）
```

**和 `len` / `in` 的区别：**

| 写法 | 问什么 | 返回 |
|---|---|---|
| `len(tags)` | 一共几个？ | 数字 |
| `"Python" in tags` | 在不在？ | True / False |
| `tags.count("Python")` | 出现几次？ | 数字 |

⚠️ **`count` 是列表的方法，字典没有。**

---

## 四者对比速查

| 类型 | 括号 | 取值 | 可变 | 有序 | 主要场景 |
|---|---|---|---|---|---|
| 列表 list | `[...]` | `lst[0]` | ✅ | ✅ | 有序数据、遍历 |
| 字典 dict | `{k: v}` | `d["key"]` | ✅ | ✅ | 带字段的记录、JSON |
| 集合 set | `{...}` | 不能取 | ✅ | ❌ | 去重 |
| 元组 tuple | `(...)` | `t[0]` | ❌ | ✅ | 固定值 |

---

## 语法速查

### 字典

```python
d = {"name": "张三", "age": 20}

# 取值
d["name"]                  # 取值
d.get("phone")             # 不存在返回 None
d.get("phone", "未填写")    # 给默认值

# 增改删
d["grade"] = "大二"         # 增（不是 append！）
d["age"] = 21              # 改
d.pop("grade")             # 删
del d["age"]               # 删

# 判断与长度
"name" in d                # True（判断键，不是值）
len(d)                     # 键值对个数

# 遍历
for k, v in d.items():     # 键 + 值（推荐）
for k in d.keys():         # 只要键
for v in d.values():       # 只要值
```

### 集合

```python
set([1, 2, 2, 3])          # {1, 2, 3}
list(set(tags))            # 去重后变列表
a | b                      # 并集
a & b                      # 交集
a - b                      # 差集
```

### 列表补充

```python
lst.count(x)               # x 出现几次
lst.index(x)               # x 第一次出现的下标
```

---

## 三个核心模式（以后天天用）

### 模式 1：打擂台（找最大/最小）

```python
top = data[0]
for item in data:
    if item["field"] > top["field"]:
        top = item
```

⚠️ `top = item` 换的是**整个人**，不是只换字段。

### 模式 2：计数器

```python
count = 0
for item in data:
    if 条件:
        count += 1
```

### 模式 3：筛选收集

```python
result = []
for item in data:
    if 条件:
        result.append(item["field"])
```

> 这三个模式，pandas 的 groupby、SQL 的 WHERE、Spark 的 filter，本质都是它们。

---

## 今天的代码

**`student.py`** —— 字典基础 + 嵌套取值

```python
student = {
    "name": "赵俊淞",
    "age": 20,
    "city": "南京",
    "scores": {"语文": 85, "数学": 92, "英语": 78}
}

print(f"姓名：{student['name']}，年龄：{student['age']}，城市：{student['city']}")
print(f"数学：{student['scores']['数学']}")

scores = student["scores"]
avg = sum(scores.values()) / len(scores)
print(f"平均分：{avg:.1f}")

student["grade"] = "大二"
student["city"] = "北京"

for key, value in student.items():
    print(f"{key} = {value}")

phone = student.get("phone", "未填写")
print(f"电话：{phone}")
```

**`students.py`** —— 列表套字典 + 三种核心模式

```python
students = [
    {"name": "张三", "age": 20, "score": 85},
    {"name": "李四", "age": 21, "score": 92},
    {"name": "王五", "age": 19, "score": 78},
    {"name": "赵六", "age": 22, "score": 60},
    {"name": "钱七", "age": 20, "score": 55}
]

# 打擂台
top = students[0]
for s in students:
    if s['score'] > top['score']:
        top = s
print(f"最高分：{top['name']} {top['score']}")

# 累加
total = 0
for s in students:
    total += s['score']
print(f"平均分：{total / len(students):.1f}")

# 计数器
pass_count = 0
for s in students:
    if s["score"] >= 60:
        pass_count += 1
print(f"及格人数：{pass_count}")

# 筛选收集
failed = []
for s in students:
    if s["score"] < 60:
        failed.append(s["name"])
print(f"不及格：{failed}")
```

**`set_demo.py`** —— 集合去重 + 计数

```python
tags = ["Python", "SQL", "Python", "Linux", "SQL", "Hive", "SQL"]

unique_tags = list(set(tags))
print(f"不同标签：{len(unique_tags)} 个")
print(f"去重后：{unique_tags}")

for tag in unique_tags:
    count = tags.count(tag)
    print(f"{tag} 出现 {count} 次")
```

**`day06_practice.py`** —— 三道巩固练习

```python
# C1：商品字典
product = {
    "name": "笔记本电脑",
    "price": 5999,
    "stock": 12,
    "tags": ["数码", "办公", "热销"]
}
print(f"{product['name']} {product['price']}元")
print(product["tags"][2])
product["price"] = product["price"] * 0.9
print(f"折后价：{product['price']:.1f}")
product["brand"] = "联想"
print(product.get("color", "暂无颜色信息"))

# C2：订单列表
orders = [
    {"id": 1, "user": "张三", "amount": 120},
    {"id": 2, "user": "李四", "amount": 80},
    {"id": 3, "user": "王五", "amount": 250},
    {"id": 4, "user": "赵六", "amount": 45},
    {"id": 5, "user": "钱七", "amount": 300}
]

total = 0
for s in orders:
    total += s["amount"]
print(f"总金额：{total}")

print(f"平均金额：{total / len(orders):.1f}")

top = orders[0]
for s in orders:
    if s["amount"] > top["amount"]:
        top = s
print(f"最高：{top['user']} {top['amount']}")

count = 0
for s in orders:
    if s["amount"] >= 100:
        count += 1
print(f"大额订单：{count} 笔")

low_users = []
for s in orders:
    if s["amount"] < 100:
        low_users.append(s["user"])
print(f"小额订单用户：{low_users}")

# C3：标签统计
articles = [
    {"title": "文章A", "tags": ["Python", "SQL"]},
    {"title": "文章B", "tags": ["Python", "Linux"]},
    {"title": "文章C", "tags": ["SQL", "Hive", "SQL"]},
    {"title": "文章D", "tags": ["Python"]}
]

all_tags = []
for a in articles:
    for t in a["tags"]:
        all_tags.append(t)
print(f"所有标签（含重复）：{all_tags}")

unique_tags = list(set(all_tags))
print(f"去重后：{unique_tags}")

print(f"不同标签：{len(unique_tags)} 个")

for t in unique_tags:
    count = all_tags.count(t)
    print(f"{t} 出现 {count} 次")
```

---

## 踩坑记录

### 🐛 坑 1：嵌套取值括号位置错

```python
d["a"["b"]]     # ❌ TypeError
d["a"]["b"]     # ✅
```

**原因**：两个方括号要**并排**，先剥外层再剥内层。

### 🐛 坑 2：函数调用用了方括号

```python
set[nums]       # ❌
set(nums)       # ✅
list(set[nums]) # ❌
list(set(nums)) # ✅
```

**铁律：**

| 符号 | 含义 |
|---|---|
| `()` 圆括号 | 调用函数、传参数 |
| `[]` 方括号 | 取下标、取元素 |

### 🐛 坑 3：字典用了列表的方法

```python
product.append("brand")     # ❌ AttributeError
product["brand"] = "联想"    # ✅
```

**字典新增 = 直接赋值，不是 append。**

### 🐛 坑 4：`in` 判断键还是值

```python
d = {"a": 1}
print("a" in d)     # True（键）
print(1 in d)       # False（值不算）
print(1 in d.values())   # True（这才是判断值）
```

### 🐛 坑 5：`d.key` 用点号取字典值

```python
d.key       # ❌ AttributeError
d["key"]    # ✅
d[key]      # ✅（key 是变量时）
```

**字典取值只用方括号；变量不加引号，字符串才加引号。**

### 🐛 坑 6：`:.1f` 脱离 f-string

```python
print(discount:.1f)         # ❌ SyntaxError
print(f"{discount:.1f}")    # ✅
```

**格式说明符只能写在 f-string 的 `{}` 里。**

### 🐛 坑 7：f-string 引号冲突

```python
f"{s["name"]}"    # ❌ SyntaxError
f"{s['name']}"    # ✅ 里外引号不同
```

### 🐛 坑 8：`for i in len(x)`

```python
for i in len(articles):             # ❌ TypeError
for i in range(len(articles)):      # ✅
```

**`for` 只跟容器，不跟数字。** 要序号就 `range(len(...))`。

### 🐛 坑 9：字典用数字下标

```python
articles[i][0]              # ❌ KeyError
articles[i]["tags"]         # ✅
articles[i]["tags"][j]      # ✅
```

### 🐛 坑 10：中文输入法混进代码

```python
sum ＝0              # ❌ 全角等号
for s in orders：     # ❌ 全角冒号
print (f"{sum｝)      # ❌ 全角右花括号
```

**写代码前，先看一眼输入法是不是英文。**

### 🐛 坑 11：`sum` 当变量名

```python
sum = 0    # ⚠️ 覆盖内置函数
total = 0  # ✅
```

### 🐛 坑 12：集合打印顺序不稳定（实测发现）

```python
unique_tags = set(tags)
print(f"去重后：{unique_tags}")     # 顺序每次运行都可能不同
```

同一份代码连跑三次，实测结果：

| 运行次数 | 打印内容 |
|---|---|
| 第 1 次 | `{'Linux', 'Python', 'Hive', 'SQL'}` |
| 第 2 次 | `{'SQL', 'Python', 'Hive', 'Linux'}` |
| 第 3 次 | `{'SQL', 'Python', 'Hive', 'Linux'}` |

**原因**：集合本身无序，且 Python 3.3 起默认对字符串哈希做随机化，所以每次启动程序，遍历顺序都可能变。

**解法**：转列表或排序后再打印。

```python
unique_tags = list(set(tags))          # 转回列表
unique_tags = sorted(set(tags))        # 推荐：去重 + 排序，顺序稳定
```

**为什么重要**：输出不稳定就没法对比预期结果、没法复现、没法测试。数据处理里"结果可复现"是底线。

---

## 自检清单

- [x] 字典用键取值，列表用下标取值
- [x] `d["不存在"]` 会崩，`d.get("不存在")` 给退路
- [x] 增和改写法一样，看键之前有没有
- [x] `in` 判断的是键，不是值
- [x] 字典没有 `append`，新增用赋值
- [x] 嵌套取值 `d["a"]["b"]`，两个方括号并排
- [x] 列表套字典 = Excel 表格
- [x] `list(set(...))` 去重
- [x] `count()` 数出现次数
- [x] 集合无序，不能 `s[0]`
- [x] 元组不可变
- [x] `for` 只跟容器，要下标用 `range(len(...))`
- [x] 格式说明符写在 f-string 里
- [x] 写代码前切英文输入法
- [x] 能写打擂台、计数器、筛选收集三种模式

---

## 一句话记住

> **列表靠数，字典靠叫；`[]`会崩，`get()`给退路；**
> **字典新增用赋值，不是 append；**
> **嵌套一层层剥；集合管去重；`for`不跟数字。**

---

## 明天预告

**Day 07 · 复盘与 Git（第 1 周收官）**

- 复习本周：变量 → 条件 → 循环 → 列表 → 字典
- 整理所有代码，统一风格，清理乱文件
- 写 README（3 行就够：学什么、怎么跑、有什么）
- 全部推 GitHub，确认仓库整洁
- `git log --oneline` 看提交历史

产出：本周全部代码推送 + README

> 第 1 周收官日，也是给第 2 周打地基的一天。

---

## 附：当天工作记录（不属于课程笔记）

### 仓库状态（2026-09-17 20:00 核实）

- 最新提交：`263608c feat: 完成 Day6 巩固练习（商品、订单、标签统计）`
- 提交链：`263608c` ← `23f2bc7` ← `a7bb297` ← `d9d6850`
- 文件：`day06_practice.py` 已入库，共 17 个文件
- **本地领先远程 1 个提交（ahead 1），`263608c` 尚未 push**

### 待办

- `git push` 把 `263608c` 推上去
- 更新 `大数据开发学习规划-每日清单.xlsx`：第 5、6 天改为已完成，表头改 6 天
- 更新 `Python学习进度跟踪表.xlsx`：进度总览 / 每日打卡 / 技能清单 #21#22 / 错题本新增 6 条
