"""命令行通讯录
做一个小工具 contacts.py，可以管理联系人。"""

"""功能需求
程序运行时，循环显示菜单："""

"""text
===== 通讯录 =====
1. 添加联系人
2. 查看所有联系人
3. 查找联系人
4. 删除联系人
5. 退出"""

"""请选择：
每个功能的详细要求
1. 添加联系人
输入姓名、电话
存到一个列表里（每个联系人是一个字典）
保存到 contacts.json 文件
2. 查看所有联系人
从文件读取
按行显示：1. 张三 - 13800138000
3. 查找联系人
输入姓名
找到就显示电话；找不到提示"未找到"
4. 删除联系人
输入姓名
找到就删掉并保存到文件；找不到提示"未找到"
5. 退出
结束程序
技术要求（必须用到）
技能	用在哪
函数	每个功能抽成一个函数
列表 + 字典	联系人数据结构
循环	主菜单循环
条件判断	菜单选择
文件读写 + JSON	保存/读取 contacts.json
异常处理	读取文件不存在时不崩
加分项（可选）
添加时判断姓名是否重复
查找时支持模糊匹配
删除前确认"""
#import json
# n = int(input(f"请输入要添加几个联系人"))
# person = []
# try:
#     for i in range(n):
#         name = input("请输入姓名：")
#         phone = input("请输入电话")
#         person.append({"name" : name,"phone" : phone})
#     print(person)
#
#     with open("contacts.json","w",encoding="utf-8")as f:
#         json.dump(person,f,ensure_ascii=False,indent=2)
#
#     with open("contacts.json","r",encoding="utf-8")as f:
#         print(json.load(f))
#
#
# except AttributeError:
#     print("'_io.TextIOWrapper' object has no attribute 'json'")
# except TypeError:
#     print("'str' object cannot be interpreted as an integer")
# finally:
#     print("结束")


import json
import os

# 切换到本文件所在目录，保证 contacts.json 在任何位置运行都能找到
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def load_contacts():
    """从 contacts.json 文件加载联系人列表，文件不存在则返回空列表"""
    if not os.path.exists('contacts.json'):
        return []
    try:
        with open('contacts.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_contacts(contacts):
    """将联系人列表保存到 contacts.json 文件"""
    with open('contacts.json', 'w', encoding='utf-8') as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)


def add_contact(contacts):
    """添加联系人，支持姓名重复检查"""
    name = input("请输入姓名：").strip()
    if not name:
        print("姓名不能为空！")
        return

    # 检查姓名是否已存在
    for c in contacts:
        if c["name"] == name:
            print(f"联系人「{name}」已存在！")
            return

    phone = input("请输入电话：").strip()
    if not phone:
        print("电话不能为空！")
        return

    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)
    print(f"联系人「{name}」添加成功！")


def show_contacts(contacts):
    """显示所有联系人"""
    if not contacts:
        print("通讯录为空！")
        return
    print("\n===== 所有联系人 =====")
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} - {c['phone']}")
    print()


def find_contact(contacts):
    """查找联系人，支持模糊匹配"""
    name = input("请输入要查找的姓名：").strip()
    if not name:
        print("姓名不能为空！")
        return

    results = [c for c in contacts if name in c["name"]]
    if not results:
        print("未找到该联系人！")
    else:
        print(f"\n找到 {len(results)} 个匹配结果：")
        for c in results:
            print(f"  {c['name']} - {c['phone']}")
        print()


def delete_contact(contacts):
    """删除联系人，删除前确认"""
    name = input("请输入要删除的姓名：").strip()
    if not name:
        print("姓名不能为空！")
        return

    for i, c in enumerate(contacts):
        if c["name"] == name:
            confirm = input(f"确认删除「{name}」吗？(y/n)：").strip().lower()
            if confirm == 'y':
                contacts.pop(i)
                save_contacts(contacts)
                print(f"联系人「{name}」已删除！")
            else:
                print("已取消删除。")
            return

    print("未找到该联系人！")


def main():
    """主函数：显示菜单并分发操作"""
    contacts = load_contacts()

    while True:
        print("===== 通讯录 =====")
        print("1. 添加联系人")
        print("2. 查看所有联系人")
        print("3. 查找联系人")
        print("4. 删除联系人")
        print("5. 退出")
        choice = input("请选择：").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            show_contacts(contacts)
        elif choice == '3':
            find_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("再见！")
            break
        else:
            print("无效选择，请重新输入！")


if __name__ == '__main__':
    main()