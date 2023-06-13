"""
嵌套
列表是个"容器"，容器可以放很多东西
列表是个可变容器，列表中的常见功能是对列表本身进行操作
"""
# 定义
data_list = [11, 22, "xxx", ["中国移动", "中国联通"], 666, True]


data_list = [
    "黄琪翔",
    "海燕",
    "Bob",
    [988, 231, 3333, 666],
    "john",
    222,
    ["黄油漆", "白油漆", "绿油漆", "红油漆"],
    ["Django", "MongoDB", ["env", "venv"], "MySQL"],
]

# 取值
data_list[1]  # "海燕"
data_list[1][-1]  # "燕"
data_list[-1][2][-2]  # "env"

# 操作
data_list[0] = "黄飞鸿"
# ['黄飞鸿', '海燕', 'Bob', [988, 231, 3333, 666], 'john', 222, ['黄油漆', '白油漆', '绿油漆', '红油漆'], ['Django', 'MongoDB', ['env', 'venv'], 'MySQL']]
data_list[3][-1] = "88888"
# ['黄飞鸿', '海燕', 'Bob', [988, 231, 3333, '88888'], 'john', 222, ['黄油漆', '白油漆', '绿油漆', '红油漆'], ['Django', 'MongoDB', ['env', 'venv'], 'MySQL']]

"""
data_list[4][0] = "J"  # 报错？ john ---> John
'str' object does not support item assignment 字符串类型不可更改
"""

# 嵌套修改大小写
res = data_list[2].lower()
data_list  # 'Bob' 是大写
res  # 'bob' 是小写

# 嵌套增加值
data_list.append(456)
# ['黄飞鸿', '海燕', 'Bob', [988, 231, 3333, '88888'], 'john', 222, ['黄油漆', '白油漆', '绿油漆', '红油漆'], ['Django', 'MongoDB', ['env', 'venv'], 'MySQL'], 456]

data_list[-2].append("Python")
# ['黄飞鸿', '海燕', 'Bob', [988, 231, 3333, '88888'], 'john', 222, ['黄油漆', '白油漆', '绿油漆', '红油漆'], ['Django', 'MongoDB', ['env', 'venv'], 'MySQL', 'Python'], 456]

"""
列表是个可变容器，列表中的常见功能是对列表本身进行操作
"""

"""
案例一 循环输出商品信息
"""
goods = [["BEC高级", 1000], ["BEC中级", 600], ["BEC初级", 300]]

for i in range(len(goods)):
    message = f"{i} {goods[i][0]}"
    # print(message)

# 输出
# 0 BEC高级
# 1 BEC中级
# 2 BEC初级

"""
案例二 循环输出商品信息，用户去输入序号，根据用户输入的序号获取商品信息
"""
goods = [["BEC高级", 1000], ["BEC中级", 600], ["BEC初级", 300]]


while True:
    input_index = input("请输入选择商品的序号：")

    # print(input_index.isdecimal(), type(input_index)) # True <class 'str'>
    # 是数字但是是字符串类型

    if input_index.isdecimal():
        # 转换为整型
        input_index = int(input_index)
        # 范围
        if 0 < input_index < len(goods):
            good_info = goods[input_index]
            message = f"您选择的商品是{good_info[0]},价格是{good_info[1]}"
            print(message)
            break
        else:
            print("请再次输入")
    else:
        print("请输入数字")

"""
案例三 将敏感词替换成**
"""
key_list = ["日本", "台湾", "美国", "新疆"]
text_input = input("请输入评论：")
for key in key_list:
    text_input = text_input.replace(key, "**")
print(text_input)

"""
案例四 嵌套创建用户列表 一个用户名一个密码进行存储消息
"""
user_list = []
while True:
    user = input("请输入用户名(Q/q退出)：")
    if user.upper() == "Q":
        break
    pwd = input("请输入密码：")
    data = [user, pwd]
    user_list.append(data)
print(user_list)
