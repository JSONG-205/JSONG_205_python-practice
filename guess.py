#猜随机数
import random
secret = random.randint(1, 100)
flag = 1
num = int(input("来猜一个数："))
count = 1
if num < secret:
    print("太小了")
elif num > secret:
    print("太大了")
else:
    print("牛逼，一发入魂")
while num != secret:
    num = int(input("继续猜："))
    count += 1
    if count >= 7:
        print(f"小妹妹你太拉了！答案是{secret}")
        break
    if num < secret:
        print("太小了")
    elif num > secret:
        print("太大了")
    else:
        print("小妹妹你挺牛逼克拉斯啊，这都猜对了")
