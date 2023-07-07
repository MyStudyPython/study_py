"""
with 上下文

有时会忘记关闭文件 file.close()
"""
import os

script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
object_path = os.path.join(script_directory, "read.txt")

file_object = open(object_path, mode="rb")
data = file_object.read()
file_object.close()  # 强调！！！一定要记得关闭

# 但是忘记了怎么办
print("=========开始==========")
# 离开时缩进，自动关闭文件
with open(object_path, mode="rb") as file_object:
    data = file_object.read().decode("utf-8")
    print(data)
print("=========结束==========")
