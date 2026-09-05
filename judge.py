num: int = int(input("请输入一个整数："))

# 第一组：判断正负零（三选一）
if num > 0:
    print("这是正数")
elif num < 0:
    print("这是负数")
else:
    print("这是零")

# 第二组：判断奇偶（二选一）
if num % 2 == 0:
    print("这是偶数")
else:
    print("这是奇数")