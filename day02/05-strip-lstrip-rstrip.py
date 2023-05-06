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
# 让用户循环反复的输入2个值[必须都是数字，不是数字就重复输入，直到都是数字为止],且让两个数字相加
