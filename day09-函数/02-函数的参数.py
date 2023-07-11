"""
形参与实参
形式参数的含义指的是在函数中占位，在函数编程中能够占位，以便实际参数传递过来后能够有位置进行处理的参数
实参是实际传入参数的值

在执行参数时，传入参数时一般有两种模式：

位置传参
关键字传参
"""


# 定义有三个参数的函数（a1/a2/a3一般称为形式参数-形参）
def my_func(a1, a2, a3):
    result = a1 + a2 - a3
    return result


# 执行函数并传入参数（执行函数传值时一般称为实际参数-实参）
## 有几个形参，在调用时就要有几个实参
## 执行函数并传入参数
"位置传参"
res1 = my_func(1, 6, 8)  # -1

res2 = my_func(7, 8, 3)  # 12

"关键字传参"
res1 = my_func(a1=1, a3=6, a2=8)  # 3

res2 = my_func(a2=7, a3=8, a1=3)  # 2

"""
混合使用

位置参数在前面，关键字参数在后面！！！！
"""
res1 = my_func(1, a3=6, a2=8)  # 3
# res1 = my_func(1, 6, a2=8) #报错 因为a2被位置参数赋值了，就不能用关键字传参再传一次

res2 = my_func(2, a3=8, a2=3)  # -3
# res2 = my_func(2, a3=8, a1=3)  # 报错同理

"""
注意：
1. 函数要求你传入几个参数，你就要传入几个参数
2. 参数传参类型可以为： None、 bool、int、str、list、dist...
3. 混合使用的时候，相同的参数不能赋值两次，
    比如位置参数已占的位置，关键字传参就不能再次传入
"""

"""
练习题1：
定义函数，接受1个字符串类型的参数,函数内部计算字符串中的“a”出现的次数并输出。
"""


def str_func(str):
    count = 0
    for i in str:
        if i == "a":
            count += 1

    return count


res1 = str_func("sdadadayyjhjadanklkkkl")  # 5

"""
练习题2：
定义函数，接受两个参数：字符串--文本，字符串--关键词，计算某一个字符出现的次数
"""


def string_func(str, key):
    count = 0
    for i in str:
        if i == key:
            count += 1
    return count


res2 = string_func("sdadadayyjhjadanklkkkl", "a")  # 5
