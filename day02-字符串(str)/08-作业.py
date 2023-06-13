# 判断下列逻辑语句的True,False.
1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6  # True
"""

在 Python 中，逻辑运算符的优先级按照从高到低依次为：
not (非)
and (与)
or (或)

"""
# 1 > 1 or 3 < 4 or (4 > 5 and 2 > 1 and 9 > 8) or 7 < 6
# False or True or (False and True and True) or False
# False or True or False or False
# True


# 有变量name = " aleX leNb " 完成如下操作
name = " aleX leNb "
# 移除 name 变量对应的值两边的空格,并输出处理结果
num_1 = name.strip()
# 判断 name 变量是否以 "al" 开头,并输出结果
num_2 = name.startswith("al")
# 判断name变量是否以"Nb"结尾,并输出结果
num_3 = name.endswith("Nb")
# 将 name 变量对应的值中的所有的"l" 替换为 "p",并输出结果
num_4 = name.replace("l", "p")
# 将name变量对应的值中的第一个"l"替换成"p",并输出结果
num_5 = name.replace("l", "p", 1)
# 将 name 变量对应的值根据所有的"l" 分割,并输出结果。
num_6 = name.split("l")
# 将name变量对应的值根据第一个"l"分割,并输出结果。
num_7 = name.split("l", 1)
# 将 name 变量对应的值变大写,并输出结果
num_8 = name.upper()
# 将 name 变量对应的值变小写,并输出结果
num_9 = name.lower()

# 判断name变量对应的值字母"l"出现几次，并输出结果
count_9 = 0
for i in name:
    if i == "l":
        count_9 += 1
# print(count_9, name.count("l"))
"""
等同于
name.count("l")
"""

# 如果判断name变量对应的值前四位"l"出现几次,并输出结果
count_10 = 0
for i in name[:4]:
    if i == "l":
        count_10 += 1
# print(count_10, name[:4].count("l"))
"""
等同于
name[:4].count("l")
"""
# 请输出 name 变量对应的值的第 2 个字符?
num_11 = name[1]
# 请输出 name 变量对应的值的前 3 个字符?
num_12 = name[:3]
# 请输出 name 变量对应的值的后 2 个字符?
num_13 = name[-3:]


# 如何实现字符串的反转？如： name = "wupeiqi" 请反转为 name ="iqiepuw"
name = "wupeiqi"
name_list = []
for i in range(len(name) - 1, -1, -1):
    name_list.append(name[i])

name = "".join(name_list)
# print(name)
"""
等同于 name = name[::-1]
"""


# 如何实现 '1,2,3' 变成 ['1,'2,'3]
str = "1,2,3"
num_list = str.split(",")

# 以下代码输出是什么? list="a,b,c,d,e,f" print(list[10:])
list = "a,b,c,d,e,f"
#     0 1 2 3 4 5 6 7 8 9 10 包括 逗号
list[10:]  # "f"

# 对3.2做四舍五入，并打印绝对值
x = 3.2
x = round(x)  # 四舍五入
x = abs(x)  # 绝对值

# "123"能否转成数字？"34r"呢？说明原因
int_num_1 = int("123")  # 123
"""
如果字符串中包含非数字字符，例如 "34r"，则会抛出 ValueError 异常。
"""
# int_num_2 = int("34r")
# 报错
# 如果字符串中包含非数字字符，例如 “34r”，则会抛出 ValueError 异常。

# 制作趣味模板程序需求：等待⽤户输⼊名字、地点、爱好，根据⽤户的名字和爱好进行任意显示
# 如：敬爱可亲的xxx，最喜欢在xxx地⽅⼲xxx
# 使用input获取内容，格式化输出打印
user_input = input("请输入姓名、地点、爱好：（用,隔开）")
user_list = user_input.split(",")
message = f"敬爱可亲的{user_list[0]}，最喜欢在{user_list[1]}地⽅⼲{user_list[2]}"
