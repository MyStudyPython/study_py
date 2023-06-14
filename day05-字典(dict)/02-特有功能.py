"""
特有功能

获取值 get
获取所有的键 dict.keys()
获取所有的值 dict.values()
获取所有的键值对 dict.items()
设置值 dict.setdefault(key,value)
更新字典键值对 dict.update(key,value)
移除指定键值对 dict.pop(key,value)
按照顺序移除（后进先出） dict.popitem()
"""
info = {"name": "黄天霸", "age": 15, "status": True, "hobby": ["乒乓球", "足球"], "data": None}

"""
获取值 get
"""
# 去字典中根据键，获取对应的值
v1 = info.get("name")  # "黄天霸"

v2 = info.get("email")  # None

"当键不存在时，直接覆盖"
v3 = info.get("email", "example@example.com")  # v3 = example@example.com
"当值不存在时，不理直接取键对应的值"
v4 = info.get("age", 999)  # 15


"""
if data == None:
    print("此键不存在")
else:
    print(data)
if data: # 不存在则返回None，None == False
    print(data)
else:
    print("键不存在")
"""
# 改进
# 判断info字典的键中是否存在email
if "email" in info:  # 判断email是否存在于字典key中
    data = info.get("email")
    print(data)
else:
    print("不存在")

"存在问题：如果字典中有'email':None的元素，则此判断不准确"
# 改进
# 直接一步到位如果key="hobby"存在返回值value，不存在返回123
data = info.get("hobby", 123)
print(data)  # 输出：['乒乓球', '足球']

"""
案例：字典存储用户信息

如果键不存在 db_password = None
如果键存在 db_password = '密码'
          db_password 和 用户输入的pwd 进行判断登录
"""
user_dict = {"huangtianyou": "666", "liyutuan": "888", "tianyi": "999"}


# while True:
#     user = input("请输入用户名：")  # "root"
#     db_password = user_dict.get(user)
#     if db_password == None:
#     if not db_password:
#         print("该用户不存在，请重新输入")
#     else:
#         while True:
#             pwd = input("请输入密码：")
#             if db_password == pwd:
#                 print("登录成功")
#                 break
#             else:
#                 print("登录失败,请重新输入密码")
#         break

while True:
    username = input("请输入用户名: ")
    db_password = user_dict.get(username)
    if username in user_dict:
        while True:
            password = input("请输入密码: ")
            if db_password == password:
                print("登录成功")
                break
            else:
                print("密码错误，请重新输入")
        break
    else:
        print("该用户不存在，请重新输入")


"""
获取所有的键

注意：在Python2中
字典.keys()直接获取到的是列表，而Python3中返回的是`高仿列表`，这个高仿的列表可以被循环显示。

ps：高仿的列表作用是缓存，他可以节省内存，具体方式在生成器篇章讲到
"""
info = {"name": "黄天霸", "age": 15, "status": True, "hobby": ["乒乓球", "足球"], "data": None}
# 高仿列表
v1 = info.keys()  # dict_keys(['name', 'age', 'status', 'hobby'])

# 循环高仿列表
for key in info.keys():
    print(key)

# name
# age
# status
# hobby
# data

# 转换成python列表
res = list(v1)  # ['name', 'age', 'status', 'hobby']


"""
获取所有的值

注意：与获取所有的键相同，在Python2中
字典.values()直接获取到的是列表，而Python3中返回的是高仿列表，这个高仿的列表可以被循环显示。
"""
info = {"name": "黄天霸", "age": 15, "status": True, "hobby": ["乒乓球", "足球"], "data": None}
v2 = info.values()  # dict_values(['黄天霸', 15, True, ['乒乓球', '足球'], None])


"""
获取所有的键值对
"""
info = {"name": "黄天霸", "age": 15, "status": True, "hobby": ["乒乓球", "足球"], "data": None}
v3 = info.items()
# dict_items([('name', '黄天霸'), ('age', 15), ('status', True), ('hobby', ['乒乓球', '足球']), ('data', None)])

# 可以使用for循环，获取直接拆分
# 方案1
for ele in info.items():
    print(ele[0], ele[1])  # ele是一个元组 (键，值)

# 方案2 -> 推荐
for key, value in info.items():
    print(key, value)  # key代表键，value代表值，将兼职从元组中直接拆分出来了。

"""
设置值 setdefault
"""
info = {"name": "黄天霸", "email": "xxx@live.com"}
info.setdefault("age", 55)  # {'name': '黄天霸', 'email': 'xxx@live.com', 'age': 55}
print(info)
# key不存在，则添加，key存在则不改变value
info.setdefault("name", "alex")  # {'name': '黄天霸', 'email': 'xxx@live.com', 'age': 55}


"""
更新字典键值对 update
"""
info = {"age": 12, "status": True}
info.update({"age": 14, "name": "黄天霸"})
# info中没有的键直接添加；有的键则更新值
print(info)  # 输出：{"age":14, "status":True,"name":"黄天霸"}

"""
移除指定键值对 pop
"""

info = {"age": 12, "status": True, "name": "武沛齐"}
data = info.pop("age")
# 移除掉的同时会将值传递给data
info  # {"status":True,"name":"武沛齐"}
data  # 12

"""
按照顺序移除（后进先出） popitem
-   py3.6后，popitem移除最后的值。
-   py3.6之前，popitem随机删除。
"""

info = {"age": 12, "status": True, "name": "武沛齐"}
data = info.popitem()  # 移除掉最后的值，将被移除的值组成元组
# ("name","武沛齐" ) -> data

info  # {"age":12, "status":True}
data  # ("name","武沛齐")
