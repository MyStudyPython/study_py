"""
其他很多编程语言执行函数时，默认传参时会将数据重新拷贝一份，会浪费内存

提示注意：其他语言也可以通过 ref 等关键字来实现传递内存地址

当然，如果你不想让外部的变量和函数内部参数的变量一致，也可以选择将外部值拷贝一份，再传给函数
"""

import copy


# 可变类型 & 修改内部修改
def func(data):
    data.append(999)


v1 = [11, 22, 33]
new_v1 = copy.deepcopy(v1)  # 拷贝一份数据，把拷贝的数据传入参数
func(new_v1)
# print(v1)  # [11,22,33]

"""
TIPS:python的内存驻留机制
"""


def demo1():
    demo = [1, 2, 3]
    return demo
    # 函数的每次调用结束，都会销毁内部所有的值
    # 所以


res1 = demo1()
res2 = demo1()
# 由于demo1被调用了两次，所以生成了两次demo并将其进行返回赋值
## 两次都各不相同
print(id(res1))  # 2053770228864
print(id(res2))  # 2053770135424


# 但是也有例外
def demo2():
    demo = "123"
    return demo


res3 = demo2()
res4 = demo2()
# 由于python有着变量驻留机制优化内存，对于所有都不可变数据类型可能会存在指向同一内存地址
print(id(res3))  # 2053770266288
print(id(res4))  # 2053770266288

# 变量驻留机制演示
a = "123456"
b = "123456"
print(id(a))  # 2053770266672
print(id(b))  # 2053770266672

"""
1. 函数参数的默认值 
Python在创建函数(未执行)时，如果发现函数的参数中有默认值，则在函数内部会创建一块区域并赋值这个默认值
当执行函数向默认值区域传值的时候，则让b指向新传入的值的地址
"""


def func(a, b=1):
    # print(a,b)
    pass


# 当执行函数但是并未向默认值区域传值的时候，则让b指向函数维护的那个值的地址
func(1)  # 1 1
# 当执行函数向默认值区域传值的时候，则让b指向新传入的值的地址
func(1, 2)  # 1 2

"""
注意：默认参数如果可变会踩坑
【默认参数的值是可变类型 list/dict/set】 & 【函数内部会修改这个值】
"""

"""
案例一：
"""


def func(a1, a2=[1, 2]):
    a2.append(666)
    print(id(a2))
    print(a1, a2)


"""函数讲解
func函数在定义的时候即会生成a2=[1,2]的内存空间，此函数空间在整个程序运行阶段都存活
假设传入没有传入a2的值，即指向默认值，a2.append即加载默认的空间中
假设有传入值，则将a2指向传入值的空间
"""

func(100)  # 140315508122624 100 [1, 2, 666]
"""
func(100)没有传入a2值，则a2.append则添加默认生成的140315508122624空间a2=[1,2]中
a2使用的内存空间id是140315508122624
"""

func(200)  # 140315508122624 200 [1, 2, 666, 666]
"""
func(200)没有传入a2值，则a2.append则添加默认生成的140315508122624空间a2=[1,2,666]中
a2使用的内存空间id是140315508122624
"""

func(99, [77, 88])  # 140315508124864 99 [77, 88, 666]

"""
func(99,[77,88])传入了a2值，则原本的140315508122624空间被[77,88]的140315508124864空间覆盖，则a2.append则添加到a2=[77,88]中
a2使用的内存空间id是140315508124864
"""

func(300)  # 140315508122624 300 [1, 2, 666, 666, 666]
"""
func(300)没有传入a2值，则a2.append则添加默认生成的140315508122624空间a2=[1,2,666,666]中
a2使用的内存空间id是140315508122624
"""


"""
案例二：
"""


def func(a1, a2=[1, 2]):
    a2.append(a1)
    return a2


v1 = func(10)  # [1, 2, 10, 20, 40]
v2 = func(20)  # [1, 2, 10, 20, 40]
v3 = func(30, [11, 22])  # [11, 22, 30]
v4 = func(40)  # [1, 2, 10, 20, 40]

"""
函数讲解：
1.在函数func定义的时候会生成一块内存空间存放默认参数a2=[1,2]
2.v1 = func(10)执行，由于a2没有传入值，a2即使用默认空间a2=[1,2]，append结果默认空间a2=[1,2,10]，返回值为return a2即v1指向a2默认空间内存地址
3.v2 = func(20)执行，由于a2没有传入值，a2即使用默认空间a2=[1,2,10]，append结果默认空间a2=[1,2,10,20]，返回值为return a2即v2指向a2默认空间内存地址
4.v3 = func(30, [11, 22])指向，a2没有使用默认空间，创建了新空间a2=[11, 22]，append结果新空间a2=[11, 22, 30]，返回值return a2即v3指向a2新空间内存地址
5.v4 = func(40)执行，由于a2没有传入值，a2即使用默认空间a2=[1,2,10,20]，append结果默认空间a2=[1,2,10,20,40]，返回值为return a2即v4指向a2默认空间内存地址


6.此刻 v1.v2.v4都指向最初生成都默认空间，而默认空间都值是[1, 2, 10, 20, 40]，v3指向新空间，新空间对应都值是[11, 22, 30]
"""

"""
2. 动态参数的补充

在定义函数时可以用 `*和**`，其实在执行函数时，也可以用
-   形参固定，实参用`*和**`
-   形参用`*和**`，实参也用 `*和**`
"""

"2.1 形参固定，实参用`*和**"


def func(a1, a2):
    print(a1, a2)


func(11, 22)
func(a1=1, a2=2)

func(*[11, 22])  # 相当于打散，按顺序赋值，把11交给a1,22交给a2
func(**{"a1": 11, "a2": 22})  # 相当于打散，按关键字赋值，把11交给a1,22交给a2

"2. 形参用`*和**`，实参也用 `*和**"


def func(*args, **kwargs):
    print(args, kwargs)


# 注意，这里会把他们都当作顺序传参
## args = ([11,22,33],{"k1":1,"k2":2}) kwargs = {}
func([11, 22, 33], {"k1": 1, "k2": 2})

# 这里在实参中使用*和**
## args=(11,22,33),kwargs={"k1":1,"k2":2}
func(*[11, 22, 33], **{"k1": 1, "k2": 2})

# 值得注意：按照这个方式将数据传递给args和kwargs时，数据是会重新拷贝一份的（可理解为内部循环每个元素并设置到args和kwargs中）

"在format字符串格式化也支持这样的用法"
v1 = "我是{},年龄：{}".format("kinght", 18)
v2 = "我是{name},年龄：{age}".format(name="kinght", age=18)

v3 = "我是{},年龄：{}".format(*["kinght", 18])
v4 = "我是{name},年龄：{age}".format(**{"name": "kinght", "age": 18})

"""
案例：下载抖音视频

抖音视频下载，首先需要找到视频解析源，这里使用的

    https://www.dy114.com/douyin

获取解析源后，在目录下创建了一个file的文件夹，创建了一个`7_url.csv`的文件

    鱼香肉丝,http://v11-x.douyinvod.com/4fdc29fe92aabe5280e599568adaae8b/6219cdd2/video/tos/cn/tos-cn-ve-15-alinc2/852932a75a8443af97f51825476c723a/?a=1128&br=1633&bt=1633&cd=0%7C0%7C0%7C0&ch=0&cr=0&cs=0&cv=1&dr=0&ds=3&er=&ft=YbbdSWWFBNFqd.4YagD1233CCd3w&l=20220226134809010212170090122648AC&lr=&mime_type=video_mp4&net=0&pl=0&qs=0&rc=ajV4NTU6Zmo3OzMzNGkzM0ApOGRmODZnZTtmNzdlZWk4OWcpaGRqbGRoaGRmNWlpLXI0MGRgYC0tZC0vc3MzYDIyNTMwLTMvNjI0MGFeOmNwb2wrbStqdDo%3D&vl=&vr=
    游戏指挥官,http://v5-f.douyinvod.com/e14bc1c0ab2ccf947956b5a16893b4cf/6219cdfb/video/tos/cn/tos-cn-ve-15-alinc2/ccb04fdcc55546d29ac4fe6737eda997/?a=1128&br=905&bt=905&cd=0%7C0%7C0%7C0&ch=0&cr=0&cs=0&cv=1&dr=0&ds=3&er=&ft=YbbdSWWFBNFqd.4YagD12EqCCd3w&l=2022022613491001019405122531268848&lr=&mime_type=video_mp4&net=0&pl=0&qs=0&rc=M2QzM2U6ZjM3OzMzNGkzM0ApMzo6NTo2PGU2N2g0M2c0aWcpaGRqbGRoaGRmY2BoMXI0MGI1YC0tZC1hc3NhMl9hLV4wYmMuMmM1XjZjOmNwb2wrbStqdDo%3D&vl=&vr=
    打工人模拟器,http://v1-cold1.douyinvod.com/a3de8062cf93de87082c77dd24a20976/6219ce00/video/tos/cn/tos-cn-ve-15-alinc2/230204e5b7c043b297ec5bf0b7f9e8b4/?a=1128&br=1078&bt=1078&cd=0%7C0%7C0%7C0&ch=0&cr=0&cs=0&cv=1&dr=0&ds=3&er=&ft=ElUQrWWFBNFqd.4YagD12SGCCd3w&l=202202261350220102091561561025F834&lr=&mime_type=video_mp4&net=0&pl=0&qs=0&rc=M211ajQ6ZnFnOzMzNGkzM0ApOTs8ZDdoZGVlN2g8aWg1PGcpaGRqbGRoaGRmYi1lLXI0MDBfYC0tZC0vc3NeMy5jLTYwLTFhMi9eYC0uOmNwb2wrbStqdDo%3D&vl=&vr=

然后进行文件读取下载
"""

import requests, os


def get_file_path():
    abs_path = os.path.abspath(__file__)
    dir_path = os.path.dirname(abs_path)
    return dir_path


def download(title, url):
    res = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
        },
    )
    movie_file_path = os.path.join(get_file_path(), "file", "{}.mp4".format(title))
    with open(movie_file_path, mode="wb") as file:
        file.write(res.content)


def init():
    csv_file_path = os.path.join(get_file_path(), "file", "7_url.csv")
    print(csv_file_path)
    with open(csv_file_path, mode="rt", encoding="utf-8") as csv:
        for file in csv:
            file = file.strip().split(",")  # 把字符串进行分割成列表
            download(*file)  # 传入download进行下载


init()
