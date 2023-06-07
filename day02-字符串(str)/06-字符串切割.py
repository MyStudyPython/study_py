# 1. 字符串拼接
v1 = "我"
v2 = "好人"
text = v1 + "是" + v2  # 我是好人


# 2. 字符串格式化
v1 = "我"
v2 = "好人"
text = "{}不是{}".format(v1, v2)  # 我不是好人

# 3.列表，里面有很多字符串，你想要让他们按照某个连接符拼接起来
data_list = ["你好", "你不好", "6666", "9999"]
res = "_".join(data_list)  # 你好_你不好_6666_9999

data_list = ["你好", "你不好", "6666", "9999"]
res = ",".join(data_list)  # 你好,你不好,6666,9999

data_list = ["你好", "你不好", "6666", "9999"]
res = "".join(data_list)  # 你好你不好66669999
"""
注意事项：想要通过json去拼接，列表中必须都是字符串
"""


"""
....
....
....
"""
# 9.长度的补足
name = "xxx"
text = name.center(13, "*")  # *****xxx*****

name = "xxx"
text = name.ljust(13, "*")  # xxx**********

name = "xxx"
text = name.rjust(13, "*")  # **********xxx


# 10.长度的补足,只能在左边补0(二进制字符串前面补0)
name = "lll"
text = name.zfill(10)  # 0000000lll

name = "lll"
text = name.zfill(8)  # 00000lll

# 示例一
# 提示用户输入两个数字相加，例如：5+2,6+9格式（不用考虑 yy+77）
text = input(">>>")
data_list = text.split("+")  # ["5","9"]
res = int(data_list[0]) + int(data_list[1])
print(res)

# 示例二
# 提示用户输入两个数字相加，例如：5+2,6+9格式（不用考虑 yy+77）
text = input(">>>")
data_list = text.split("+")  # ["5","9"]
if data_list[0].isdecimal() and data_list[1].isdecimal():
    res = int(data_list[0]) + int(data_list[1])
    print(res)
else:
    print("输入错误")

# 示例三
# 排队买票
# ["a","b","c"]
name_list = []
name_list.append("a")
name_list.append("b")
name_list.append("c")

# name_list = ["a","b","c"]

# 1. 循环让用户输入姓名（q/Q终止），每输入一个姓名都追加到列表中
# 2. 输入q退出之后，将所有的人员姓名通过逗号连接成字符串并输出
user_list = []
while True:
    name = input("请输入姓名：")
    if name.upper() == "Q":
        break
    user_list.append(name)

res = ",".join(user_list)
print(res)
