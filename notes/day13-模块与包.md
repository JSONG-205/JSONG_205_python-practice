# Day 13 · 模块与包

> 日期：2026-09-23（周三）｜ 用时：约 3h ｜ 状态：✅ 完成

---

## 今天做到了什么

- [x] 理解模块 = 一个 `.py` 文件
- [x] 三种 import 方式
- [x] 标准库 `math`（数学）
- [x] 标准库 `os`（系统）
- [x] 标准库 `datetime`（时间）
- [x] 标准库 `random`（随机）
- [x] `pip install` 第三方库
- [x] 用 `requests` 调用 GitHub API
- [x] **解决了解释器与 pip 不匹配问题**
- [x] 完成 5 道练习

**里程碑**：能用别人写好的库了。**这是 Python 强大的原因——不用造轮子。**

---

## 核心概念

### 1. 什么是模块

**模块 = 一个 `.py` 文件。**

```python
import json           # json 模块
import random         # random 模块
import math           # math 模块
```

**你自己写的文件也是模块**（`day08_practice.py` 可以被 import）。

### 2. 三种 import 方式

```python
# 方式 1：import 模块名（推荐）
import math
print(math.sqrt(16))        # 用 math. 前缀

# 方式 2：from 模块 import 函数
from math import sqrt
print(sqrt(16))             # 不用前缀

# 方式 3：import 模块 as 别名
import math as m
print(m.sqrt(16))
```

**推荐**：优先用方式 1，来源清晰。

### 3. 标准库三剑客

**`math` —— 数学**

```python
import math
math.pi              # 3.14159...
math.sqrt(144)       # 平方根
math.pow(2, 10)      # 次方（返回浮点）
math.ceil(4.3)       # 向上取整 5
math.floor(4.9)      # 向下取整 4
```

**`os` —— 系统**

```python
import os
os.getcwd()                       # 当前目录
os.listdir(".")                   # 列出文件
os.path.exists("data.txt")        # 文件存在？
os.path.join("a", "b.txt")        # 拼路径
```

**`datetime` —— 时间**

```python
from datetime import datetime, date, timedelta

datetime.now()                        # 当前日期时间
date.today()                          # 今天的日期
date.today() + timedelta(days=7)      # 7 天后
datetime.now().strftime("%Y-%m-%d")   # 格式化
```

**`random` —— 随机**

```python
import random
random.randint(1, 100)             # 随机整数
random.choice(["石头","剪刀","布"]) # 随机选一个
random.sample(range(1,50), 6)      # 抽 6 个不重复
random.shuffle(lst)                # 原地打乱（无返回值）
```

### 4. 第三方库用 pip 装

```bash
pip install requests
```

**常用命令：**

```bash
pip install 库名             # 装
pip install 库名==版本        # 装指定版本
pip list                     # 看已装的
pip uninstall 库名            # 卸载
```

**国内加速：**

```bash
pip install 库名 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 5. `requests` 调用 API

```python
import requests

response = requests.get("https://api.github.com/users/JSONG-205")
print(response.status_code)      # 200

data = response.json()           # JSON → 字典
print(data["name"])
print(data["followers"])
```

### 6. 关键坑：解释器和 pip 不匹配

**问题**：pip 装到了 Python A，但 PyCharm 用 Python B 跑，就报 `ModuleNotFoundError`。

**解决**：确保 PyCharm 的 Python Interpreter 和你 pip 装的 Python 是同一个。

**怎么查**：

- PyCharm 运行输出第一行会显示用的是哪个 Python
- `Settings → Project → Python Interpreter` 看配置

**终极方式**（不推荐，会破坏系统）：

```bash
C:\msys64\mingw64\bin\python.exe -m pip install 库名
```

> ⚠️ 上面这条「终极方式」实际不可行，见文末「附：当天工作记录」里的勘误。

---

## 语法速查

### 三种 import

```python
import math                          # 用 math.xxx
from math import sqrt                # 直接用 sqrt
import math as m                     # 用 m.xxx
```

### math

```python
math.pi                              # 圆周率
math.sqrt(16)                        # 平方根
math.pow(2, 10)                      # 次方
math.ceil(4.3) / math.floor(4.9)     # 上取整 / 下取整
```

### os

```python
os.getcwd()                          # 当前目录
os.listdir(".")                      # 列目录
os.path.exists("f.txt")              # 存在？
os.path.join("a", "b")               # 拼路径
```

### datetime

```python
datetime.now()                       # 现在
date.today()                         # 今天
date.today() + timedelta(days=7)     # 7 天后
datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

### random

```python
random.randint(1, 100)               # 随机整数
random.choice(lst)                   # 随机选一个
random.sample(lst, 3)                # 抽 3 个不重复
random.shuffle(lst)                  # 打乱（原地）
```

### requests

```python
response = requests.get(url)
response.status_code                 # 状态码
response.json()                      # 转字典
data["字段名"]                        # 取值
```

---

## 今天的代码

**`day13_practice.py`**

```python
# 练习 1：math
import math
print(math.pi)
print(math.sqrt(144))
print(math.pow(2, 10))
print(math.ceil(4.3))
print(math.floor(4.9))

# 练习 2：os
import os
print(os.getcwd())
print(os.listdir("."))
print(os.path.exists("day13_practice.py"))

# 练习 3：datetime
from datetime import datetime, date, timedelta
print(datetime.now())
print(date.today())
print(date.today() + timedelta(days=7))
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 练习 4：random
import random
print(random.randint(1, 100))
print(random.choice(["剪刀", "石头", "布"]))
print(random.sample(range(1, 50), 6))

lst = [1, 2, 3, 4, 5]
random.shuffle(lst)
print(lst)

# 练习 5：requests 调用 API
import requests
response = requests.get("https://api.github.com/users/JSONG-205")
print(response.status_code)

data = response.json()
print(data["name"])
print(data["followers"])
```

---

## 踩坑记录

### 🐛 坑 1：`pow` 和 `math.pow` 返回值不同

```python
pow(2, 10)          # 1024（整数）
math.pow(2, 10)     # 1024.0（浮点）
```

**内置 `pow` 返回整数，`math.pow` 返回浮点。**

### 🐛 坑 2：`shuffle` 有返回值吗？

```python
new_lst = random.shuffle(lst)     # ❌ new_lst = None
```

**`shuffle` 是原地打乱，返回 None。**

**正确：**

```python
random.shuffle(lst)
print(lst)
```

### 🐛 坑 3：解释器和 pip 不匹配（今天最大坑）

**现象**：pip 装好了库，PyCharm 运行还是 `ModuleNotFoundError`。

**原因**：pip 装到了 Python A，PyCharm 用 Python B。

**排查**：

- 看运行输出第一行是什么 Python
- 看 pip 装到哪了

**解法**：PyCharm `Settings → Python Interpreter` 换成同一个 Python。

### 🐛 坑 4：MSYS2 Python 拒绝 pip 装包

```
error: externally-managed-environment
```

**MSYS2 系统的 Python 禁止用 pip 装包。**

**解法**：换系统 Python 3.12（今天的做法）。

### 🐛 坑 5：模块名写错

```python
import util        # ❌ 少 s
import utils       # ✅
```

**模块名一个字母都不能差。**

---

## 自检清单

- [x] 知道模块是什么
- [x] 会三种 import 方式
- [x] 会用 `math`（pi / sqrt / pow / ceil / floor）
- [x] 会用 `os`（getcwd / listdir / path.exists）
- [x] 会用 `datetime`（now / today / timedelta / strftime）
- [x] 会用 `random`（randint / choice / sample / shuffle）
- [x] 会用 `pip install` 装第三方库
- [x] 会用 `requests` 调 API
- [x] 知道解释器和 pip 要匹配
- [x] 完成 5 道练习

---

## 一句话记住

> **模块 = .py 文件，`import 模块名` 用；**
> **标准库：`math` `os` `datetime` `random`；**
> **第三方库 `pip install`，注意解释器要匹配。**

---

## 明天预告

**Day 14 · 阶段小测**

- 关掉所有资料
- 独立写 20-30 行命令行小工具
- 检验前两周掌握情况

**产出**：1 个独立小工具

---

## 附：当天工作记录（不属于课程笔记）

### 解释器问题已解决 ✅

切换成功，运行输出第一行确认变成：

```
C:\Users\Lenovo\AppData\Local\Programs\Python\Python312\python.exe  ← 系统 Python 3.12
```

不再走 msys64 的 Python，`requests` 直接可用。练习 5 输出 `200 / JSONG / 0`，**API 请求、JSON 解析、取值全部正确**。

### ⚠️ 一处勘误

笔记「核心概念 6」里的这条：

```bash
C:\msys64\mingw64\bin\python.exe -m pip install 库名
```

被标成"终极方式"，但实际**走不通**，而且和同一个坑里刚写的现象自相矛盾：

- 那个 msys64 的 Python **根本没装 pip**（敲 `-m pip` 直接报 `No module named pip`）
- 就算给它装上 pip，MSYS2 的 Python 是"系统托管"的，pip 会**直接拒绝**：`error: externally-managed-environment`（PEP 668 保护）——就是本笔记坑 4 里那条

所以 msys64 这条路是死的。正确解法就是笔记里已经写的那句：**换成系统 Python 3.12**。原文保留不动，仅在此注明，免得以后复习被误导。

### 实测校验

用系统 Python 3.12.10 跑 `day13_practice.py` → 输出：

```
200
JSONG
0
```

请求成功、状态码 200、拿到 GitHub 用户名，三个值全对。

### 仓库状态（2026-09-23 19:50 核实）

- 最新提交：`0851bb5 feat: Day12 异常与调试练习 + 笔记 + 知识点手册更新`
- 本地与远程**完全同步**（`## main...origin/main` 无 ahead）
- 笔记里"Day 9~13 共 5 个 commit 待推"的信息**已过时**——Day 9~12 前几轮都推上去了，实际只剩 Day 13 这一笔待提交

### 小提醒

`day13_practice.py` 里练习 1~4 都注释掉了，只留练习 5 运行。调试时这么写没问题，但如果想让这个文件当"Day 13 成果"展示，把前面的注释放开更好看。

### 待办

- `day13_practice.py` 提交推送
- 更新 `大数据开发学习规划-每日清单.xlsx`：第 13 天 → 2026-09-23 / 已完成
- README 进度只到 Day09，Day10~Day13 四行没补
