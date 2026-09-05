grade = float(input("请输入考试成绩："))
if grade<=100:
    if grade >= 90:
        level = "优秀"
    elif grade >= 80:
        level = "良好"
    elif grade >= 70:
        level = "中等"
    elif grade >= 60:
        level = "及格"
    elif grade >= 0:
        level = "不及格"
    else :
        level = "分数不合法"

else :
    level = "分数不合法"

print(f"你的成绩为{grade:.1f}，等级为{level}")