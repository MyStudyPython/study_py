"""
运算符(js 中没见过的)
成员运算
逻辑运算（高级用法）
"""


"""
成员运算，xx中是否含有xx
"""
# 基本用法
v1 = "中国" in "中国人"  # True
v2 = "葡萄牙" in "中国人"  # False

# 可以替换相同变量
text = "中国人是好人"
v3 = "中国" in text  # True

# 试一试交互
text = input("请输入你的评论：")
if "中国" in text:
    print("不能包含中国的信息")
else:
    print(text)

text = input("请输入你的评论：")
if "中国" in text:
    print(text)
else:
    print("只能包含中国的信息")


"""
逻辑运算（高级用法）----很少写
"""
# v1 = 值 and/or 值
v1 = 2 and 4  # 4

"""
值 and 值

逻辑运算符的结果取决于那个值的位置？结果等于值
如果第一个值 为转成 True/False 为True 那值一定为第二个 否则为第一个
v1 = 2 and 4

值 or 值
规律类似 只是and和or 与和或的区别
"""

# 案例
v1 = 6 and 9  # 9
v2 = 0 and 1  # 0
v3 = 88 and 0  # 0
v4 = "" and 9  # ""
v5 = "深圳" and "成都"  # "成都"
v6 = 1 or 2  # 1
v7 = 0 or 2  # 2

# 先分析and,在分析or
v8 = 1 and 8 or 9 and 10 or 11 or 12 and 0 or "" and "xxx"  # 8


name = 23
v1 = name or 666  # 23
