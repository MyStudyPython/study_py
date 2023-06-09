"""
公共功能
相加  +  ---- 字符串拼接一样
相乘  *  ---- 列表复制
包含  in
获取长度 len
索引
切片
for循环
"""

"""
相加 ---- 字符串拼接一样
两个列表相加获取生成一个新的列表
"""

data = ["1", "2"] + ["3", "4"]  # ['1', '2', '3', '4']

# 等同于
v1 = [1, 2]
v2 = [3, 4]
v3 = v1 + v2  # [1, 2, 3, 4]

"""
相乘  --- 列表复制
列表*整型 将列表中的元素再创建N份并生成一个新的列表
"""
data = ["1", "2"] * 2  # ['1', '2', '1', '2']

v1 = [1, 2]
v2 = 2
v3 = v1 * v2  # [1, 2, 1, 2]

# 列表乘列表会报错
# v4 = [1, 2] * ["1", "2"]

"""
in 包含
"""
num_list = [1, 2, 3, 4]
result1 = 1 in num_list  # True
result2 = "1" in num_list  # False

# 案例一 pop -> .index找不到会报错
device_list = ["phone", "computer", "ipad"]
find_device = "computer"
if find_device in device_list:
    index = device_list.index(find_device)
    device_list.pop(index)

# 案例二：敏感词替换 -> 检查是否有敏感词
text = input("请输入文本内容：")  # 实打实大大大功夫格斗给干饭干饭
forbidden_list = ["实打", "大", "干饭"]
for item in forbidden_list:
    text = text.replace(item, "**")
# print(text) # **实******功夫格斗给****
"""
注意：**列表检查元素是否存在时，是采用逐一比较的方式，效率会比较低。**
"""

"""
获取长度 len
"""
data_list = [11, 22, 33, 44]
num = len(data_list)  # 4

"""
索引 --- 下标
"""
# 读
user_list = ["范德彪", "刘华强", "尼古拉斯赵四"]
user_list[0]  # 范德彪
user_list[2]  # 刘华强
# user_list[3]  # 报错

# 改
user_list = ["范德彪", "刘华强", "尼古拉斯赵四"]
user_list[0] = "孙悟空"
# print(user_list) # ["孙悟空","刘华强",'尼古拉斯赵四']

# 删
user_list = ["范德彪", "刘华强", "尼古拉斯赵四"]

# 第一种删除方式
# del user_list[1]  # ["范德彪", "尼古拉斯赵四"]

# 第二种删除方式
# user_list.remove("刘华强")  # ["范德彪", "尼古拉斯赵四"]

# 第三种删除方式
user_list.pop(1)  # ["范德彪", "尼古拉斯赵四"]

"""
注意：超出索引范围会报错。
提示：由于字符串是不可变类型，所以他只有索引读的功能，
      而列表可以进行读、改、删
"""

"""
切片，多个元素的操作
"""
# 读取一部分
user_list = ["范德彪", "刘华强", "尼古拉斯赵四"]
user_list[0:2]  # ["范德彪","刘华强"]
user_list[1:]  # ["刘华强","尼古拉斯赵四"]
user_list[:-1]  # ["范德彪", "刘华强"]
user_list[:]  # ["范德彪", "刘华强", "尼古拉斯赵四"]

# 修改一部分
user_list = ["范德彪", "刘华强", "尼古拉斯赵四"]
user_list[0:2] = [11, 22, 33, 44]  # [11, 22, 33, 44, '尼古拉斯赵四']
user_list = ["范德彪", "刘华强", "尼古拉斯赵四"]
user_list[2:] = [11, 22, 33, 44]  # ['范德彪', '刘华强', 11, 22, 33, 44]
user_list = ["范德彪", "刘华强", "尼古拉斯赵四"]
user_list[3:] = [11, 22, 33, 44]  # ['范德彪', '刘华强', '尼古拉斯赵四', 11, 22, 33, 44]
# 超出索引范围，直接放于最后
user_list = ["范德彪", "刘华强", "尼古拉斯赵四"]
user_list[10000:] = [11, 22, 33, 44]  # ['范德彪', '刘华强', '尼古拉斯赵四', 11, 22, 33, 44]
# 负数都是放在最前面，并且替换掉了索引0，且前取后不取
user_list = ["范德彪", "刘华强", "尼古拉斯赵四"]
user_list[-10000:1] = [11, 22, 33, 44]  #  [11, 22, 33, 44, '刘华强', '尼古拉斯赵四']

# 删除一部分
user_list = ["范德彪", "刘华强", "尼古拉斯赵四"]
del user_list[1:]  # ['范德彪']

"""
步长
"""
user_list = ["范德彪", "刘华强", "尼古拉斯赵四", "宋小宝", "刘能"]
#              0         1           2             3       4
user_list[1:4:2]  # ['刘华强', '宋小宝']
user_list[0::2]  # ['范德彪', '尼古拉斯赵四', '刘能']
user_list[1::2]  # ['刘华强', '宋小宝']
user_list[4:1:-1]  # 倒序  ['刘能', '宋小宝', '尼古拉斯赵四']

# 案例：实现列表的翻转
user_list = ["范德彪", "刘华强", "尼古拉斯赵四", "宋小宝", "刘能"]
new_data = user_list[::-1]  # ['刘能', '宋小宝', '尼古拉斯赵四', '刘华强', '范德彪']

data_list = ["范德彪", "刘华强", "尼古拉斯赵四", "宋小宝", "刘能"]
data_list.reverse()  # ['刘能', '宋小宝', '尼古拉斯赵四', '刘华强', '范德彪']

# 给你一个字符串请实现字符串的翻转？
name = "黄天佑"
name = name[::-1]
# name.reverse() 字符串是不能使用reverse的

"""
for 循环
"""
user_list = ["范德彪", "刘华强", "尼古拉斯赵四", "宋小宝", "刘能"]
for item in user_list:
    print(item)

# 序号取值 -> 有点画蛇添足
user_list = ["范德彪", "刘华强", "尼古拉斯赵四", "宋小宝", "刘能"]

for index in range(len(user_list)):
    item = user_list[index]
    # print(item)

"""
切记，循环的过程中对数据进行删除会出现问题
"""
user_list = ["刘的话", "范德彪", "刘华强", "刘尼古拉斯赵四", "宋小宝", "刘能"]
for item in user_list:
    if item.startswith("刘"):
        user_list.remove(item)
print(user_list)  # ['范德彪', '刘尼古拉斯赵四', '宋小宝']
"""
错误方式， 有坑，结果不是你想要的。

循环的时候同时进行删除，会导致for寻欢取出紊乱，
因为for循环取出了索引0，被删除了，范德彪就会变成索引0，for循环再次取索引1的时候，取出的就是刘华强了，
同理，刘华强被删除了，下一次取出的就直接是宋小宝，跳过了刘尼古拉斯赵四
"""

"""
正确的方式
倒着删除不会影响索引位置
"""
user_list = ["刘的话", "范德彪", "刘华强", "刘尼古拉斯赵四", "宋小宝", "刘能"]
for index in range(len(user_list) - 1, -1, -1):
    item = user_list[index]
    if item.startswith("刘"):
        user_list.remove(item)
print(user_list)  # ['范德彪', '宋小宝']
