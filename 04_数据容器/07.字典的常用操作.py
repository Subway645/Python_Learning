my_dict = my_dict1 = {"张三":99, "李四":88, "王五":77};
# 新增元素
my_dict["赵六"] = 66
print(f"新增元素后，结果：{my_dict}")

# 更新元素
my_dict["李四"] = 96
print(f"更新元素后，结果：{my_dict}")

# 删除元素
score = my_dict.pop("赵六")
print(f"字典中被移除了一个元素，结果是：{my_dict}，赵六的考试分数是{score}")

# 清空元素
my_dict.clear()
print(f"字典被清空，内容是：{my_dict}")

# 获取全部的Key
my_dict = my_dict1 = {"张三":99, "李四":88, "王五":77};
keys = my_dict.keys()
print(f"字典的全部Keys是：{keys}，类型是{type(keys)}")

# 遍历字典
# 方式一
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict[key]}")
# 方式二：直接对字典进行for循环，每一次循环都是直接得到key
print()
for key in my_dict:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict[key]}")

# 统计字典内的元素数量
num = len(my_dict)
print(f"字典内的元素数量是{num}")