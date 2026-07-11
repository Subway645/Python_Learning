#方式1：使用print直接输出
print(type("赛百味"))
print(type(645))
print(type("c"))
print(type(11.23))

#方式2：使用变量存储type()语句的结果
string_type = type("赛百味")
print(string_type)
print(type(string_type))

#方式3：使用type(),查看变量中存储的数据类型信息
name="赛百味"
name_type=type(name)
print(name_type)
name=1
name_type=type(name)
print(name_type)