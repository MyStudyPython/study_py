"""
其他类型转换成列表
`list(其他类型)`

首先 int、bool无法转换成列表
"""

"""
str 转列表
"""
name = "马化腾"
data = list(name)  # ['马', '化', '腾']

"""
元祖转列表
"""
v1 = (11, 22, 33, 44)  # 元组
vv1 = list(v1)  # 列表 [11,22,33,44]

"""
集合转列表
"""
v2 = {"alex", "eric", "dsb"}  # 集合
vv2 = list(v2)  # 列表 ["alex","eric","dsb"]
