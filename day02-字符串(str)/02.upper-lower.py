"""
定义

字符串是一个不可变的类型
"""

# 大写
name1 = "root"
res1 = name1.upper()
print(res1)

# 小写
name2 = "ROOT"
res2 = name2.lower()
print(res2)


"""
示例
"""
# 示例一
# 注册某个网站等某个网络的时候，填写验证码（不区分大小写）
code = input("请输入某个验证码(FbeY) ： ")
big_code = code.upper()

if big_code == "FBEY":
    print("验证码正确")
else:
    print("验证码错误")


# 实例二
# 让用户循环输入姓名，用字符串格式化给他输出“恭喜xxx，获得500w”，如用户输入“q/Q”，循环终止
while True:
    name = input("请输入你的姓名（q/Q）：")
    if name.upper() == "Q":
        break
    message = ("恭喜{}，获得500w").format(name)
    print(message)
