tags = ["Python", "SQL", "Python", "Linux", "SQL", "Hive", "SQL"]

# 1. 去重
unique_tags = set(tags)
print(f"不同标签：{len(unique_tags)} 个")
print(f"去重后：{unique_tags}")

# 2. 统计每个标签出现次数
for tag in unique_tags:
    count = tags.count(tag)
    print(f"{tag} 出现 {count} 次")