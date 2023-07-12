"""
函数名就是变量名

1. 
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

choice_dist = {"1": register(), "2": login(), "3": show_users()}
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
