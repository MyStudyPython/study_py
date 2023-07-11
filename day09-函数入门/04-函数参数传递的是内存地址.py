"""
在python中为我们提供了一个函数`id()`来查看值的内存地址(以十进制展示)

函数在传递参数时，默认不会重新创建一份数据，
在赋值给函数中的参数，而是同时指向同一块内存。

参数传递是：
引用、内存地址




Python参数的这一特性有两个好处：

-   节省内存
-   对于可变类型且函数中修改元素的内容，所有的地方都会修改。可变类型：列表、字典、集合


1. 函数参数的默认值 
Python在创建函数(未执行)时，如果发现函数的参数中有默认值，则在函数内部会创建一块区域并赋值这个默认值
当执行函数向默认值区域传值的时候，则让b指向新传入的值的地址

2. 动态参数的补充
在定义函数时可以用 `*和**`，其实在执行函数时，也可以用
-   形参固定，实参用`*和**`
"""


def demo(b):
    # print(id(b))  # 140530256566448
    pass


a = 123
# print(id(a))  # 140530256566448
demo(a)


def func(a1):
    a1.upper()
    # print(id(a1)) # 1878614870064
    # print(id(a1.upper())) # 1878615344112


v1 = "hhh"
func(v1)

# print(id(v1)) # 1878614870064
# print(v1) # hhh


"""
注意：
a1,v1是同一块内存地址，但由于字符串是不可变类型
a1.upper() 生成新的值 但是没有返回
"""


def func(a1):
    a1.append(666)


v1 = [11, 22, 33]
func(v1)

# print(v1)  # [11, 22, 33, 666]

"""
注意：
a1,v1是同一块内存地址，但由于列表是可变类型
a1.append() 在原列表中追加数据。
"""

"""
- 函数传递参数时，默认传递是内存地址/引用（不会重新拷贝一份数据再传递）
- 一定要注意参数传递时可变/不可变类型：函数内部执行操作时，是重新生成数据；修改原数据
"""
