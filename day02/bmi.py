def calc_bmi(height,weight):
    return weight / (height ** 2)

def get_bmi_level(bmi):
    """根据 BMI 值返回等级"""
    if bmi < 18.5:
        return "偏瘦"
    elif bmi < 24:
        return "正常"
    elif bmi < 28:
        return "偏胖"
    else:
        return "肥胖"

height = float(input("请输入身高（米）："))
weight = float(input("请输入体重（公斤）："))
BMI = calc_bmi(height,weight)

print(f"BMI为{BMI:.1f}")
level = get_bmi_level(BMI)
print(f"你的BMI为{BMI:.1f}，你属于{level}")