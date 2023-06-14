"""
字典是 无序、键不重复 且 元素只能是 键值对 的可变的 容器。

data = {key:value,key:value}

我们可以单纯理解，他的key是集合类型，而value是任意类型。
  元素必须键值对
  键不重复，重复则会被覆盖
  键必须是哈希类型
  容器

  无序（在Python3.6+字典就是有序了，之前的字典都是无序。）
  但是，这里就算是有序了，也不能通过索引取值
"""
"键不重复，重复则会被覆盖"
info = {"k1": 123, "k1": 999}
info  # {"k1":999}

"""
键必须是哈希类型
可哈希类型:int、bool、str、tuple
不可哈希:列表、字典、集合
"""
v1 = 123
v2 = "123"
v3 = (11, 22, 33)

v4 = [11, 22, 33]  # 不可哈希
v5 = {"k1": 123}  # 不可哈希
v6 = {123}  # 不可哈希

# res = hash(v5) #报错
res = hash(v3)  # 不报错

# 合法的定义
data_dict = {"武沛齐": 29, True: 5, 123: 5, (11, 22, 33): ["alex", "eric"]}
# 不合法的定义
# v1 = {[1, 2, 3]: "周杰伦", "age": 18}
# v2 = {{1, 2, 3}: "哈哈哈", "name": "alex"}
# v3 = {{"k1": 123, "k2": 456}: "呵呵呵", "age": 999}

"""
字典与元祖的存储原理相似，但是只对key做哈希处理
"""

"""
两种定义模式
v1 = {}
v2 = dict()
"""
info = {"age": 12, "status": True, "name": "wupeiqi", "hobby": ["篮球", "足球"]}

"注意：同样True会被当作1，所以会被覆盖掉"
data_dict = {1: 29, True: 5}  # 同样True会被当作1，所以会被覆盖掉
data_dict  # {1: 5}

"""
运用字典的地方
当我们想要表示一组固定信息时，用字典可以更加的直观，例如：
"""
uer_list = [
    ["root", "123", 18, "xxx@example.com"],
    ["admin", "456", 20, "yyy@example.com"],
]
uer_list = [
    ("root", "123", 18, "xxx@example.com"),
    ("admin", "456", 20, "yyy@example.com"),
]

uer_list = [
    {"name": "root", "pwd": "123", "age": 18, "email": "xxx@example.com"},
    {"name": "admin", "pwd": "456", "age": 20, "email": "yyy@example.com"},
]
