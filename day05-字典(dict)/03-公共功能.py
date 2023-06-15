"""
公共功能

求`并集`（Python3.9新加入）
长度 len
是否包含 in 
索引（键 key）取值
根据键 修改值 和 添加值 和 删除键值对
"""

"""
求`并集`（Python3.9新加入）
"""
v1 = {"k1": 1, "k2": 2}
v2 = {"k2": 22, "k3": 33}

v3 = v1 | v2  # {'k1': 1, 'k2': 22, 'k3': 33}

"""
长度 len
"""
info = {"age": 12, "status": True, "name": "孙悟空"}
data = len(info)  # 3

"""
是否包含 in 

判断是否在key里面
判断是否在value里面
判断键值对是否在字典里面
"""
"判断是否在key里面"
info = {"age": 12, "status": True, "name": "孙悟空"}
# 判断是否在key里面
v1 = "age" in info  # Truerue
v2 = "age" in info.keys()  # True
# 判断是否在value里面
v3 = "孙五天" in info.values()  # False
# 判断键值对是否在字典里面
v4 = ("status", True) in info.items()  # True


"""
索引（键 key）取值（与列表、元组、字符串索引操作不一样）

就算是有序了，也不支持0,1,2进行取值

字典不同于元组、列表和字符串，
字典的索引是`键 key`，
而列表和元组则是 `0、1、2等数值`。

列表、元组、字符串      --->  0/1/2/3/4...
字典                   --->  键 key
"""
info = {"name": "黄天霸", "age": 15, "status": True, "hobby": ["乒乓球", "足球"], "data": None}

v1 = info["name"]  # '黄天霸'
# v2 = info["email"] # 报错，不存在会报错

# 通过get取值时，键不存在会报错（以后项目开发时建议使用get方法根据键去获取值）
v3 = info.get("name")  # "黄天霸"
v4 = info.get("email")  # None

"""
根据键 修改值 和 添加值 和 删除键值对
"""
"""
增、改

增、改为一体
原值没有则新增，存在则修改
"""
# 增
info = {"name": "黄天霸", "age": 15, "status": True, "hobby": ["乒乓球", "足球"], "data": None}
info["sex"] = "男"
# {'name': '黄天霸', 'age': 15, 'status': True, 'hobby': ['乒乓球', '足球'], 'data': None, 'sex': '男'}
print(info)
# 改
info["age"] = 100
# {'name': '黄天霸', 'age': 100, 'status': True, 'hobby': ['乒乓球', '足球'], 'data': None, 'sex': '男'}

"删除"
info = {"name": "黄天霸", "age": 15, "status": True, "hobby": ["乒乓球", "足球"], "data": None}
# 删除info字典中键为age的那个键值对（键不存在则报错）
del info["age"]
# del info["email"]  # 报错，不存在会报错

# 删除info字典中键为status的那个键值对（键不存在则报错）
data = info.pop("status")  # 但是pop可以取值
print(info)  # 输出： {"name":"武沛齐"}
print(data)  # True
# data = info.pop("email")  # 报错，不存在会报错

# 判断键是否存在，存在了再删除
if "email" in info:
    del info["email"]

"""
for 循环
"""
info = {"name": "黄天霸", "age": 15, "status": True, "hobby": ["乒乓球", "足球"], "data": None}

# 循环取键
# 方案1 -> 默认取出就是键
for key in info:
    print(key)  # 默认是所有键
# 方案2
for key in info.key():
    print(key)

# 循环取值
for value in info.values():
    print(value)

# 循环取键值对
for k, v in info.items():
    print(k, v)
