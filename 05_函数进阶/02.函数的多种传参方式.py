def user_info(name, age, gender):
    print(f"姓名是：{name}，年龄是：{age}，性别是：{gender}")

# 位置传参
user_info('张三', 20, '男')

# 关键字参数
user_info(name = '李四', age = 21, gender = '女')
user_info(age = 17, gender = '女', name = '王五')
user_info('小明', gender = '男', age = '15')

# 缺省参数（要从右往左）
def user_info(name, age, gender='男'):
    print(f"姓名是：{name}，年龄是：{age}，性别是：{gender}")

user_info('小华',13)

# 不定长参数-位置不定长，*号
# 不定长定义的形式参数会作为元组存在，接收不定长数量的参数传入
def user_info(*args):
    print(f"args参数类型是：{type(args)}，内容是：{args}")
user_info(1,2,3,'小明','男')

# 不定长-关键字不定长，**号
# 不定长定义的形式参数会作为字典存在，接收不定长数量的参数传入
def user_info(**kwargs):   #key-word
    print(f"args参数类型是：{type(kwargs)}，内容是：{kwargs}")
user_info(name = '小明', age = 11, gender = '男')

