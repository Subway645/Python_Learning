"""
序列（列表、元组、字符串）支持切片操作
切片：从一个序列中，取出一个子序列
语法：序列[起始下标:结束下标:步长]
起始下标留空视作从头开始
结束下标（不包含本身）表示何处结束，留空视作截取到结尾

注意：此操作不会影响序列本身，而是会得到一个新的序列
"""

# 对list切片，从1开始，4结束，步长1
my_list = [0,1,2,3,4,5,6]
result = my_list[1:4] # 步长默认为1，可省略不写
print(result)

# 对tuple进行切片，从头开始，到最后结束，步长1
my_tuple = (0,1,2,3,4,5,6)
result = my_tuple[:]
print(result)

# 对str切片，从头开始，到最后结束，步长2
my_str = "0123456"
result = my_str[::2]
print(result)


# 对str进行切片，从头开始，到最后结束，步长-1
result = my_str[::-1]
print(result)

# 对list进行切片，从3开始，到1结束，步长为-1
result = my_list[3:1:-1]
print(result)

#对tuple进行切片，从头开始，到尾结束，步长为-2
result = my_tuple[::-2]
print(result)