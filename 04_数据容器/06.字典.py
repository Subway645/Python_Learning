# 定义字典
my_dict1 = {"张三":99, "李四":88, "王五":77};

# 定义空字典
my_dict2 = {}
my_dict3 = dict()
print(f"字典1的内容是：{my_dict1}，类型：{type(my_dict1)}")
print(f"字典2的内容是：{my_dict2}，类型：{type(my_dict2)}")
print(f"字典3的内容是：{my_dict3}，类型：{type(my_dict3)}")

# 定义重复Key的字典
my_dict1 = {"张三":99, "张三":88, "王五":77};
print(f"重复Key字典的内容是：{my_dict1}")

# 字典和集合一样，不能使用下标索引，但可基于Key获取Value
my_dict1 = {"张三":99, "李四":88, "王五":77};
score = my_dict1["李四"]
print(f"李四的考试分数是{score}分")

#字典的嵌套（Key和Value可为任意数据类型，Key不可为字典）
stu_dict = {
    "张三":{
        "语文":87,
        "数学":97,
        "英语":98
    }, "李四":{
        "语文":92,
        "数学":86,
        "英语":98
    }, "王五":{
        "语文":83,
        "数学":92,
        "英语":91
    }
}
print(f"学生的考试信息是：{stu_dict}")

# 从嵌套字典中获取数据
# 查看张三语文信息
score = stu_dict["张三"]["语文"]
print(f"张三的语文成绩是{score}分")