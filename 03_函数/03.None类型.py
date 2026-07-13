"""
若函数没有使用return语句
实际上返回了：None，该字面量的类型是<class'NoneType'>
"""

def fun():
    print:("你好")
result = fun()
print(result)
print(type(result))

"""
在if判断中，None等同于False
"""
def check_age(age):
    if age > 18:
        return "Success"
    else:
        return None
result = check_age(16)
if not result:
    print("未成年，不可进入")

"""
用于声明无初始内容的变量
"""
name = None