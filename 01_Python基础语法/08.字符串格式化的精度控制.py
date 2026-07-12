#使用%m.n控制
#m:控制宽度，要求是数字，设置的宽度小于数字自身时不生效
#n:控制小数点精度，要求是数字，会进行小数的四舍五入

price = 35
message = "价格是%5d元" % price ##输出为[空格][空格][空格]35
print(message)
price = 11.345
message = "价格是%7.2f元" % price  ##输出为[空格][空格]11.35
print(message)

