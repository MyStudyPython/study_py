"""
lambda 表达式（匿名函数），找一行代码实现定义简单的函数

匿名函数，则是基于`lambda`表达式实现定义一个可以没有名字的函数

基于Lambda定义的函数格式为：`lambda 参数:函数体`

-   匿名函数支持任意参数

    ``` python
    lambda x: 函数体
    lambda x1,x2: 函数体
    lambda *args, **kwargs: 函数体
    ```

-   匿名函数只支持函数题为单行的代码

    ``` python
    f1 = lambda x:x+100
    ```

-   默认将函数体单行代码执行的结果返回

    ``` python
    func = lambda x: x + 100
    v1 = func(10)
    print(v1) # 110
    ```

    在编写匿名函数时，由于受限函数体只能写一行，所以匿名函数只能处理非常简单的功能，可以快速并简单的创建函数
"""


def func():
    return 123


# func是函数名（变量）
# lambda 参数: 函数体，   函数体中写了123，内部自动会执行一个retrun
func = lambda: 123


def func(a1, a2):
    return a1 + a2


func = lambda a1, a2: a1 + a2


def func(data_string):
    return data_string.upper()


func = lambda data_string: data_string.upper()

"""
注意：
 - lambda 内部自动return
 - return 后面生成的是什么，返回的就是什么
"""
data = []
v1 = data.append(123)  # None
v2 = data.append(456)  # None


def func(data_list):
    return data_list.append(999)


res = func([123, 456, 789])  # None

func = lambda data_list: data_list.append(999)

value = func([123, 456, 789])  # None

"""
案例一：看代码，写成打印的值
"""
f1 = lambda data: data.replace("中国", "四川")
res = f1("中国联通")  # 四川联通
