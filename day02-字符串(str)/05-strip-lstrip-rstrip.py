"""
去除空白
"""
name = " hhh "
v1 = name.strip()  # "hhh"
v2 = name.lstrip()  # "hhh "
v3 = name.rstrip()  # " hhh"

data = input("请输入:")
if data == "":
    print("输入不能为空")
else:
    print(data)

if 123:
    pass
else:
    pass


"""
示例
"""
# 示例一
# 输入的姓名不能为空
name = input("请输入姓名：")  # " "
data = name.strip()  # data = " " ===> False
if data:
    # 用户输入的姓名不为空
    print("用户输入的姓名不为空")
else:
    # 用户输入为空
    print("用户输入为空")


name = input("请输入姓名：")  # " "
data = name.strip()  # data = " " ===> False
if not data:
    # 用户输入为空
    print("用户输入为空")
else:
    # 用户输入的姓名不为空
    print("用户输入的姓名不为空")
