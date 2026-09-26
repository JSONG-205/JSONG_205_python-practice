product = {
    "name": "笔记本电脑",
    "price": 5999,
    "stock": 12,
    "tags": ["数码", "办公", "热销"]
}
# 打印商品名和价格
print(f"{product['name']}{product['price']}元")

# 打印第三个标签（"热销"）
print(product["tags"][2])
# 打 9 折，更新 price，保留 1 位小数
product["price"] = product["price"] * 0.9
print(f"折后价：{product['price']:.1f}")
# 新增 "brand": "联想"
product["brand"] = "联想"
# get() 取 "color"，没有就显示"暂无颜色信息"
print(product.get("color","暂无颜色信息"))

print()
# 订单列表
orders = [
    {"id": 1, "user": "张三", "amount": 120},
    {"id": 2, "user": "李四", "amount": 80},
    {"id": 3, "user": "王五", "amount": 250},
    {"id": 4, "user": "赵六", "amount": 45},
    {"id": 5, "user": "钱七", "amount": 300}
]
# 1 算总金额	累加
total = 0
for s in orders :
    total += s["amount"]
print(f"总金额：{total}")
# 2	算平均金额（保留 1 位小数）	累加 + 除法
print(f"平均金额：{total / len(orders):.1f}")
# 3	找金额最高的订单，打印 user 和 amount	打擂台
top = orders[0]
for s in orders:
    if s["amount"] > top["amount"]:
        top = s
print(f"最高:{top['user']} {top['amount']}")
# 4	统计金额 ≥100 的订单有几笔	计数器
count =0
for s in orders:
    if s["amount"] >= 100 :
        count +=1
print(f"大额订单:{count}笔")
# 5	找出金额 <100 的订单的 user，收进列表	筛选收集
low_users = []
for s in orders:
    if s["amount"] < 100 :
        low_users.append(s["user"])
print(f"小额订单用户{low_users}")

print ()

# C3：标签统计
articles = [
    {"title": "文章A", "tags": ["Python", "SQL"]},
    {"title": "文章B", "tags": ["Python", "Linux"]},
    {"title": "文章C", "tags": ["SQL", "Hive", "SQL"]},
    {"title": "文章D", "tags": ["Python"]}
]

# 1. 收集所有标签
all_tags = []
for s in articles:
    for i in s["tags"]:
        all_tags.append(i)
print(f"所有标签（含重复）：{all_tags}")


# 2. 去重
unique_tags = list(set(all_tags))
print(f"去重后：{unique_tags}")

# 3. 数量
print(f"不同标签：{len(unique_tags)} 个")

# 4. 每个标签出现几次
for t in unique_tags:
    count = all_tags.count(t)
    print(f"{t} 出现 {count} 次")