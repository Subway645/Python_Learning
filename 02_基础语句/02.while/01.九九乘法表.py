#打印九九乘法表
#定义外层循环变量
i = 1
while i <= 9:
    #定义内层循环变量
    j = 1
    while j <= i:
        print(f"{i}*{j}={i * j}",end=" ")
        j+=1
    print()
    i+=1
