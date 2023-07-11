"""
global关键字 补充
默认情况下，在局部作用域对全局变量只能进行：读取和修改内部元素（可变类型），无法对全局变量进行重新赋值

案例：在局部作用域中修改全局变量 -\> 可变类型
"""

COUNTRY = "中国"
CITY_LIST = ["北京", "上海", "深圳"]


# print(CITY_LIST, id(CITY_LIST))  # ['北京', '上海', '深圳'] 2511269560064
def download():
    url = "http://www.xxx.com"
    print(CITY_LIST, id(CITY_LIST))  # ['北京', '上海', '深圳'] 2511269560064
    "指针指向的空间不能变，但可变类型空间内部的值可以变,所以上面 CITY_LIST 是 ['北京', '上海', '深圳']"
    CITY_LIST.append("广州")
    CITY_LIST[0] = "南京"
    print(CITY_LIST, id(CITY_LIST))  # ['南京', '上海', '深圳', '广州'] 2511269560064


download()
print(CITY_LIST, id(CITY_LIST))  # ['南京', '上海', '深圳', '广州'] 2511269560064

"虽然在可变类型的情况下，局部作用域可以修改可变类型的值，但是由于无法修改指针指向的内存地址，所以无法重新赋值"

COUNTRY = "中国"
CITY_LIST = ["北京", "上海", "深圳"]


def download():
    url = "http://www.xxx.com"
    # 不是对全部变量赋值，而是在局部作用域中又创建了一个局部变量 CITY_LIST 。
    CITY_LIST = ["河北", "河南", "山西"]
    print(CITY_LIST)


download()
print(CITY_LIST)  # ["北京","上海","深圳"]

"想要在局部作用域中对全局变量重新赋值，则可以基于 `global`关键字实现"

COUNTRY = "中国"
CITY_LIST = ["北京", "上海", "深圳"]


def download():
    url = "http://www.xxx.com"
    global CITY_LIST  # 指示CITY_LIST使用的是全局变量
    CITY_LIST = ["河北", "河南", "山西"]
    print(CITY_LIST)
    global CHINA  # 定义全局变量
    CHINA = "中华人民共和国"


download()
print(CITY_LIST)  # ['河北', '河南', '山西']
print(CHINA)  # 中华人民共和国
