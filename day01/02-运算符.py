"""
运算符(js 中没见过的)
成员运算
逻辑运算（高级用法）
"""


"""
成员运算，xx中是否含有xx
"""
# 基本用法
v1 = "中国" in "中国人"   # True
print(v1)
v2 = "葡萄牙" in "中国人"  # False
print(v2)

# 可以替换相同变量
text = "中国人是好人"
v3 = "中国" in text     # True
print(v3)

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
