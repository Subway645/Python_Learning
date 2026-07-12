print("该景区儿童免票，成人收费。")
age = input("请输入你的年龄：")
age = int(age)
if age >= 18 | age < 60:
    print("请支付10元。")
elif age < 18:
    print("你好小朋友！")
else:
    print("请支付3元。")
print("祝你游玩愉快！")