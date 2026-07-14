mylist = ["Tom","Jerry","Ham"]
# 1. 查找某元素在列表内的下标索引
index = mylist.index("Jerry")
print(f"Jerry在列表中的下标索引值是：{index}")

# 2. 修改特定下标索引值
mylist[0] = "Tommy"
print(f"列表被修改元素后，结果是{mylist}")

# 3. 在指定下标位置插入新元素
mylist.insert(1, "Sam")
print(mylist) # ["Tom","Sam","Jerry","Ham"]

# 4. 追加单个元素
mylist.append("Dave") # ["Tom","Sam","Jerry","Ham","Dave"]
print(mylist)

# 5. 追加一批元素
mylist2 = [1,2,3]
mylist.extend(mylist2)
print(mylist) # ["Tom","Sam","Jerry","Ham","Dave",1,2,3]

# 6.1 删除元素——del 01.列表[下标]
del mylist[1]
print(mylist) # ["Tom","Jerry","Ham","Dave",1,2,3]
# 6.2 删除元素——01.列表.pop(下标)
element = mylist.pop(2)
print(f"弹出的元素是{element},现在列表为{mylist}") # ["Tom","Jerry","Dave",1,2,3]

# 7. 删除某元素在列表中的第一个匹配项
mylist = [1,2,3,2,4]
mylist.remove(2)
print(mylist) # [1, 3, 2, 4]

# 8. 清空列表
mylist.clear()
print(mylist) # []

# 9. 统计列表中某元素的数量
mylist = [1,2,3,2,4]
count = mylist.count(2)
print(f"元素2出现了{count}次") # 2

# 10. 统计列表中全部元素的数量
length = len(mylist)

