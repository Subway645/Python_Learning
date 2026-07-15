# 集合：不支持重复元素，乱序（不支持下标索引访问）

#定义集合
my_set = {"Tom","Jerry","Missy","Tom"}
my_set_empty = set()  #定义空集合
print(f"1: {my_set}, {type(my_set)}")
print(f"2: {my_set_empty}, {type(my_set_empty)}")

# 添加新元素
my_set.add("Ham")
my_set.add("Tom")
print(f"3: {my_set}")

# 移除元素
my_set.remove("Tom")
print(f"4: {my_set}")

# 随机取出元素
element = my_set.pop()
print(f"5: 集合被取出元素{element}, 取出元素后：{my_set}")

# 清空集合
my_set.clear()
print(f"6: {my_set}")

# 取两个集合的差集
# 集合1.difference(集合2),功能：取出集合1和集合2的差集（集合1有而集合2没有）
# 结果：得到一个新集合，原集合不变
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2)
print(set3)
print(set1,set2)


# 消除两个集合的差集
# 在集合1中消除和集合2相同的元素
set1.difference_update(set2)
print(f"消除差集后，集合1结果：{set1}")
print(f"消除差集后，集合2结果：{set2}")

#两个集合合并
set3 = set1.union(set2)
print(f"两集合合并结果：{set3}")

#统计集合元素数量len()
num = len(set3)
print(f"集合中元素数量有：{num}个")

#集合的遍历
#不支持下标索引，不能用while循环
set1 = {1,2,3,4,5}
for element in set1:
    print(element,end = " ")