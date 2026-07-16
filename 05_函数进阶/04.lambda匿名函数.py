"""
def:定义有名称函数，可以基于名称重复使用
lambda:定义匿名函数，只可临时使用一次
语法：
lambda 传入参数:函数体（一行代码，且只能写一行，不要写return，默认使用return）
"""

def test_func(compute):
    result = compute(1, 2)
    print(type(compute))
    print(result)

test_func(lambda x, y:x + y)