"""
函数名就是变量名

1. 函数做元素
2. 函数名赋值
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
