# 导入 json 标准库，用于读写 JSON 格式的文件
import json
# 导入 os 标准库，用于检查文件是否存在（避免直接读取不存在的文件导致报错）
import os


def load_contacts():
    """从 contacts.json 文件加载联系人列表，文件不存在则返回空列表"""
    # 先检查 contacts.json 文件是否已经存在，如果不存在，直接返回一个空列表，避免后续读取报错
    if not os.path.exists('contacts.json'):
        return []
    try:
        # 以只读模式（'r'）和 UTF-8 编码打开 contacts.json 文件，并将其赋值给变量 f
        with open('contacts.json', 'r', encoding='utf-8') as f:
            # 使用 json.load() 解析文件内容，将 JSON 数据转换为 Python 的列表/字典并返回
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        # 如果文件读取时出现 JSON 格式错误，或者文件突然找不到了，捕获异常并返回空列表，防止程序崩溃
        return []


def save_contacts(contacts):
    """将联系人列表保存到 contacts.json 文件"""
    # 以写入模式（'w'）和 UTF-8 编码打开 contacts.json 文件（如果文件不存在会自动创建，存在则覆盖原内容）
    with open('contacts.json', 'w', encoding='utf-8') as f:
        # 使用 json.dump() 将 Python 的 contacts 列表写入文件
        # ensure_ascii=False 保证中文字符能正常显示，而不是被转义成 \uXXXX
        # indent=2 让生成的 JSON 文件带有缩进，方便人工查看和调试
        json.dump(contacts, f, ensure_ascii=False, indent=2)


def add_contact(contacts):
    """添加联系人，支持姓名重复检查"""
    # 获取用户输入的姓名，并使用 .strip() 去掉首尾可能误输入的空格
    name = input("请输入姓名：").strip()
    # 如果去掉空格后姓名为空字符串，提示用户并直接返回，不执行后续添加逻辑
    if not name:
        print("姓名不能为空！")
        return

    # 遍历当前的联系人列表 contacts，检查是否有联系人的 name 和输入的姓名完全一致
    for c in contacts:
        if c["name"] == name:
            # 如果姓名已存在，提示用户并直接返回，避免添加重复联系人
            print(f"联系人「{name}」已存在！")
            return

    # 获取用户输入的电话，同样去掉首尾空格
    phone = input("请输入电话：").strip()
    # 如果电话为空，提示用户并返回
    if not phone:
        print("电话不能为空！")
        return

    # 将包含姓名和电话的字典追加到 contacts 列表中
    contacts.append({"name": name, "phone": phone})
    # 数据修改后，立刻调用 save_contacts 函数将最新列表保存到文件中，实现数据持久化
    save_contacts(contacts)
    # 打印添加成功的提示信息
    print(f"联系人「{name}」添加成功！")


def show_contacts(contacts):
    """显示所有联系人"""
    # 如果联系人列表为空，提示用户通讯录为空并返回
    if not contacts:
        print("通讯录为空！")
        return
    # 打印分隔线，美化输出界面
    print("\n===== 所有联系人 =====")
    # 使用 enumerate 遍历列表，i 是从 1 开始的序号，c 是当前的联系人字典
    for i, c in enumerate(contacts, 1):
        # 按 "序号. 姓名 - 电话" 的格式打印每个联系人的信息
        print(f"{i}. {c['name']} - {c['phone']}")
    # 打印一个空行，让界面看起来更清爽
    print()


def find_contact(contacts):
    """查找联系人，支持模糊匹配"""
    # 获取用户想要查找的姓名，并去掉首尾空格
    name = input("请输入要查找的姓名：").strip()
    # 如果输入的姓名为空，提示用户并返回
    if not name:
        print("姓名不能为空！")
        return

    # 使用列表推导式进行模糊匹配：只要联系人的姓名中包含用户输入的字串，就加入结果列表
    results = [c for c in contacts if name in c["name"]]
    # 如果结果列表为空，说明没有找到匹配的联系人
    if not results:
        print("未找到该联系人！")
    else:
        # 如果找到了，打印匹配到的数量
        print(f"\n找到 {len(results)} 个匹配结果：")
        # 遍历并打印所有匹配到的联系人信息
        for c in results:
            print(f"  {c['name']} - {c['phone']}")
        # 打印空行美化界面
        print()


def delete_contact(contacts):
    """删除联系人，删除前确认"""
    # 获取用户想要删除的联系人姓名，并去掉首尾空格
    name = input("请输入要删除的姓名：").strip()
    # 如果输入为空，提示并返回
    if not name:
        print("姓名不能为空！")
        return

    # 遍历联系人列表，同时获取索引 i 和联系人字典 c
    for i, c in enumerate(contacts):
        # 如果找到了姓名完全匹配的联系人
        if c["name"] == name:
            # 为了防止误删，先让用户输入 y 或 n 进行二次确认
            confirm = input(f"确认删除「{name}」吗？(y/n)：").strip().lower()
            # 如果用户输入了 'y'（转为小写后比较），执行删除操作
            if confirm == 'y':
                # 使用 pop(i) 根据索引从列表中移除该联系人
                contacts.pop(i)
                # 删除后立刻保存文件，确保数据同步
                save_contacts(contacts)
                print(f"联系人「{name}」已删除！")
            else:
                # 如果用户没有输入 'y'，提示已取消删除
                print("已取消删除。")
            # 处理完（无论是否删除）直接返回，结束函数
            return

    # 如果循环结束都没有找到匹配的姓名，提示未找到
    print("未找到该联系人！")


def main():
    """主函数：显示菜单并分发操作"""
    # 程序启动时，先从文件加载已有的联系人数据到内存中
    contacts = load_contacts()

    # 开启一个无限循环，让菜单可以一直显示，直到用户主动选择退出
    while True:
        # 打印通讯录的主菜单界面
        print("===== 通讯录 =====")
        print("1. 添加联系人")
        print("2. 查看所有联系人")
        print("3. 查找联系人")
        print("4. 删除联系人")
        print("5. 退出")
        # 获取用户输入的菜单选项，并去掉首尾空格
        choice = input("请选择：").strip()

        # 根据用户输入的数字字符串，分发到对应的功能函数
        if choice == '1':
            add_contact(contacts)      # 调用添加联系人函数
        elif choice == '2':
            show_contacts(contacts)    # 调用查看所有联系人函数
        elif choice == '3':
            find_contact(contacts)     # 调用查找联系人函数
        elif choice == '4':
            delete_contact(contacts)   # 调用删除联系人函数
        elif choice == '5':
            # 如果用户选择 5，打印告别语
            print("再见！")
            # 使用 break 跳出 while 循环，结束程序
            break
        else:
            # 如果用户输入了 1-5 以外的内容，提示无效并让用户重新输入
            print("无效选择，请重新输入！")


# 判断当前脚本是否是直接运行的（而不是被其他文件 import 导入的）
# 如果是直接运行，则执行 main() 函数启动程序
if __name__ == '__main__':
    main()