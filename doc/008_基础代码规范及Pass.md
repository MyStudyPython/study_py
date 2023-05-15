# 1 基础代码规范 {#1-基础代码规范}

为了保证代码的良好阅读性、代码执行效率，程序员前辈们设计了一套较为通用的代码开发规范，这不是强制性的，也不会导致代码报错，但却是成为优秀程序员所必备，目前所介绍的代码规范在前文章节的基础进行补充

## 1.1 名称命名法 {#11-名称命名法}

在Python开发过程中会创建各种文件夹/文件/变量等，这些命名在基础的pep8规范上，增加了一些规范性规则

-   文件夹，小写 & 小写下划线连接，例如：`commands`、`data_utils`等

-   文件，小写 & 小写下划线连接，例如：`page.py`、`db_convert.py`等

-   变量

    -   全局变量，大写 & 大写下划线连接，例如：`NAME = "武沛齐"`
        、`BASE_NAME = 18`
    -   局部变量，小写 &
        小写下划线连接，例如：`data = [11,22,33]`、`user_parent_id = 9`等

## 1.2 注释 {#12-注释}

为了确保代码的可读性，能够让你自己在以后阅读代码、维护程序的时候不发出：`这是那个菜逼写的`感叹，注释就是至关重要的

-   文件夹注释

    -   文件夹下可以创建一个`__init__.py`的文件，在文件内容实用`""" """`写上注释

        ![image-20201122135126441](https://skystarry-1251157247.cos.ap-chengdu.myqcloud.com/img/image-20201122135126441.png){loading="lazy"}

-   文件注释

    -   使用文件注释，可以介绍该文件的功能模块

        ``` python
        """
        这个文件主要为项目提供工具和转换的功能，初次之外还有日志....
        例如：
        	...
        	...
        	...
        """
        ```

-   代码注释

    -   介绍下方代码功能，一般在代码开头

        ``` python
        name = "edg"
        # 单行注释：name变量与6b进行拼接
        data = name + "6b" 
        print(data)

        """
        多行注释：下方代码，就是瞎几把写的
        交换ab的值
        """
        a = 1
        b = 2
        b,a = a,b
        ```

## 1.3 todo {#13-todo}

对于一个大型系统，通常不会是一个开发阶段，所以可以在代码中写个todo，写入未来在这里的开发计划

todo是基于注释实现的

![image](https://img2023.cnblogs.com/blog/2269668/202302/2269668-20230226222648912-453935906.png){loading="lazy"}

## 1.4 嵌套层数不能过多 {#14-嵌套层数不能过多}

以后写条件语句一定要想办法减少嵌套的层级（最好不要超过3层）。层数多了，代码可读性和运行效率会极差，例如下面的代码，就可以提桶回家了

![image](https://img2023.cnblogs.com/blog/2269668/202302/2269668-20230226222707956-1685818760.png){loading="lazy"}

## 1.5 简单的逻辑先处理 {#15-简单的逻辑先处理}

案例：

``` python
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}
]
for index in range(len(goods)):
    item = goods[index]
    print(index + 1, item['name'], item['price'])

while True:
    num = input("请输入要选择的商品序号(Q/q)：")  # "1"
    if num.upper() == "Q":
        break
    if num.isdecimal():
        num = int(num)
        if 0 < num < 5:
            target_index = num - 1
            choice_item = goods[target_index]
            print(choice_item["name"], choice_item['price'])
        else:
            print("序号范围选择错误")
    else:
        print("用户输入的序号格式错误")
```

可以将简单的逻辑往上提，例如单独使用if语句进行判断输入的格式是否错误，就可以大量减少循环次数和层数

``` python
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}
]
for index in range(len(goods)):
    item = goods[index]
    print(index + 1, item['name'], item['price'])

while True:
    num = input("请输入要选择的商品序号(Q/q)：")  # "1"
    # 先处理简单逻辑，减少了if...else的嵌套
    if num.upper() == "Q":
        break
    if not num.isdecimal():
        print("用输入的格式错误")
        break
    num = int(num)

    if num > 4 or num < 0:
        print("范围选择错误")
        break
    target_index = num - 1
    choice_item = goods[target_index]
    print(choice_item["name"], choice_item['price'])
```

## 1.6 循环 {#16-循环}

减少循环次数，尽量少循环多干事，提高代码效率。

``` python
key_list = []
value_list = []
info = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
for key, value in info.items():
    key_list.append(key)
    value_list.append(value)
```

虽然更简洁，由于`info.keys和info.values`也是循环，会导致效率低

``` python
info = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
key_list = list(info.keys())
value_list = list(info.values())
```

## 1.8 变量和值书写时遵循PEP8规范 {#18-变量和值书写时遵循pep8规范}

``` python
# 推荐
name = "kinght"
age = 20

# 不推荐
name="kinght"
age=10
```

可以使用pycharm的格式化工具进行自动化处理

![image-20211130143912660](https://skystarry-1251157247.cos.ap-chengdu.myqcloud.com/img/image-20211130143912660.png){style="zoom: 50%"}

# 2 知识补充 -\> pass {#2-知识补充----pass}

Python的代码块是基于 `:`
和`缩进`来实现，Python中规定代码块中必须要有代码才算完整，在没有代码的情况下为了保证语法的完整性可以用pass代替，例如：

``` python
# 其他编程语言 -> 其他编程语言通常会使用大括号进行包裹
if 提交{
    ...
}else{
    ....
}

# python -> 需要保证格式完整性
if 条件 : 
    pass # pass等于没有代码，啥都不做
else:
    pass
```