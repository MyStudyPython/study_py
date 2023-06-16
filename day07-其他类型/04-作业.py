"""
[2, 30, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
  - 将列表中的字符串"1"变成数字101
  - 将列表中的"tt"变成大写
  - 将列表中的数字3变成字符串"100"
"""
str_list = [2, 30, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
'将列表中的字符串"1"变成数字101'
str_list[3][-2][-1][-1] = 101
# [2, 30, 'k', ['qwe', 20, ['k1', ['tt', 3, 101]], 89], 'ab', 'adv']

'将列表中的"tt"变成大写'
str_list[3][-2][-1][0] = str_list[3][-2][-1][0].upper()
# [2, 30, 'k', ['qwe', 20, ['k1', ['TT', 3, 101]], 89], 'ab', 'adv']

'将列表中的数字3变成字符串"100"'
str_list[3][-2][-1][1] = "100"
# [2, 30, 'k', ['qwe', 20, ['k1', ['TT', '100', 101]], 89], 'ab', 'adv']


"""
li = [1, 3, 2, "a", 4, "b", 5,"c"]
  - 通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
  - 通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]
  - 通过对li列表的切片形成新的列表l3,l3 = ["1,2,4,5]
  - 通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
  - 通过对li列表的切片形成新的列表l5,l5 = ["c"]
  - 通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]
"""
li = [1, 3, 2, "a", 4, "b", 5, "c"]
l1 = li[:3]
l2 = l1[3:6]
l3 = li[::2]
l4 = li[1:6:2]
l5 = li[-1]
l6 = li[-3::-2]

"""
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
  - 计算列表的长度并输出
  - 列表中追加元素"seven",并输出添加后的列表
  - 请在列表的第1个位置插入元素"Tony",并输出添加后的列表
  - 请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
  - 请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添
  加。
  - 请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
  - 请删除列表中的元素"ritian",并输出添加后的列表
  - 请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
  - 请删除列表中的第2至4个元素，并输出删除元素后的列表
"""
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
li_len = len(li)

li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
li.append("seven")

li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
li.insert(0, "Tony")

li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
li.insert(2, "Kelly")

li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
l2 = [1, "a", 3, 4, "heart"]
li.extend(l2)

li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
s = "qwert"
s_list = "".join(s)
li.extend(s_list)

li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
if "ritian" in li:
    li.remove("ritian")
else:
    pass

li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
del_li = li.pop(1)

li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# 将该切片设置为[]，表示将这个切片对应的元素从li中删除。
li[1:4] = []


"""
请将列表中的每个元素通过 "_" 链接起来。
['李少奇','李启航','渣渣辉']
"""
arr = ["李少奇", "李启航", "渣渣辉"]
str_list = "_".join(arr)  # 李少奇_李启航_渣渣辉

"""
请将
元组 v1 = (11,22,33) 中的所有元素追加到
列表 v2 = [44,55,66] 中。
"""
v1 = (11, 22, 33)
v2 = [44, 55, 66]

# 方式一
# for i in v1:
#     v2.append(i)

# 方式二
# v1_list = list(v1)
# v2.extend(v1_list)

# 方式三
"""
可以直接添加

在 Python 中，元组和列表都是序列，它们都支持切片和迭代，这使得它们具有相同的操作方法
这是 Python 中序列类型的通用性体现。
"""
v2.extend(v1)

"""
请将
元组 v1 = (11,22,33,44,55,66,77,88,99) 中的所有偶数索引位置的元素 
追加到列表 v2 = [44,55,66] 中。
"""
v1 = (11, 22, 33, 44, 55, 66, 77, 88, 99)
v2 = [44, 55, 66]
for i in range(len(v1)):
    if i % 2 == 0:
        v2.append(v1[i])

# [44, 55, 66, 11, 33, 55, 77, 99]

"""
将字典的键和值分别追加到 key_list 和 value_list 两个列表中，如：
  key_list = []
  value_list = []
  info = {'k1':'v1','k2':'v2','k3':'v3'}
"""
key_list = []
value_list = []
info = {"k1": "v1", "k2": "v2", "k3": "v3"}

key_list = list(info.keys())
value_list = list(info.values())

print(key_list, value_list)

"""
{'k1': "v1", "k2": "v2", "k3": [11,22,33]}
  - 输出所有的key
  - 输出所有的value
  - 输出所有的key和value
  - 字典中添加一个键值对，"k4": "v4"，输出添加后的字典
  - 修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
  - 在k3对应的值中追加一个元素 44，输出修改后的字典
  - 在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
"""
dict_example = {"k1": "v1", "k2": "v2", "k3": [11, 22, 33]}

# dict_keys = dict_example.keys()
for key in info.keys():
    print(key)

# dict_values = dict_example.values()
for value in info.values():
    print(value)

# dict_items = dict_example.items()
for key, value in info.items():
    print(key, value)

dict_example["k4"] = "v4"

dict_example["k1"] = "alex"

dict_example["k3"].append(44)

dict_example["k3"].insert(0, 18)


"""
hero = {
    "法师": {
        "小法": ["约德尔人", "自认为很邪恶"],
        "火男": ["AOE伤害", "消耗强"],
        "安妮": ["小熊", "幼女魔法师"],
        "光辉": ["强控", "远程大招"],
    },
    "战士": {"赵信": ["一点寒芒先到，随后枪出如龙", "the Seneschal of Demacia"]},
    "射手": {"金克斯": ["哒哒哒哒哒", "究极死神飞弹"]},
}

  - 给此 ["约德尔人","自认为很邪恶"] 列表第二个位置插入一个 元素：'如果我俩角色互换，我会
  让你看看什么叫作残忍'。
  - 将此["强控","远程大招"]列表的 "远程大招" 删除。
  - 将此["一点寒芒先到，随后枪出如龙", "the Seneschal of Demacia"]列表的 "the Seneschal
  - of Demacia"全部变成大写。
  - 给 '射手' 对应的字典添加一个键值对 '女枪' :['哈哈哈哈哈']
  - 删除这个键值对："安妮": ["小熊","幼女魔法师"]
  - 给此["哒哒哒哒哒","究极死神飞弹"]列表的第一个元素，加上一句话：'疯子'
"""

hero = {
    "法师": {
        "小法": ["约德尔人", "自认为很邪恶"],
        "火男": ["AOE伤害", "消耗强"],
        "安妮": ["小熊", "幼女魔法师"],
        "光辉": ["强控", "远程大招"],
    },
    "战士": {"赵信": ["一点寒芒先到，随后枪出如龙", "the Seneschal of Demacia"]},
    "射手": {"金克斯": ["哒哒哒哒哒", "究极死神飞弹"]},
}

hero["法师"]["小法"].insert(1, "如果我俩角色互换，我会让你看看什么叫作残忍")

hero["法师"]["光辉"].remove("远程大招")

hero["战士"]["赵信"][-1] = hero["战士"]["赵信"][-1].upper()

hero["射手"]["女枪"] = ["哈哈哈哈哈"]

del hero["法师"]["安妮"]

hero["射手"]["金克斯"][0] += "，疯子"


"""
有字符串"k:1|k1:2|k2:3|k3:4" 处理成字典 {'k':1,'k1':2....}
"""
# info_str = "k:1|k1:2|k2:3|k3:4"
# info_list = info_str.split("|")
# info_set = {}
# for item in info_list:
#     info_item = item.split(":")
#     info_item_key = info_item[0]
#     info_item_value = int(info_item[1])
#     info_set[info_item_key] = info_item_value

# print(info_set)

s = "k: 1|k1:2|k2:3 |k3 :4"
d = {k.strip(): int(v) for k, v in [i.split(":") for i in s.split("|")]}

"""
info = {'name':'王刚蛋','hobby':'铁锤','age':'18'}

请用代码验证 "name" 是否在字典的键中
请用代码验证 "alex" 是否在字典的值中
"""
info = {"name": "王刚蛋", "hobby": "铁锤", "age": "18"}
# 判断键值是否存在
# info_in_name = info.get("name") # 王刚蛋
# info_in_alex = info.get("alex") # None

info_in_name = "name" in info.keys()  # True
info_in_alex = "alex" in info.values()  # False

"""
有如下：v1 = {'孙悟空','李杰','太白','景女神'}， v2 = {'李杰','景女神'}
  - 请得到 v1 和 v2 的交集并输出
  - 请得到 v1 和 v2 的并集并输出
  - 请得到 v1 和 v2 的 差集并输出
  - 请得到 v2 和 v1 的 差集并输出
"""
v1 = {"孙悟空", "李杰", "太白", "景女神"}
v2 = {"李杰", "景女神"}
# v3 = v1 & v2  # {'李杰', '景女神'}
# v4 = v1 | v2  # {'太白', '李杰', '孙悟空', '景女神'}
# v5 = v1 - v2  # {'太白', '孙悟空'}
# v6 = v2 - v1  # set()


v3 = v1.intersection(v2)  # {'李杰', '景女神'}
v4 = v1.union(v2)  # {'太白', '李杰', '孙悟空', '景女神'}
v5 = v1.difference(v2)  # {'太白', '孙悟空'}
v6 = v2.difference(v1)  # set()

"""
判断以下值那个能做字典的key ？那个能做集合的元素？
  1
  -1
  ""
  None
  [1,2]
  (1,)
  {11,22,33,4}
  {'name':'wupeiq','age':18}
"""
a = 1
b = -1
c = ""
d = None
e = [1, 2]  # 不行，报错
f = (1,)
g = {11, 22, 33, 4}  # 不行，报错
h = {"name": "wupeiq", "age": 18}  # 不行，报错


"""
按照需求为列表[1, 3, 6, 7, 9, 8, 5, 4, 2]排序
  - 从大到小排序
  - 反转l1列表
"""
info = [1, 3, 6, 7, 9, 8, 5, 4, 2]
info.sort(reverse=True)

info = [1, 3, 6, 7, 9, 8, 5, 4, 2]
info.reverse()

"""
l1 = [11, 22, 33, 44, 55]，
请把索引为奇数对应的元素删除，不能一个一个删除
"""
l1 = [11, 22, 33, 44, 55]
res = l1[1::2]  # [22, 44]

li_num = len(l1) - 1
l1[1:li_num:2] = []
"""
报错
ValueError: attempt to assign sequence of size 0 to extended slice of size 3
下面一样的道理
"""


# l1 = [11, 22, 33, 44, 55]
# l1[0::2] = []
"""
报错
ValueError: attempt to assign sequence of size 0 to extended slice of size 3

如果列表 l1 中所有下标为奇数的元素数目为偶数，
那么左侧和右侧的元素个数就不匹配了。

假设列表 l1 = [1, 2, 3, 4]，执行 l1[0::2] = [] 这个赋值语句之后，
左侧应该会被替换成一个空列表，
即 l1 = [1, 3]，但是由于左侧的元素数量为 2，右侧的元素数量为 0，
因此这个赋值语句就无法完成。
"""

# 这样写是正确的
l1 = [11, 22, 33, 44, 55]
del l1[0::2]
