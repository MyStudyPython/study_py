"""
1. 写文件 (打开文件、写文件、关闭文件)
2. 读文件 (打开文件、读取文件、关闭文件)

文件是utf-8 进行存储的
所以需要转码和解码
"""

name = "马化腾"
data = name.encode("utf-8")  # b'\xe9\xa9\xac\xe5\x8c\x96\xe8\x85\xbe'
rester = data.decode("utf-8")  # 马化腾

"""
写文件 --- 会自动生成文件(文件不存在，则创建文件。文件存在，则清空文件)
"""
import os

# 1. 打开文件
#   - "write.txt"  文件路径
#   -  mode = "wb"   写文件的模式打开
# 获取当前脚本文件的绝对路径
script_path = os.path.abspath(__file__)
# 获取当前脚本文件所在的目录路径
script_directory = os.path.dirname(script_path)
# 将目录路径和文件名拼接成完整的文件路径
file_path_write = os.path.join(script_directory, "write.txt")

file_object = open(file_path_write, mode="wb")
# 2. 写文件
name = "今天星期五了！！！"
file_object.write(name.encode("utf-8"))
# 3. 关闭文件
file_object.close()

"换行方式写"
file_object = open(file_path_write, mode="wb")

v1 = "我是星期五\n"  # unicode
file_object.write(v1.encode("utf-8"))
v2 = "我是星期六\n"
file_object.write(v2.encode("utf-8"))
v3 = "我是星期天\n"
file_object.write(v3.encode("utf-8"))

file_object.close()

"写入非文本文件 --- 图片(像素点)"
# 读取图片信息
file_path_photo = os.path.join(script_directory, "photo1.jpeg")

# 读取图片信息
f1 = open(file_path_photo, mode="rb")
data = f1.read()
f1.close()

file_path_photo = os.path.join(script_directory, "photo2.jpeg")
# 写入图片信息
f2 = open(file_path_photo, mode="wb")
f2.write(data)
f2.close()


"""
案例一
实现用户注册，每注册一个用户就在文件中写入一行(循环操作，直到用户q终止)

admin,123 格式
"""
script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
object_path_test1 = os.path.join(script_directory, "test1.txt")

f1 = open(object_path_test1, mode="wb")
while True:
    user = input(">>>> 请输入用户名：")
    if user.upper() == "Q":
        break
    pwd = input(">>>> 请输入密码：")

    # 真的写到了文件中吗，还是计算器的内容（缓冲区）
    user_info = f"{user},{pwd}\n"
    f1.write(user_info.encode("utf-8"))

    # 强制将内容中的数据写入硬盘(文件中)
    f1.flush()

f1.close()


# 真的写到了文件中吗，还是计算器的内容（缓冲区）
# f1.write(user_info.encode("utf-8"))
# 强制将内容中的数据写入硬盘(文件中)
# f1.flush()
"区别在于 用户输入时 write执行一次 flush就会把内容写入到文件中一次"


"""
写文件
追加模式 
而不是上面的全部覆盖

文件不存在，则创建文件。
文件存在，则打开文件，写内容时，永远写在文件的尾部。
"""
object_path_add = os.path.join(script_directory, "add.txt")
file_object = open(object_path_add, mode="ab")
file_object.write("不知道写点什么\n".encode("utf-8"))
file_object.close()


"""
读文件 --- 文本
"""

# 1. 打开文件
#   - "read.txt"  文件路径
#   -  mode = "rb"   读文件的模式打开
#      r = 读取文件   b = 二进制内容

# 获取当前脚本文件的绝对路径
script_path = os.path.abspath(__file__)  # d:\practice\study_py\day08-文件操作\01-快速读写.py
# 获取当前脚本文件所在的目录路径
script_directory = os.path.dirname(script_path)  # d:\practice\study_py\day08-文件操作
# 将目录路径和文件名拼接成完整的文件路径
file_path_read = os.path.join(script_directory, "read.txt")


file_object = open(file_path_read, mode="rb")
# 2. 读取文件
#   - .read() 读取所有的文件内容，赋值给data
data = file_object.read()
# 3. 关闭文件
file_object.close()

# print(data)
# 字节类型
# b'12312312\n231241241\n123124124\n21312341'
text = data.decode("utf-8")  # 字节转字符串
# print(text)

# 将读取到的字符串切割并获取到每一行数据
row_list = text.strip().split("\n")
# print(row_list)

"每次读取文本文件都需要decode未免显得太过麻烦，所以其实可以直接用rt模式"
# r读取，t文本内容。 encoding="utf-8" 编码成utf-8
file_object = open(file_path_read, mode="rt", encoding="utf-8")
data = file_object.read()
file_object.close()


"读文件 --- 图片"
# photo.jpeg
file_path_photo = os.path.join(script_directory, "photo1.jpeg")
file_object = open(file_path_photo, mode="rb")
data = file_object.read()
file_object.close()
# print(data)
# 图片等原始二进制内容
# b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\...后续内容省略

"判断路径是否存在"
exists1 = os.path.exists("read.txt")
exists2 = os.path.exists(file_path_read)
# 存在返回True 不存在返回False
# print(exists1) # False
# print(exists2) # True


"当读取很大的文件时，可以逐行去读取"
file_object = open(file_path_read, "rb")

# 第一种 readline() 一行一行的读 过于麻烦
# line1 = file_object.readline().decode("utf-8")
# print(line1)
# line2 = file_object.readline().decode("utf-8")
# print(line2)

# 第二种 for循环
for line in file_object:
    line_string = line.decode("utf-8")
    line_string = line_string.strip()
    # print(line_string)


file_object.close()

"""
案例二
读取以下文件中的企业名称
"N晶科" 那一列
"""
script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
object_file_test2 = os.path.join(script_directory, "data.txt")

f2 = open(object_file_test2, mode="rb")
# 文件很大的时候需要逐行去读取
for line in f2:
    line_string = line.decode("utf-8")
    line_string = line_string.strip()
    if line_string:
        data = line_string.split(",")[1]
        print(data)

f2.close()
