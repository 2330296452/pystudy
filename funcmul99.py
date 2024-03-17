def output_result(i):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {j * i:2d}", end="  ")


for i in range(1, 10):
    output_result(i)
    print()
print()


def multip(x, y):
    """
    计算两个数的乘积
    :param x: 数字1
    :param y: 数字2
    :return: 两个数的乘积
    """
    return x * y


for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {multip(j, i):2d}", end="  ")
    print()
print()


def table_multi(range, i=1, j=1):
    """
    递归输出乘法表
    :param range: 行数
    :param i: 当前行
    :param j: 当前列
    :return: None
    """
    if i > range:
        return
    if j <= i:
        print(f"{j} * {i} = {j*i:2d}", end="  ")
        table_multi(range, i, j + 1)
    else:
        print()
        table_multi(range, i + 1, 1)

table_multi(9)
print()
