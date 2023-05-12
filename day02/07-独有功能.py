"""
索引
"""
#       0  1  2  3 4 5 6 7 8 9 10 11
text = "我 在 学 习 p y t h o n 课 程"

text[0]  # "我"
text[8]  # "我"
text[10]  # "课"

# text[100]  # 超栈 报错

v1 = len(text) - 1
text[v1]  # 程


# 依次打印 text的值
text = "我 在 学 习 p y t h o n 课 程"
index = 0
while index < len(text):
    print(text[index])
    index += 1

"""
倒序输出
"""
#       0  1  2  3 4 5 6 7 8 9 10 11
#                            -3-2-1
text = "我 在 学 习 p y t h o n 课 程"
text[-1]  # 程


"""
切片 前选后不选
"""
text = "我 在 学 习 p y t h o n 课 程"
text[0:2]  # "我在"
text[2:8]  # "学习pytho"
text[2:-1]  # "学习python课"
text[2:]  # "学习python课程"
text[:-1]  # "我在学习python课"
text[:]  # "我在学习python课程"

num = 189
# 1.转换成二进制的字符串
bin_string = bin(num)  # 0b10111101

# 2.不要ob,data = "10111101"
data = bin_string[2:]  # 10111101

# 3.将二进制字符串补足16位，在他前面补0
result = data.zfill(16)
print(result)  # 0000000010111101

"""
循环
"""
# 给你一个字符串 data= "我要学习python编程"，让他循环字符串中的每个元素
# - while 循环 + 索引
# - for 循环

# while 循环
data = "我要学习python编程"
index = 0
while index < len(data):
    char = data[index]
    print(char)
    index += 1


# for循环
data = "我要学习python编程"
for item in data:
    print(item)


"""
range函数作用，帮助你生成一个数字列表
"""
v1 = range(5)  # [0,1,2,3,4]
v2 = range(5, 10)  # [5,6,7,8,9]
v3 = range(5, 10, 2)  # [5,7,9]
v4 = range(10, 0, -1)  # [10,9,8,7,6,5,4,3,2,1]

for item in v1:
    print(item)


for item in v2:
    print(item)

for item in v4:
    print(item)

# 请实现获取字符串中的每个元素并输出
data = "我要学习python编程"

# 方式一
index = 0
while index < len(data):
    print(data[index])
    index += 1

# 方式二
for item in data:
    print(item)

# 方式三
for idx in range(len(data)):
    print(data[idx])
