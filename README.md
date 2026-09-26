# JSONG_205_python-practice

大数据开发学习之路 · Python 编程地基

## 学习者

- GitHub：JSONG-205
- 起点：零基础
- 节奏：每天 2 小时，每天有代码产出
- 目标：6 个月走完大数据开发路线（Python → Linux → SQL → Hadoop → Hive → Spark → 离线数仓 → 实时）

## 已完成

| 天 | 主题 | 产出文件 |
|---|---|---|
| Day 1 | 环境搭建与第一行代码 | `day01/hello.py` |
| Day 2 | 变量与数据类型 | `day02/intro.py` `calc.py` `bmi.py` |
| Day 3 | 条件判断 | `day03/judge.py` `grade.py` |
| Day 4 | 循环 | `day04/multiplication.py` `guess.py` |
| Day 5 | 列表 list | `day05/scores.py` `shopping.py` `numbers.py` |
| Day 6 | 字典 dict 与集合 set | `day06/student.py` `students.py` `set_demo.py` `day06_practice.py` |
| Day 7 | 复盘与 Git | 仓库整理、`.gitignore`、本 README |
| Day 8 | 函数 | `day08/day08_practice.py`；`scores.py` `bmi.py` `numbers.py` `students.py` `calc.py` 重构为函数 |
| Day 9 | 字符串 | `day09/day09_practice.py` |
| Day 10 | 文件读写 | `day10/day10_practice.py` + `day10/data/` |
| Day 11 | JSON 数据 | `day11/day11_practice.py` + `day11/data/` |
| Day 12 | 异常与调试 | `day12/day12_practice.py` |
| Day 13 | 模块与包 | `day13/day13_practice.py` |
| Day 14 | 阶段小测 | `day14/contacts.py`（命令行通讯录） |

## 目录结构

```
python-practice/
├── notes/                  # 学习笔记 day01 ~ day13 + 00-重要知识点手册.md
├── day01/                  # 第 1 天
│   └── hello.py
├── day02/
│   ├── intro.py
│   ├── calc.py
│   └── bmi.py
├── day03/
│   ├── judge.py
│   └── grade.py
├── day04/
│   ├── multiplication.py
│   └── guess.py
├── day05/
│   ├── scores.py
│   ├── shopping.py
│   └── numbers.py
├── day06/
│   ├── student.py
│   ├── students.py
│   ├── set_demo.py
│   └── day06_practice.py
├── day08/
│   └── day08_practice.py
├── day09/
│   └── day09_practice.py
├── day10/
│   ├── day10_practice.py
│   └── data/               # txt 测试文件（运行生成）
├── day11/
│   ├── day11_practice.py
│   └── data/               # json 文件（运行生成）
├── day12/
│   └── day12_practice.py
├── day13/
│   └── day13_practice.py
├── day14/
│   ├── contacts.py
│   └── contacts.json
├── README.md
└── .gitignore
```

> **说明**
> - Day 7 是复盘日，没有独立代码目录。
> - 各天代码按天分文件夹；`data/` 下的文件是程序运行生成的，已被 `.gitignore` 排除。

## 怎么运行

需要 Python 3.12+。

```bash
python dayNN/文件名.py
```

例如：

```bash
python day04/guess.py
```

脚本开头会自动把工作目录切到自身所在目录，所以**从哪个目录运行都能找到同级的 `data/` 文件**。

## 学习笔记

每天的笔记在 `notes/` 目录，包含：

- 今天做到了什么
- 核心概念
- 语法速查
- 今天的代码
- 踩坑记录
- 自检清单

另外 `notes/00-重要知识点手册.md` 是按主题汇总的速查手册（不按天），复习时看这一份就够。

## 下一步

- Day 15~21：类与对象、pandas
- Day 22+：Linux → SQL → Hadoop → Hive → Spark → 离线数仓 → 实时

完整计划见《大数据开发 6 个月 · 每日学习清单》。
