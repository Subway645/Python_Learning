def test_func(compute):
    result = compute(1, 2)
    print(type(compute))
    print(result)

def compute_1(x, y):
    return x + y

#调用，并传入函数
test_func(compute_1)