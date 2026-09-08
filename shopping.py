# 要做的四件事：
# 1带编号打印购物车
# 2输入想买的商品 → append 加入
# 3输入想删的商品 → remove 删除
# 4打印最终购物车和数量
cart = ["苹果", "牛奶", "面包"]
for i in range(3):
    print(f"{i+1}.{cart[i]}")
new_name = input("请输入要买的商品：")

if new_name in cart:
    cart.append(new_name)
    cart.remove(new_name)

name = input("请输入想删掉的商品：")
if name in cart:
    cart.remove(name)
    print(f"已删除{name}")
else:
    print("购物车里没有这个商品")

print(cart)

