# 通过下标索引取值
my_str = "tom and jerry"
value1 = my_str[2] # m
value2 = my_str[-7] # d
print(value1,value2)

# 和元组一样，字符串是一个无法修改的数据容器

# index方法
value = my_str.index("and")
print(f"在字符串{my_str}中查找and，其起始下标是：{value}")

# replace方法——替换
# 语法：字符串.replace(字符串1, 字符串2)
# 功能：将字符串的全部：字符串1，替换为字符串2
# 注意：不是修改字符串本身，而是得到一个新的字符串
my_str = "name1 and name2"
new_my_str = my_str.replace("name", "姓名")
print(my_str)
print(new_my_str)

# split方法——分割
# 语法：字符串.split(分隔符字符串）
# 功能：按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象
# 注意：字符串本身不变，而是得到一个新的列表对象
my_str = "tom and jerry"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}进行split切分后得到：{my_str_list},类型是{type(my_str_list)}")

# strip方法——规整操作（去除前后指定字符串）
# 语法：字符串.strip(字符串)
my_str = " tom and jerry "
print(my_str.strip())
# 注意：传入的"12"其实是："1"和"2"都会被移除，按照单个字符
my_str = "12tom and jerry21"
print(my_str.strip("12"))
my_str = "12tom and jerry12"
print(my_str.strip("12"))
my_str = "12tom and jerry11"
print(my_str.strip("12"))

#count方法——统计字符串中某字符串出现的次数
my_str = "name1 and name2"
count = my_str.count("name")
print(count)

#len方法——统计字符串长度
num = len(my_str)
print(num)