# 起始余额默认为1000元
money = 1000
name = None

# 要求客户输入姓名
name = input("您好，请输入您的姓名：")

# 定义余额查询函数
def query(show_head):
    if show_head:
        print("----------余额----------")
    print(f"{name}，您好，您的余额剩余：{money}元")

# 定义存款函数
def saving(add):
    global money
    money += add
    print("----------存款----------")
    print(f"{name}，您好，您的存款{add}元成功")
    query(False)

# 定义取款函数
def get_money(num):
    global money
    money -= num
    print("----------取款----------")
    print(f"{name}，您好，取款{num}元成功")
    query(False)

# 定义主菜单函数
def main():
    print("----------主菜单---------")
    print(f"{name}，您好，请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return int(input("请输入您的选择："))

#设置无限循环，确保函数不会退出
while True:
    choice = main()
    if choice == 1:
        query(True)
        continue
    elif choice == 2:
        add = int(input("请输入您的存款金额："))
        saving(add)
        continue
    elif choice == 3:
        num = int(input("请输入您的取款金额："))
        get_money(num)
        continue
    else:
        print("程序退出")
        break
