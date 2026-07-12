print("该景区儿童免票，成人收费。")
print("请输入你的年龄：")
age = input()
age = int(age)
if age >= 18:
    print("您已成年，请支付10元。")
else:
    print("你好小朋友！")
print("祝你游玩愉快！")