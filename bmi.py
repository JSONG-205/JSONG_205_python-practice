height = float(input("请输入身高（米）："))
weight = float(input("请输入体重（公斤）："))
BMI = weight / (height ** 2)

print(f"BMI为{BMI:.1f}")

if BMI < 18.5:
    level = "偏瘦"
elif BMI < 24:
    level = "正常"
elif BMI < 28:
    level = "偏胖"
else:
    level = "肥胖"

print(f"你的BMI为{BMI:.1f}，你属于{level}")