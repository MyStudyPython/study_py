"""
函数名就是变量名

1. 函数做元素
2. 函数名赋值
3. 函数名做参数和返回值
"""


def func():
    print(123)
    print(123)
    print(123)


v1 = func  # <function func at 0x000001A16DCA0680> 这是个函数对象类型
v2 = func()  # None
# print(type(v1)) # <class 'function'>
v3 = v1()  # None
"""
本质上：func就是一个变量，代指这个函数而已，func() => 执行函数

注意：函数同时也可被哈希，所以函数名也可以当做集合的元素、字典的键。
"""


"1. 函数做元素"


def func():
    return 123


v1 = 999

data_list = [11, 22, v1, func, func, func, True, "XXX", (11, 223), {}, func(), func()]

data_list[4]  # <function func at 0x000001E90EE816C0>

"""
案例一：用户系统系统
请基于函数实现用户登录、注册、查看所有的用户信息
"""


def register():
    pass


def login():
    pass


def show_users():
    pass


print("欢迎xxx系统")
print("1.注册；2.登录；3.查看所有用户")

choice = input("请选择序号：")
# choice = int(choice)

# if choice == 1:
#     register()
# elif choice == 2:
#     login()
# elif choice == 3:
#     show_users()
# else:
#     print("选择错误")

choice_dist = {"1": register, "2": login, "3": show_users}
choice_item = choice_dist.get(choice)
if not choice_item:
    print("选择错误")
else:
    choice_item()

"""
案例二：利用字典dict 达到某种指标，发送到四个地方报警（短信、邮件、钉钉、微信）
"""


def send_sms():
    print("发送短信报警")


def send_email():
    print("发送邮件报警")


def send_dingding():
    print("发送钉钉报警")


def send_wechat():
    print("发送微信报警")


func_dist = {send_sms, send_email, send_dingding, send_wechat}

for item in func_dist:
    item()

"""
案例三：
资源下载管理器，系统有三大专区：图片专区、NBA专区、短视频专区
- 每个专区定义一个函数
- 用户去选择
  - 选择对了进入专区
  - 选择错了重复选择（错误提示）
  - 用户选择是输入Q/q，终止程序。
- 图片专区（NBA和短视频专区功能相同）
  - 罗列出来所有的序号和图片。
  - 让用户选择序号，用户选择哪个序号，则内部帮用户把这个图片下载下来。
  - 再次提示用户输入是否继续（n/N），返回上一级（让用户重新选择专区）
"""


def image_area():
    print("===================进入专区选择=======================")
    image_dict = {
        "1": (
            "吉他男神",
            "https://hbimg.huabanimg.com/51d46dc32abe7ac7f83b94c67bb88cacc46869954f478-aP4Q3V",
        ),
        "2": (
            "漫画美女",
            "https://hbimg.huabanimg.com/703fdb063bdc37b11033ef794f9b3a7adfa01fd21a6d1-wTFbnO",
        ),
        "3": (
            "游戏地图",
            "https://hbimg.huabanimg.com/b438d8c61ed2abf50ca94e00f257ca7a223e3b364b471-xrzoQd",
        ),
        "4": (
            "alex媳妇",
            "https://hbimg.huabanimg.com/4edba1ed6a71797f52355aa1de5af961b85bf824cb71-px1nZz",
        ),
    }
    for k, v in image_dict.items():
        print(k, v[0], v[1])

    while True:
        choice = input(">>>>>>>>>>>>请选择下载序号(n/N):")
        if choice.upper() == "N":
            return
        choice_item = image_dict.get(choice)
        if not choice_item:
            print("\n选择错误，请重新选择")
            continue
        # 下载需要title和url
        title, url = choice_item
        print(title, url)


def nba_area():
    print("===================进入专区选择=======================")
    nba_dict = {
        "1": {
            "title": "威少奇才首秀三双",
            "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300fc20000bvi413nedtlt5abaa8tg&ratio=720p&line=0",
        },
        "2": {
            "title": "塔图姆三分准绝杀",
            "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0d00fb60000bvi0ba63vni5gqts0uag&ratio=720p&line=0",
        },
    }
    for k, v in nba_dict.items():
        print(k, v["title"], v["url"])

    while True:
        choice = input(">>>>>>>>>>>>请选择下载序号(n/N):")
        if choice.upper() == "N":
            return
        choice_item = nba_dict.get(choice)
        if not choice_item:
            print("\n选择错误，请重新选择")
            continue
        # 下载需要title和url
        title, url = choice_item["title"], choice_item["url"]
        print(title, url)


def video_area():
    print("===================进入专区选择=======================")
    video_dict = {
        "1": {
            "title": "东北F4模仿秀",
            "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f570000bvbmace0gvch7lo53oog",
        },
        "2": {
            "title": "卡特扣篮",
            "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f3e0000bv52fpn5t6p007e34q1g",
        },
        "3": {
            "title": "罗斯mvp",
            "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg",
        },
    }
    for k, v in video_dict.items():
        print(k, v["title"], v["url"])

    while True:
        choice = input(">>>>>>>>>>>>请选择下载序号(n/N):")
        if choice.upper() == "N":
            return
        choice_item = video_dict.get(choice)
        if not choice_item:
            print("\n选择错误，请重新选择")
            continue
        # 下载需要title和url
        title, url = choice_item["title"], choice_item["url"]
        print(title, url)


fun_dist = {"1": image_area, "2": nba_area, "3": video_area}


def main():
    while True:
        print("1.图片专区;2.NBA专区;3.短视频专区")
        choice = input(">>>>>>>>>>>请选择专区(q/Q):")

        # 用户选择是输入Q/q，终止程序。
        if choice.upper() == "Q":
            break

        choice_item = fun_dist.get(choice)
        # 选择错了重复选择（错误提示）
        if not choice_item:
            print("\n选择错误，请重新选择")
            continue

        # 选择对了进入专区
        choice_item()


main()


"2. 函数名赋值"


def func(a1, a2):
    print(a1, a2)


abc = func

# 此时，abc和func都代指上面的那个函数，所以都可以被执行。
func(1, 1)
abc(2, 2)


# 其实上诉案例已经使用过函数名赋值啦
def func():
    return 123


list = [func, "1"]
list[0]()  # 列表第一个元素 == func ，加括号就可以直接执行

"对函数名重新赋值，如果将函数名修改为其他值，函数名便不再代指函数"


def func(a1, a2):
    print(a1, a2)


# 执行func函数
func(11, 22)

# func重新赋值成一个字符串
func = "kinght"
print(func)  # kinght


# func 又重新指向另一个函数
def func():
    print(666)


func()  # 666

"""
注意：
由于函数名被重新定义之后，就会变量新被定义的值，
所以大家在自定义函数时，不要与python内置的函数同名，否则会覆盖内置函数的功能
"""

# len内置函数用于计算值得长度
v1 = len("kinght")
print(v1)  # 6


# len重新定义成另外一个函数
def len(a1, a2):
    return a1 + a2


# 以后执行len函数，只能按照重新定义的来使用
v3 = len(1, 2)
print(v3)

"3. 函数名做参数和返回值"


def plus(num):
    return num + 100


def handler(func):
    res = func(10)
    print(res)


handler(plus)
"""
函数名作参数
调用handler函数，参数为plus，未加括号不执行，传入后在res = func(10) -=> plus(10)
"""


def plus(num):
    return num + 100


def handler():
    print("执行handler函数")
    return plus


result = handler()
data = result(20)  # 120
print(result)  # <function plus at 0x0000029D7BCA20C0>

"""
函数名作返回值
运行handler()函数，函数内将plus函数返回到了result变量，后执行result变量
"""
