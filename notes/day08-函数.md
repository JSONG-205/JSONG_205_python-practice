# Day 08 · 函数

> 日期：2026-09-19（周六）｜ 用时：约 3h ｜ 状态：✅ 完成

---

## 今天做到了什么

- [x] `def` 定义函数
- [x] 参数与返回值
- [x] 分清 `return` 和 `print`
- [x] 默认参数（放后面）
- [x] 作用域（函数内变量外面看不到）
- [x] 把 5 个旧练习重构为函数
- [x] `not lst` 判断空列表
- [x] `raise ValueError` 主动报错（超前学习）
- [x] `if __name__ == "__main__":` 入口保护（超前学习）

**里程碑**：从"流水账代码"进化到"积木块代码"，能复用了。

---

## 核心概念

### 1. 为什么需要函数

**没有函数：**

```python
height1 = 1.75; weight1 = 70
bmi1 = weight1 / (height1 ** 2)
height2 = 1.68; weight2 = 55
bmi2 = weight2 / (height2 ** 2)
```

同一个公式写两遍，改一处要改两处。

**有函数：**

```python
def calc_bmi(height, weight):
    return weight / (height ** 2)

print(calc_bmi(1.75, 70))
print(calc_bmi(1.68, 55))
```

公式只写一次。

### 2. 函数定义

```python
def 函数名(参数1, 参数2):
    函数体
    return 返回值
```

| 部分 | 说明 |
|---|---|
| `def` | 关键字，声明定义函数 |
| 函数名 | snake_case（小写下划线） |
| `()` | 参数放这 |
| `:` | 冒号不能丢 |
| 缩进 | 4 空格 |
| `return` | 返回结果（可选） |

### 3. `return` vs `print`（重点）

```python
def f1(a, b):
    return a + b        # 交回值

def f2(a, b):
    print(a + b)        # 只显示

x = f1(3, 5)    # x = 8
y = f2(3, 5)    # 屏幕显示 8，但 y = None
```

| 写法 | 调用后拿到 |
|---|---|
| `return a + b` | 值 `8`，可以接着用 |
| `print(a + b)` | `None`，值丢了 |

**判断口诀**：结果后面还要用吗？

- 要用 → `return`
- 只显示给用户看 → `print`
- **不确定 → 一律 `return`**

**核心原则**：**函数负责算，主流程负责打印。**

### 4. 默认参数

```python
def greet(name, greeting="你好"):
    print(f"{greeting}，{name}")

greet("张三")                # 你好，张三（用默认值）
greet("李四", "早上好")      # 早上好，李四（覆盖默认值）
```

⚠️ **有默认值的参数必须放后面：**

```python
def f(a, b=10):      # ✅
def f(a=10, b):      # ❌ SyntaxError
```

**为什么？** 调用时如果省略参数，Python 不知道你省的是哪个。

### 5. 作用域

```python
x = 10

def f():
    x = 20        # 新建局部变量，不是改外面的
    print(x)      # 20

f()               # 20
print(x)          # 10（外面的没变）
```

**函数是独立小房间：**

- 外面的变量，函数里能读
- 函数里改同名变量，是新建，不影响外面
- 函数执行完，局部变量销毁

### 6. `not lst` 判断空列表

```python
if not lst:
    raise ValueError("空列表没有最大值")
```

**Python 里"空的东西 = 假"：**

| 值 | 真假 |
|---|---|
| `[]` 空列表 | 假 |
| `[1,2]` 非空列表 | 真 |
| `""` 空字符串 | 假 |
| `"abc"` 非空字符串 | 真 |
| `0` | 假 |
| `None` | 假 |

`if not lst:` 等价于 `if len(lst) == 0:`，但更简洁。

### 7. `raise ValueError(...)`

```python
raise ValueError("空列表没有最大值")
```

执行到这行，程序**当场停下**，屏幕显示：

```
ValueError: 空列表没有最大值
```

**为什么要主动报错？**

- 不主动 raise：可能报 `IndexError`，信息不清晰
- 主动 raise：信息明确，"空列表没有最大值"一眼看懂

**Day 12 会专门学异常处理。**

### 8. `if __name__ == "__main__":`

**每个 .py 文件都有内置变量 `__name__`，值取决于怎么使用：**

| 场景 | `__name__` 的值 |
|---|---|
| 直接运行 `python xxx.py` | `"__main__"` |
| 被别的文件 `import` | `"xxx"`（文件名） |

**用途**：把"功能代码"和"测试代码"分开。

```python
def add(a, b):
    return a + b


if __name__ == "__main__":
    print(add(3, 4))    # 只有自己运行才跑
```

| 场景 | 测试代码执行吗 |
|---|---|
| 自己运行 | ✅ 执行 |
| 别人 import | ❌ 不执行 |

---

## 语法速查

```python
# 定义
def 函数名(参数):
    return 值


# 默认参数
def f(a, b=10):
    ...


# 多参数
def f(a, b, c):
    ...


# 无返回值
def f():
    print("hi")


# 无参数
def f():
    ...


# 空列表判断
if not lst:
    ...


# 主动报错
raise ValueError("消息")


# 入口保护
if __name__ == "__main__":
    ...
```

---

## 今天的代码

### 重构 1：`scores.py`

```python
def average(lst):
    """返回列表的平均值"""
    total = 0
    for n in lst:
        total += n
    return total / len(lst)


scores = [85, 92, 55, 78, 90]

print(scores)
print(f"最高分：{max(scores)}")
print(f"最低分：{min(scores)}")
print(f"平均分：{average(scores):.1f}")

for i in range(len(scores)):
    if scores[i] < 60:
        scores[i] = 60

print(f"调整后：{scores}")
print(f"排序后：{sorted(scores)}")
```

### 重构 2：`bmi.py`

```python
def calc_bmi(height, weight):
    """根据身高体重算 BMI"""
    return weight / (height ** 2)


def get_bmi_level(bmi):
    """根据 BMI 值返回等级"""
    if bmi < 18.5:
        return "偏瘦"
    elif bmi < 24:
        return "正常"
    elif bmi < 28:
        return "偏胖"
    else:
        return "肥胖"


height = float(input("请输入身高（米）："))
weight = float(input("请输入体重（公斤）："))

bmi = calc_bmi(height, weight)
level = get_bmi_level(bmi)

print(f"你的BMI为{bmi:.1f}，你属于{level}")
```

### 重构 3：`numbers.py`

```python
def get_evens(lst):
    """返回所有偶数"""
    result = []
    for n in lst:
        if n % 2 == 0:
            result.append(n)
    return result


def get_big(lst, threshold=30):
    """返回所有大于 threshold 的数，默认 30"""
    result = []
    for n in lst:
        if n > threshold:
            result.append(n)
    return result


def count_between(lst, low, high):
    """统计 low~high 之间的数量（含两端）"""
    count = 0
    for n in lst:
        if low <= n <= high:
            count += 1
    return count


def sort_desc(lst):
    """从大到小排序，返回新列表"""
    return sorted(lst, reverse=True)


nums = [12, 45, 8, 33, 21, 60, 17, 99, 5, 40]

print(get_evens(nums))
print(get_big(nums))
print(count_between(nums, 20, 50))
print(sort_desc(nums))
```

### 重构 4：`students.py`

```python
def find_top(students):
    """打擂台找最高分学生"""
    top = students[0]
    for s in students:
        if s["score"] > top["score"]:
            top = s
    return top


def average_score(students):
    """返回平均分"""
    total = 0
    for s in students:
        total += s["score"]
    return total / len(students)


def count_pass(students):
    """统计及格人数"""
    count = 0
    for s in students:
        if s["score"] >= 60:
            count += 1
    return count


def find_failed(students):
    """返回所有不及格的学生姓名列表"""
    failed = []
    for s in students:
        if s["score"] < 60:
            failed.append(s["name"])
    return failed


students = [
    {"name": "张三", "age": 20, "score": 85},
    {"name": "李四", "age": 21, "score": 92},
    {"name": "王五", "age": 19, "score": 78},
    {"name": "赵六", "age": 22, "score": 60},
    {"name": "钱七", "age": 20, "score": 55}
]

top = find_top(students)
print(f"最高分：{top['name']} {top['score']}")
print(f"平均分：{average_score(students):.1f}")
print(f"及格人数：{count_pass(students)}")
print(f"不及格：{find_failed(students)}")
```

### 重构 5：`calc.py`

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


a = float(input("请输入第一个数字："))
b = float(input("请输入第二个数字："))

print(f"和为{add(a, b)}，差为{subtract(a, b)}，积为{multiply(a, b)}，商为{divide(a, b):.2f}")
```

### 巩固练习：`day08_practice.py`

```python
# C1：算术函数
def square(n):
    return n * n


def cube(n):
    return n * n * n


def power(n, exp=2):
    return n ** exp


# C2：列表工具（手写实现）
def max_of(lst):
    if not lst:
        raise ValueError("空列表没有最大值")
    m = lst[0]
    for x in lst[1:]:
        if x > m:
            m = x
    return m


def min_of(lst):
    if not lst:
        raise ValueError("空列表没有最小值")
    m = lst[0]
    for x in lst[1:]:
        if x < m:
            m = x
    return m


def sum_of(lst):
    total = 0
    for x in lst:
        total += x
    return total


def average_of(lst):
    if not lst:
        raise ValueError("空列表无法求平均")
    return sum_of(lst) / len(lst)


# C3：学生成绩系统
def find_top(students):
    if not students:
        return None
    top = students[0]
    for s in students[1:]:
        if s["score"] > top["score"]:
            top = s
    return top


def find_low(students):
    if not students:
        return None
    low = students[0]
    for s in students[1:]:
        if s["score"] < low["score"]:
            low = s
    return low


def count_pass(students, threshold=60):
    cnt = 0
    for s in students:
        if s["score"] >= threshold:
            cnt += 1
    return cnt


def find_by_score(students, min_score):
    result = []
    for s in students:
        if s["score"] >= min_score:
            result.append(s["name"])
    return result


def class_report(students):
    top = find_top(students)
    low = find_low(students)
    passed = count_pass(students)
    above_90 = find_by_score(students, 90)

    print("===== 班级报告 =====")
    print(f"最高分：{top['name']} {top['score']}")
    print(f"最低分：{low['name']} {low['score']}")
    print(f"及格人数：{passed}")
    print(f"90分以上：{above_90}")


if __name__ == "__main__":
    # 测试代码
    print("--- C1 ---")
    print(square(4))
    print(cube(3))
    print(power(2))
    print(power(2, 5))

    print("\n--- C2 ---")
    nums = [3, 1, 4, 1, 5, 9, 2, 6]
    print(max_of(nums))
    print(min_of(nums))
    print(sum_of(nums))
    print(average_of(nums))

    print("\n--- C3 ---")
    students = [
        {"name": "张三", "score": 85},
        {"name": "李四", "score": 92},
        {"name": "王五", "score": 78},
        {"name": "赵六", "score": 60},
        {"name": "钱七", "score": 55},
    ]
    class_report(students)
```

---

## 三个重构原则

| 原则 | 说明 | 例子 |
|---|---|---|
| **一件事** | 一个函数只干一件事 | `calc_bmi` 只算 BMI，不管等级 |
| **参数传递** | 通过参数接收数据，不读全局变量 | 4 个函数都接收 `students` 参数 |
| **return 返回** | 用 return 交回结果，不用 print | 让调用者拿到值再决定怎么用 |

**判断要不要抽函数：**

| 情况 | 建议 |
|---|---|
| 同一段代码写 2 遍以上 | 抽函数 |
| 一段逻辑能独立描述 | 抽函数 |
| 只写一次、很简单 | 不用抽 |

---

## 踩坑记录

### 🐛 坑 1：参数没传够

```python
def calc(a, b):
    return a + b

calc(3)     # ❌ TypeError: missing 1 required positional argument: 'b'
```

**原因**：函数有 2 个必传参数，只传了 1 个。

**解法**：传够，或给默认值。

### 🐛 坑 2：默认参数没放后面

```python
def f(a=10, b):     # ❌ SyntaxError
    ...

def f(a, b=10):     # ✅
    ...
```

**规则**：有默认值的参数必须放后面。

### 🐛 坑 3：函数里 print，拿不到结果

```python
def average(lst):
    ...
    print(total / len(lst))     # ❌ 只显示，不返回

result = average([1, 2, 3])     # result = None
```

**解法**：改用 `return`。

**核心**：**函数负责算，主流程负责打印。**

### 🐛 坑 4：以为函数里改 x，外面会变

```python
x = 10

def f():
    x = 20      # 新建局部变量，不是改外面的

f()
print(x)        # 还是 10
```

**原因**：函数是独立小房间。

**解法**：真要改外面的，用 `global`（但很少用，尽量不写）。

### 🐛 坑 5：输出顺序凭语感

```python
def greet(name, greeting="你好"):
    print(f"{greeting}，{name}")
```

**错误答案**："张三你好"
**正确答案**："你好，张三"（严格按代码顺序）

**铁律**：输出什么，由代码决定，不由语感决定。

---

## 自检清单

- [x] 能写出 `def 函数名(参数):` 定义函数
- [x] 能分清 `return` 和 `print`
- [x] 知道默认参数必须放后面
- [x] 知道函数内变量外面看不到
- [x] 能用 `not lst` 判断空列表
- [x] 能用 `raise ValueError` 主动报错
- [x] 会写 `if __name__ == "__main__":`
- [x] 能把重复代码抽成函数
- [x] 能通过参数接收数据，不用全局变量
- [x] 5 个重构 + 3 组练习全部跑通

---

## 一句话记住

> **函数负责算，主流程负责打印；**
> **return 交回值，print 只显示；**
> **默认参数放后面；重复代码抽函数。**

---

## 明天预告

**Day 09 · 字符串**

- 索引与切片
- f-string 进阶
- `split / join / strip / replace / startswith`
- 字符串常用方法

产出：字符串练习 10 道

---

## 收工状态

| 项目 | 状态 |
|---|---|
| commit | ✅ `9d6d311` |
| push | ⏳ 网络问题，待重试 |
| 本地领先远程 | 1 个提交 |

**明天开工第一件事：**

```bash
cd D:\dev\python-practice
git status
git push
```

成功就继续 Day 9，失败就再等。
