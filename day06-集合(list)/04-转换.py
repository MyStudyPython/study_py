"""
转换为集合类型

其他类型如果想要转换为集合类型，
可以通过set进行转换，
并且如果数据有重复自动剔除。


提示：str/int/list/tuple/dict都可以转换为集合。
"""

"字符串 str"
v1 = "hong"
v2 = set(v1)  # {'o', 'g', 'h', 'n'}

"列表 int"
v1 = [11, 22, 33, 11, 3, 99, 22]
v2 = set(v1)  # {33, 3, 99, 11, 22}

"元组"
v1 = (11, 22, 3, 11)
v2 = set(v1)  # {11,22,3}


"""
案例 -> 数据去重
"""
data = {11, 22, 33, 3, 99}
v1 = list(data)  # [11,22,33,3,99]
v2 = tuple(data)  # (11,22,33,3,99)


# 数组 list
v1 = [11, 22, 33, 44]

# 元组 tuple
v2 = (11, 22, 33, 44)

# 元组 tuple
v3 = {11, 22, 33, 44}

"""
数组 list  元组 tuple 元组 tuple

三个之间可以直接进行相互转换，
原则：想转化弄成谁就让谁的英文名字包裹一下。
"""
v1 = [11, 22, 33, 44]
res = tuple(v1)  # (11,22,33,44)


"当元组或列表转换成集合时，会自动去重"
v1 = [11, 22, 33, 11, 33, 44]
res = set(v1)  # {11,22,33,44}
