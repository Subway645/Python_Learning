"""
for循环是将字符串的内容依次取出
for 临时变量 in 待处理数据集:
    循环满足条件时执行的代码
"""

name = "Subway"

for x in name:
    # 将name的内容，逐个取出赋予x临时变量
    # 就可以在循环体内对x进行处理
    print(x,end="")

