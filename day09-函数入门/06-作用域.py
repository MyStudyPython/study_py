"""
当我们每次执行一次函数时，都会为此执行的过程创建一块内存（调用栈）

并发编程 - 多线程 在035.多线程开发中可以查看

1. 作用域基础
- 作用域，理解成一块内存区域，只要在这个区域就可以共享这个区域的数据
- 在python中，在执行函数，就会为函数创建一个作用域
- python代码只要运行，就会有一个全局的作用域   （打断点十分明显）

2. 关于变量 --- 全局和局部
- 全局变量，在非函数中定义的（py文件顶层）
- 局部变量，在函数中定义变量

潜规则：
定义全局变量时，要用大写，多个单词用下划线连接

3. global 关键字
global 是用在函数中，用于表示此变量不是新创建的数据，而是全局变量中的数据 --- 地址指向相同
"""

"1.作用域基础"
name = "害"
age = 123
if True:
    email = "test@example.com"
else:
    gender = "male"

for i in range(10):
    pass

# print(gender) # 报错，其他可以
# print(age) # 123
age = 100
# print(age) # 100，直接修改了全局变量age


name = "慢慢来一个一个做"


def func():
    v1 = 100
    v2 = 200
    v3 = v1 + v2
    # print(v3) # 300


func()


def f1():
    age = 19
    # print(age) # 19


def f2():
    # print(age)  # 全局变量100，要是没有就会报错
    pass


f1()
f2()

"寻找变量的值时，优先回去自己的作用域中找，自己没有的话，去父级作用域找"
# print(v1) # 报错


def f3():
    text = "你是"
    data = text + name
    # print(data) # 你是慢慢来一个一个做


f3()


def f4():
    text = "你是"
    name = "谁"
    data = text + name
    # print(data) # 你是谁


f4()

"""
注意：
在python中函数是一个作用域
在作用域中寻找数据时，优先在自己作用域找，自己没有就去上级作用域找
"""

"""
2. 关于变量 --- 全局和局部 

潜规则：
定义全局变量时，要用大写，多个单词用下划线连接
"""
# 全局变量
NAME = 123
if 1 == 1:
    AGE = 18


def func():
    # 局部变量
    data = 999


"""
3. global 关键字
global 是用在函数中，用于表示此变量不是新创建的数据，而是全局变量中的数据 --- 地址指向相同
"""
NAME = "request"


def func():
    global NAME
    NAME = "response"
    print(NAME)


print(NAME)  # request
func()  # response
print(NAME)  # response

"""
关键
- 内部global之后，变量就是全局变量
- 赋值操作
"""

NAME = "admin"


def func():
    global NAME
    NAME.upper()
    print(NAME)


print(NAME)  # admin
func()  # admin
print(NAME)  # admin

"""
这里跟函数返回值一样，
NAME.upper() 改变的不是原数据，而是生成一份新的数据,所以NAME的值并没有被改变
"""

NAME = [11, 22]


def func():
    global NAME
    NAME.append(666)
    print(NAME)


print(NAME)  # [11, 22]
func()  # [11, 22, 666]
print(NAME)  # [11, 22, 666]
"和函数返回值一样"

NAME = [11, 22]


def func():
    NAME = [33, 44]
    NAME.append(999)
    print(NAME)


print(NAME)  # [11, 22]
func()  # [33, 44, 999]
print(NAME)  # [11, 22]

NAME = [11, 22]


def func():
    global NAME
    NAME = [33, 44]
    NAME.append(999)
    print(NAME)


print(NAME)  # [11, 22]
func()  # [33, 44, 999]
print(NAME)  # [33, 44, 999]
