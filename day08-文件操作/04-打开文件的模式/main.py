"""
上文我们基于文件操作基本实现了读、写的功能，
其中涉及的文件操作模式：rt、rb、wt、wb，
其实在文件操作中还有其他的很多模式。


--------- ---------------------------------------------------------------
'r'       以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式
'w'       打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内
容会被删除。如果该文件不存在，创建新文件。
'x'       写模式，新建一个文件，如果该文件已存在则会报错。
'a'       打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，
新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。

'b'       二进制模式。
't'       文本模式 (默认)。

'+'       打开一个文件进行更新(可读可写)。

默认模式是rt 打开读取文本
"""

import os

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)


"""
wb 和 w 区别
"""
object_path = os.path.join(script_dir, "write.txt")
data = "opencv 是什么东西啊"

"wb 写"
file_object = open(object_path, mode="wb")
file_object.write(data.encode("utf-8"))

"w 写"
file_object = open(object_path, mode="w", encoding="utf-8")
file_object.write(data)


file_object.close()


"""
ab 和 a 区别
"""
object_path = os.path.join(script_dir, "write.txt")

"ab 追加"
file_object = open(object_path, mode="ab")
file_object.write(data.encode("utf-8"))

"a 追加"
file_object = open(object_path, mode="a")
file_object.write(data)

file_object.close()


"""
rb 和 r 区别
"""
object_path = os.path.join(script_dir, "read.txt")

"rb 读"
file_object = open(object_path, mode="rb")
data = file_object.read()
data_string = data.decode("utf-8")
# print(data_string)

"r 读"
file_object = open(object_path, mode="r")
# 直接读取的是字符串
data_string = file_object.read()
# print(data_string)

file_object.close()
