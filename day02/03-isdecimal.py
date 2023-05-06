"""
判断字符串中是否不是整数
"""

data1 = "12"
v1 = data1.isdecimal()  # True

data2 = "a2"
v2 = data2.isdecimal()  # False

"""
作用域
"""
if 1 == 1:
    text = "xxx"
    print(text)  # xxx
print(text)  # xxx

if 1 > 2:
    text = "xxx"
    print(text)  # xxx
print(text)  # 报错

"""
示例
"""
# 示例一
# 让用户循环反复的输入2个值[必须都是数字，不是数字就重复输入，直到都是数字为止],且让两个数字相加
while True:
    num_1 = input("请输入第一个数字：")
    if num_1.isdecimal():
        break

while True:
    num_2 = input("请输入第二个数字：")
    if num_2.isdecimal():
        break

print(int(num_1) + int(num_2))
