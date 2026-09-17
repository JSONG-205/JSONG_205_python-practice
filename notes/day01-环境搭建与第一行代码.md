# Day 01 · 环境搭建与第一行代码

> 日期：2026-09-02（周三） ｜ 用时：2h ｜ 状态：✅ 完成

---

## 今天做到了什么

- [x] 安装 Python 3.14.6（**勾选 Add to PATH**）
- [x] 终端验证 `python --version`
- [x] 建立英文路径项目目录 `D:\dev\python-practice`
- [x] 写出并运行 `hello.py`
- [x] 用 Git 完成人生第一次提交

**里程碑**：从"什么都不会"到"写出第一行代码并提交版本管理"。

---

## 核心概念

### 为什么要勾选 Add to PATH

不勾选的话，终端里敲 `python` 会提示"不是内部或外部命令"。勾选后，Python 被加进系统环境变量，**在任意目录下都能识别 `python` 命令**。

### 为什么用英文路径

中文路径（如 `D:\github仓库`）在 Git 和 Python 里偶尔会出编码问题。**从第一天起就用纯英文路径**，一劳永逸。

### Git 本地 vs 远程

| 概念 | 位置 | 说明 |
|---|---|---|
| **本地仓库** | 你电脑上的文件夹 | 有 `.git` 隐藏目录才算仓库 |
| **远程仓库** | GitHub 网站 | 需要 `git push` 才会同步 |

> 不 push，GitHub 永远是空的。这个我后来踩过。

---

## 命令速查

| 命令 | 全称 | 作用 |
|---|---|---|
| `mkdir 名字` | make directory | 新建文件夹 |
| `cd 路径` | change directory | 进入文件夹 |
| `dir` | directory | 查看当前目录内容 |
| `python --version` | — | 查看 Python 版本 |
| `python 文件名.py` | — | 运行 Python 脚本 |
| `notepad 文件名.py` | — | 用记事本新建/编辑文件 |
| `git init` | — | 让 Git 接管当前文件夹 |
| `git add 文件名` | — | 把文件加入暂存区 |
| `git commit -m "说明"` | — | 正式存档一版 |
| `git log` | — | 查看提交历史 |

---

## 今天的代码

**`hello.py`**

```python
print("我写出了第一行代码")
```

运行：

```bash
python hello.py
```

输出：`我写出了第一行代码`

---

## 踩坑记录

### ❌ 坑 1：文件名拼写错误

```bash
git add heelo.py
# fatal: pathspec 'heelo.py' did not match any files
```

**原因**：文件名拼成 `heelo.py`，仓库里根本没有这个文件。

**解法**：
1. 仔细核对文件名
2. 用 `git add .` 一次加全部，省得敲文件名

> 💡 **重要心得**：报错不是"我搞坏了什么"，而是 Git 在告诉我"名字对不上"。**看到红色报错先读一遍，十次有八次答案就在那句话里。**

### ❌ 坑 2：在错误的目录执行 git 命令

```bash
PS D:\dev> git init     # ❌ 错
```

**后果**：整个 `D:\dev` 被 Git 接管，以后所有项目挤进同一个仓库，乱套。

**铁律**：**一个项目 = 一个文件夹 = 一次 `git init`**。

---

## 自检清单

- [x] 能在任意目录敲 `python --version` 看到版本号
- [x] 知道 `mkdir` / `cd` / `dir` 分别干什么
- [x] 能独立完成 init → add → commit 全流程
- [x] 理解本地仓库和 GitHub 是两回事

---

## 一句话记住

> **Git 不会覆盖，只追加版本。** 每次 commit 存一版，旧版本永远在，随时能反悔。

---

## 明天预告

**Day 02 · 变量与数据类型**
变量命名、str/int/float/bool、input/print、类型转换、f-string 格式化。

产出：`intro.py` / `calc.py` / `bmi.py`
