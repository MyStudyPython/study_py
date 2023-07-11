"""
在开发过程中，我们希望函数可以帮助我们实现某个功能，但让函数实现某功能之后有时也需要有一些结果需要反馈给我们。

关于返回值
1.返回值可以是任何类型
2.函数没有返回值，默认返回None
3.在函数的执行过程中，一旦遇到return，立即结束当前函数的执行并返回值  (打断点可以查看)   
"""

"1.返回值可以是任何类型"


def f1():
    return (11, 22, 33, 44)


res1 = f1()  # (11, 22, 33, 44)


# 这个也是元组
def f2():
    return 11, 22, 33, 44  # (11, 22, 33, 44)


res2 = f2()  # (11, 22, 33, 44)

"2.函数没有返回值，默认返回None"


def f3():
    res = (11, 22, 33, 44)


res3 = f3()  # None

"3.在函数的执行过程中，一旦遇到return，立即结束当前函数的执行并返回值  (打断点可以查看)"


def f4():
    v1 = 123
    v2 = 456
    return 999
    v3 = 180


res4 = f4()  # 999


def f5():
    for i in range(100):
        return


res5 = f5()  # 0


def f6():
    for i in range(100):
        break


res6 = f6()  # None


def f7():
    for i in range(100):
        continue


res7 = f7()  # None


def f8():
    for i in range(100):
        print(i)
    print("END")


res8 = f8()  # None

"在函数中可以只写return，后面没有值也是返回None"


def f9():
    print(1)
    print(2)
    return
    print(3)


res9 = f9()  # None

"""
练习题 1：
定义一个函数，可以接受任意个参数（位置传参+整数），
在函数的内部将将所有的参数相加并获得结果，返回给函数的调用者
"""


def add_arg(*arg):
    print("==================", arg)
    res = 0
    for item in arg:
        res += item
    return res


v1 = add_arg(1, 2, 35, 6, 7888, 4444)  # 12376
