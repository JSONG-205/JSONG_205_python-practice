import os

# 切换到本文件所在目录，保证相对路径在任何位置运行都能找到文件
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# import os
# from datetime import datetime, date, timedelta
#
# datetime.now()                        # 当前日期时间
# date.today()                          # 今天的日期
# datetime(2026, 9, 23)                 # 构造指定日期
# datetime.now().strftime("%Y-%m-%d")   # 格式化
# timedelta(days=7)                     # 7 天的间隔
# os.getcwd()              # 当前工作目录
# os.listdir(".")          # 列出目录下的文件
# os.path.exists("data.txt")   # 文件/目录是否存在
# os.mkdir("new_folder")   # 创建目录
# os.path.join("a", "b.txt")   # 拼路径：'a/b.txt'（跨平台）
# import math
# print(math.pi)
# print(math.sqrt(144))
# print(math.pow(2,10))
# print(math.ceil(4.3))
# print(math.floor(4.9))
# import os
# print(os.getcwd())
# print(os.listdir("."))
# print(os.path.exists("day13_practice.py"))
# from datetime import datetime,date,timedelta
# print(datetime.now())
# print(date.today())
# print(date.today()+timedelta (days=7))
# print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# import random
# print(random.randint(1,100))
# print(random.choice(["剪刀","石头","布"]))
# print(random.sample(range(1,50),6))
# lst = [1, 2, 3, 4, 5]
# random.shuffle(lst)
# print(lst)

import requests

response = requests.get("https://api.github.com/users/JSONG-205")
print(response.status_code)

data = response.json()
print(data["name"])
print(data["followers"])