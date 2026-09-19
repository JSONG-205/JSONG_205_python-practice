# Day 07 · 复盘与 Git（第 1 周收官）

> 日期：2026-09-17（周四）｜ 用时：约 2h ｜ 状态：✅ 完成

---

## 今天做到了什么

- [x] 复盘第 1 周 5 道题
- [x] 检查 `.gitignore` 规则
- [x] 建 `notes/` 目录
- [x] 把 day01 ~ day06 六个笔记归档
- [x] 写 `README.md`
- [x] 全部推送到 GitHub
- [x] 确认仓库结构完整、可读

**里程碑**：第 1 周收官，GitHub 上是一个**完整可读**的作品集。

---

## 核心概念

### 1. 什么是"复盘"

复盘 = 停下来，回头看看这一周学了什么。

**目的**：

| 目的 | 说明 |
|---|---|
| 检查掌握程度 | 哪些真会了，哪些只是看过 |
| 找出薄弱点 | 错的地方要重新过 |
| 建立知识链接 | 变量→循环→列表→字典，串起来 |
| 为下周做准备 | 明确下一步学什么 |

**复盘不是重复学，是用题目检查。**

### 2. 什么是"重构"

**重构 = 不改功能，只改代码结构，让它更好维护。**

Day 8 会专门做重构，Day 7 主要是**归档和整理**：

| 归档什么 | 放哪里 |
|---|---|
| 学习笔记 | `notes/` 目录 |
| 项目说明 | `README.md` |
| 忽略规则 | `.gitignore` |

### 3. `.gitignore` 的作用

**告诉 git：这些文件不要跟踪、不要提交。**

常见要忽略的：

| 规则 | 忽略什么 |
|---|---|
| `__pycache__/` | Python 缓存目录 |
| `*.py[cod]` | 编译文件 `.pyc .pyo .pyd` |
| `venv/` `.venv/` `env/` | 虚拟环境 |
| `.idea/` `.vscode/` | IDE 配置目录 |
| `*.log` `*.tmp` | 日志、临时文件 |
| `Thumbs.db` `.DS_Store` | Windows/Mac 系统文件 |

**为什么需要？**

- 缓存文件是机器生成的，与源码无关
- 提交上去会让仓库很乱
- 每个人电脑上生成的都不同，会引发无意义的冲突

### 4. `README.md` 的作用

**README 是仓库的"说明书"**，别人进来第一眼看到的东西。

**一份好的 README 要说清：**

| 内容 | 说明 |
|---|---|
| 项目是什么 | 一句话概括 |
| 谁做的 | 学习者信息 |
| 已完成什么 | 进度表 |
| 目录结构 | 哪个文件是干什么的 |
| 怎么运行 | 别人怎么跑起来 |
| 下一步 | 未来计划 |

**为什么重要？**

- GitHub 项目首页就是 README
- 面试官会点进仓库看，README 写得清楚 = 专业
- 自己几个月后回来看，也知道当初在干什么

### 5. `git status` 和 `git log` 的区别

```bash
git status        # 看当前状态：有没有未提交的改动
git log --oneline # 看历史：所有提交记录
```

| 命令 | 关注 | 用在哪 |
|---|---|---|
| `git status` | **现在** | 提交前确认 |
| `git log` | **过去** | 回顾、找提交 |

**每天收工前两个都跑一遍：**

```bash
git status
git log --oneline -5    # 看最近 5 条
```

---

## 语法速查

### Git 每天收工三连

```bash
git add .                    # 把所有改动暂存
git commit -m "描述"          # 提交到本地
git push                     # 推送到 GitHub
```

### 提交信息前缀（规范）

| 前缀 | 用在哪 | 例子 |
|---|---|---|
| `feat:` | 新功能 | `feat: 完成循环练习` |
| `fix:` | 修 bug | `fix: 修复第7次猜中被误判的问题` |
| `docs:` | 文档 | `docs: 添加 README` |
| `refactor:` | 重构 | `refactor: 把 bmi 抽成函数` |
| `chore:` | 杂项（配置等） | `chore: add .gitignore` |
| `merge:` | 合并 | `merge: 保留本地 guess.py 版本` |

### 检查状态

```bash
git status              # 当前状态
git log --oneline       # 全部提交历史
git log --oneline -5    # 最近 5 条
```

### 目录操作

```bash
dir              # 列出文件
dir *.md         # 只看 md 文件
mkdir notes      # 建目录
type 文件名       # 查看文件内容（PowerShell）
```

---

## 今天的产物

### 1. `notes/` 目录（6 个笔记）

```
notes/
├── day01-环境搭建与第一行代码.md
├── day02-变量与数据类型.md
├── day03-条件判断.md
├── day04-循环.md
├── day05-列表list.md
└── day06-字典与集合.md
```

### 2. `README.md`

```markdown
# JSONG_205_python-practice

大数据开发学习之路 · Python 编程地基

## 学习者

- GitHub：JSONG-205
- 起点：零基础
- 节奏：每天 2 小时，每天有代码产出
- 目标：6 个月走完大数据开发路线

## 已完成

| 天 | 主题 | 产出文件 |
|---|---|---|
| Day 1 | 环境搭建与第一行代码 | hello.py |
| Day 2 | 变量与数据类型 | intro.py / calc.py / bmi.py |
| Day 3 | 条件判断 | judge.py / grade.py |
| Day 4 | 循环 | multiplication.py / guess.py |
| Day 5 | 列表 list | scores.py / shopping.py / numbers.py |
| Day 6 | 字典 dict 与集合 set | student.py / students.py / set_demo.py / day06_practice.py |

## 目录结构

python-practice/
├── notes/
├── hello.py
├── intro.py / calc.py / bmi.py
├── ...
└── README.md

## 怎么运行

python 文件名.py

## 学习笔记

每天笔记在 notes/ 目录

## 下一步

Day 7 → Day 8~14 函数、字符串、文件与 JSON、异常、模块
```

### 3. 仓库最终结构

```
python-practice/
├── notes/
│   ├── day01-环境搭建与第一行代码.md
│   ├── day02-变量与数据类型.md
│   ├── day03-条件判断.md
│   ├── day04-循环.md
│   ├── day05-列表list.md
│   └── day06-字典与集合.md
├── README.md
├── .gitignore
├── hello.py / intro.py / calc.py / bmi.py
├── judge.py / grade.py
├── multiplication.py / guess.py
├── scores.py / shopping.py / numbers.py
├── student.py / students.py / set_demo.py / day06_practice.py
```

---

## 复盘 5 题回顾（今天最该记住的）

### 题 1：变量和类型

```python
a = "5"
b = 5
print(a + str(b))
```

**输出**：`"55"`（字符串拼接）

**关键**：`a` 是字符串，`b` 转换后也是字符串，`+` 拼接成 `"55"`。

### 题 2：条件判断

```python
x = 60
if x >= 90:
    print("优秀")
elif x >= 60:
    print("及格")
else:
    print("不及格")
```

**输出**：`及格`

**如果把 `elif x >= 60` 改成 `elif x <= 60`**：**输出不变**（因为 60 满足 >= 90 为假，走到 elif 时 x = 60，`<= 60` 为真，还是打印"及格"）。

### 题 3：循环

```python
total = 0
for i in range(1, 5):
    total += i
print(total)
```

**输出**：`10`

**`range(1, 5)` 几个数**：4 个（1、2、3、4），含头不含尾。

### 题 4：列表（❌ 今天你唯一错的）

```python
nums = [3, 1, 4, 1, 5]
nums.append(9)      # [3, 1, 4, 1, 5, 9]
nums.remove(1)      # 删第一个 1 → [3, 4, 1, 5, 9]
print(nums)
```

**输出**：`[3, 4, 1, 5, 9]`

**关键**：
- `append(9)` 末尾加 9
- `remove(1)` 删**第一个值** 1，不是下标

**你答的 `[3, 1, 1, 5]` 说明"多步操作心算跳步"，以后一步一步写。**

### 题 5：字典

```python
d = {"a": 1, "b": 2}
d["c"] = 3
print(len(d))         # 3
print(d.get("x", 0))  # 0（不存在返回默认值）
```

**关键**：`get("x", 0)` 找不到时返回 0，不报错。

---

## 踩坑记录

### 🐛 坑 1：`remove` 和 `pop` 混淆

```python
nums = [3, 1, 4, 1, 5]
nums.remove(1)      # 删"值 1"，不是下标
```

**`remove` 找的是"是谁"，`pop` 找的是"第几个"。**

| 方法 | 括号里写什么 | 删除对象 |
|---|---|---|
| `remove(1)` | **值** | 第一个等于 1 的元素 |
| `pop(0)` | **下标** | 第 0 个位置的元素 |

### 🐛 坑 2：`remove` 只删第一个

```python
nums = [1, 5, 1, 3, 1]
nums.remove(1)
print(nums)    # [5, 1, 3, 1]  只删了最左边的 1
```

想全删掉：

```python
nums = [n for n in nums if n != 1]    # [5, 3]
```

### 🐛 坑 3：多步操作心算跳步

题 4 出错，就是因为没一步一步写。

**正确做法**：

```
开始：     [3, 1, 4, 1, 5]
append(9)：[3, 1, 4, 1, 5, 9]
remove(1)：[3, 4, 1, 5, 9]
```

**每一步都在纸上写当前状态。**

### 🐛 坑 4：`.gitignore` 注释乱码

```bash
# ===== 铞氰蜷鎏♦♦ =====      ← 应该是 "虚拟环境"
# ===== 绯苹鞯鐨富涔 =====      ← 应该是 "系统文件"
```

**原因**：编码不一致。

**影响**：git 只认规则不认注释，功能没影响，但不美观。

---

## 自检清单

- [x] 能说出第 1 周学了什么（变量→循环→列表→字典）
- [x] 能区分 `remove` 和 `pop`
- [x] 知道多步操作要一步步写
- [x] `.gitignore` 规则齐全
- [x] `notes/` 目录建好，6 个笔记归档
- [x] `README.md` 能让人看懂项目
- [x] `git status` 显示 working tree clean
- [x] `git log` 里 7 天的提交都在
- [x] 仓库推送成功

## 一句话记住

> **`git add` → `git commit` → `git push`，每天收工三连；**
> **`git status` 看现在，`git log` 看过往；**
> **`remove` 找"是谁"，`pop` 找"第几个"。**

---

## 第 1 周回顾

**7 天走过 8 天量。** 从零基础到：

| 能力 | 状态 |
|---|---|
| 变量、类型、转换 | ✅ |
| 条件判断（if/elif/else） | ✅ |
| 循环（for/while/嵌套） | ✅ |
| 列表（增删改查/切片/遍历） | ✅ |
| 字典、集合（嵌套/遍历/去重） | ✅ |
| 三种核心模式（打擂台/计数器/筛选收集） | ✅ |
| Git 基础（init/add/commit/push） | ✅ |
| 写学习笔记 | ✅ |
| 写 README | ✅ |

**GitHub 仓库：https://github.com/JSONG-205/JSONG_205_python-practice**

---

## 明天预告

**Day 08 · 函数**

- `def` 定义函数
- 参数与返回值
- `return` vs `print`
- 默认参数
- 作用域
- 把重复逻辑抽成函数

产出：5 个练习重构为函数

---

## 后续日期记录（供参考）

| 天 | 完成日期 |
|---|---|
| Day 5 | 2026-09-17（周四）补记 |
| Day 6 | 2026-09-17（周四） |
| Day 7 | 2026-09-17（周四） |
| Day 8 | 2026-09-19（周六） |
