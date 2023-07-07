"""
1. 读文件 (打开文件、读取文件、关闭文件)
2. 写文件 (打开文件、写文件、关闭文件)

文件是utf-8 进行存储的
所以需要转码和解码
"""

name = "马化腾"
data = name.encode("utf-8")  # b'\xe9\xa9\xac\xe5\x8c\x96\xe8\x85\xbe'
rester = data.decode("utf-8")  # 马化腾

"""
读文件 --- 文本
"""
import os

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


"""
写文件 --- 会自动生成文件(文件不存在，则创建文件。文件存在，则清空文件)
"""
# 1. 打开文件
#   - "write.txt"  文件路径
#   -  mode = "wb"   写文件的模式打开
script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
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

    user_info = f"{name},{pwd}"
    print(user_info)
    f1.write(user_info.encode("utf-8"))

f1.close()
