# 演示局部变量
def test():
    num = 100
    print(num)
# print(num)会报错

#演示全局变量
num = 200
def test_a():
    print(f"test_a:{num}")
def test_b():
    print(f"test_b:{num}")
test_a()
test_b()
print(num)

#在函数内尝试修改全局变量
num = 200
def test_c():
    print(f"test_c:{num}")
def test_d():
    num = 300   # 局部变量，和函数外的num没有关系，函数外的num值不改变
    print(f"test_d:{num}")
test_c()
test_d()
print(num)

#在函数内使用global修改全局变量
num = 200
def test_e():
    print(f"test_e:{num}")
def test_f():
    #global关键字声明num是全局变量
    global num
    num = 300   # 局部变量，和函数外的num没有关系，函数外的num值不改变
    print(f"test_f:{num}")
test_e()
test_f()
print(num)