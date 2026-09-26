# Day 14 · 阶段小测

> 日期：2026-09-26（周六）｜ 用时：约 2h ｜ 状态：✅ 完成

---

## 今天的任务

**关掉所有资料，独立写一个命令行通讯录工具。**

**产出**：`contacts.py`，包含 5 个功能 + 文件持久化。

---

## 小测评分

| 项目 | 分值 | 得分 |
|---|---|---|
| 能运行，显示菜单 | 20 | 20 |
| 添加 + 保存 | 15 | 15 |
| 查看 | 15 | 15 |
| 查找 | 10 | 10 |
| 删除 + 保存 | 15 | 15 |
| 退出 | 5 | 5 |
| 函数拆分 | 10 | 10 |
| 异常处理 | 10 | 10 |
| **总分** | **100** | **100** |

**满分。** 加分项还额外完成了 3 个（重名检查、模糊匹配、删除确认）。

---

## 你的代码

**`contacts.py`**

```python
import json
import os


def load_contacts():
    """从 contacts.json 文件加载联系人列表，文件不存在则返回空列表"""
    if not os.path.exists('contacts.json'):
        return []
    try:
        with open('contacts.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_contacts(contacts):
    """将联系人列表保存到 contacts.json 文件"""
    with open('contacts.json', 'w', encoding='utf-8') as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)


def add_contact(contacts):
    """添加联系人，支持姓名重复检查"""
    name = input("请输入姓名：").strip()
    if not name:
        print("姓名不能为空！")
        return

    for c in contacts:
        if c["name"] == name:
            print(f"联系人「{name}」已存在！")
            return

    phone = input("请输入电话：").strip()
    if not phone:
        print("电话不能为空！")
        return

    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)
    print(f"联系人「{name}」添加成功！")


def show_contacts(contacts):
    """显示所有联系人"""
    if not contacts:
        print("通讯录为空！")
        return
    print("\n===== 所有联系人 =====")
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} - {c['phone']}")
    print()


def find_contact(contacts):
    """查找联系人，支持模糊匹配"""
    name = input("请输入要查找的姓名：").strip()
    if not name:
        print("姓名不能为空！")
        return

    results = [c for c in contacts if name in c["name"]]
    if not results:
        print("未找到该联系人！")
    else:
        print(f"\n找到 {len(results)} 个匹配结果：")
        for c in results:
            print(f"  {c['name']} - {c['phone']}")
        print()


def delete_contact(contacts):
    """删除联系人，删除前确认"""
    name = input("请输入要删除的姓名：").strip()
    if not name:
        print("姓名不能为空！")
        return

    for i, c in enumerate(contacts):
        if c["name"] == name:
            confirm = input(f"确认删除「{name}」吗？(y/n)：").strip().lower()
            if confirm == 'y':
                contacts.pop(i)
                save_contacts(contacts)
                print(f"联系人「{name}」已删除！")
            else:
                print("已取消删除。")
            return

    print("未找到该联系人！")


def main():
    """主函数：显示菜单并分发操作"""
    contacts = load_contacts()

    while True:
        print("===== 通讯录 =====")
        print("1. 添加联系人")
        print("2. 查看所有联系人")
        print("3. 查找联系人")
        print("4. 删除联系人")
        print("5. 退出")
        choice = input("请选择：").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            show_contacts(contacts)
        elif choice == '3':
            find_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("再见！")
            break
        else:
            print("无效选择，请重新输入！")


if __name__ == '__main__':
    main()
```

---

## 技术点覆盖

| 技能 | 用在哪 |
|---|---|
| **函数** | 6 个函数，职责清晰 |
| **列表 + 字典** | 联系人数据结构 |
| **循环** | 主菜单 `while True` |
| **条件判断** | 菜单 `if/elif` 分发 |
| **文件读写** | `open` + `with` |
| **JSON** | `json.load` / `json.dump` |
| **异常处理** | `try/except` 双捕获 |
| **列表推导式** | `[c for c in contacts if ...]` |
| **enumerate** | 带编号显示 |
| **`__name__ == '__main__'`** | 入口保护 |

---

## 加分项

| 加分项 | 状态 |
|---|---|
| 添加时判断姓名重复 | ✅ |
| 查找支持模糊匹配 | ✅ |
| 删除前确认 | ✅ |

**全部做到了。**

---

## 亮点代码

### 1. 双重保险的文件读取

```python
if not os.path.exists('contacts.json'):
    return []
try:
    with open('contacts.json', 'r', encoding='utf-8') as f:
        return json.load(f)
except (json.JSONDecodeError, FileNotFoundError):
    return []
```

**提前检查 + 兜底捕获，生产级写法。**

### 2. 模糊匹配一行搞定

```python
results = [c for c in contacts if name in c["name"]]
```

**输入"张"能匹配到"张三"。**

### 3. 入口保护

```python
if __name__ == '__main__':
    main()
```

**`contacts.py` 被 import 时不会自动跑菜单。**

---

## 小改进建议（不影响评分）

| 建议 | 说明 |
|---|---|
| 抽 `is_exist(contacts, name)` | 添加和删除都用"姓名查重"，可以复用 |
| `delete_contact` 用列表推导 | `contacts[:] = [c for c in contacts if c["name"] != name]` |
| 显示联系人时加总分 | `len(contacts)` 提示一共有几个 |

**现在这版已经很好了，别急着改。**

---

## 第 2 周总结

### 完成清单

| 天 | 主题 | 状态 |
|---|---|---|
| Day 8 | 函数 | ✅ |
| Day 9 | 字符串 | ✅ |
| Day 10 | 文件读写 | ✅ |
| Day 11 | JSON 数据 | ✅ |
| Day 12 | 异常与调试 | ✅ |
| Day 13 | 模块与包 | ✅ |
| Day 14 | 阶段小测 | ✅ |

### 第 2 周掌握的技能

| 分类 | 技能 |
|---|---|
| 函数 | `def`、`return`、默认参数、作用域、`if __name__` |
| 字符串 | 索引切片、`upper/lower/strip/split/join/replace`、`find/count`、f-string 格式 |
| 文件 | `open`、`with`、`r/w/a`、`read/readlines`、`write`、`encoding` |
| JSON | `dumps/loads`、`dump/load`、`ensure_ascii`、`indent` |
| 异常 | `try/except/finally`、5 种常见异常、看报错堆栈 |
| 模块 | `import` 三种方式、`math/os/datetime/random`、`pip`、`requests` |

### 第 2 周踩坑汇总（进错题本）

| 坑 | 天 |
|---|---|
| 函数里 `print` 拿不到值 | Day 8 |
| 默认参数放错位置 | Day 8 |
| 字符串 `replace` 后原串没变 | Day 9 |
| `if s.find("e"):` 判断错 | Day 9 |
| `f"{x:.2f}"` 格式符脱离 f-string | Day 9 |
| 同一个 `with` 块连续读多次 | Day 10 |
| `"a"` 模式下读文件 | Day 10 |
| `write()` 传入非字符串 | Day 10 |
| `dump` 少了文件对象 | Day 11 |
| `load` 参数写反 | Day 11 |
| 异常类型写错捕获不到 | Day 12 |
| 解释器和 pip 不匹配 | Day 13 |

---

## 明天 Day 15 预告

**Day 15 · 类与对象（一）**

> 第 3 周开始，进入面向对象编程

- 什么是类、什么是对象
- `class` 语法
- `__init__` 构造方法
- `self` 到底是什么

**产出**：写一个 `Student` 类

**为什么重要**：后面 PySpark 大量用类，`DataFrame` 就是类。不会类，后面 Spark 学不动。

---

## 附：当天工作记录（不属于课程笔记）

### ⚠️ 目录重构（就在今天归档前做的）

今晚把整个仓库按天分文件夹了（`dayNN/`），`contacts.py` 现在位于 `day14/`。

因为文件位置变了、工作目录也跟着变，脚本开头补了一行：

```python
os.chdir(os.path.dirname(os.path.abspath(__file__)))
```

它的作用是**运行前先把工作目录切到脚本自己所在的目录**，这样不管从哪个目录启动，
下面那句 `open('contacts.json')` 都能定位到 `day14/` 里的那个文件。

上面「你的代码」一节保留的是**小测当时的原始版本**（没有这一行），仓库里的当前版本已经加上了。
22 个 `.py` 全部用 `git mv` 迁移，git 识别为重命名，**历史没丢**。

### 实测校验

用系统 Python 3.12 跑了一遍交互测试（添加 → 查看 → 退出），功能正常。
**测试数据已还原**，你原有的 2 条联系人未受影响。

### 仓库状态（2026-09-26 21:45 核实）

- 最新提交：`8697439 refactor: 代码按天分文件夹（dayNN/），修正数据文件路径`
- 本地与远程**完全同步**（`## main...origin/main`）
- 笔记里"未提交 Day 9~14""未推送 5+ 个 commit"的信息**已过时**——Day 9~13 前几轮就推完了，
  Day 14 的 `c08cdb6` 也在本次重构时一并推上去了

### 待办

- 更新 `大数据开发学习规划-每日清单.xlsx`：第 14 天 → 2026-09-26 / 已完成
- README 进度已补到 Day14 ✅
- `new_folder/` 是 Day13 练习留下空目录，未处理
