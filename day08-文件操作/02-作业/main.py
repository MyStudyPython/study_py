"""
作业一：
用户注册和用户登录的功能

注册部分：用户名好和密码写入文件中
格式为:admin,123

登录部分：输入一次用户和密码，去文件中对比用户名和密码是否正确
"""
import os

script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
file_object_path1 = os.path.join(script_directory, "test1.txt")

# 注册部分
print("============开始注册===============")
f1 = open(file_object_path1, mode="wb")
while True:
    user = input(">>> 请输入姓名：")
    if user.upper() == "Q":
        break
    pwd = input(">>> 请输入密码：")

    user_info = f"{user},{pwd}\n"
    f1.write(user_info.encode("utf-8"))

f1.close()

print("============开始登录===============")
# 登录部分
f2 = open(file_object_path1, mode="rb")

user = input(">>> 请输入姓名：")
pwd = input(">>> 请输入密码：")

flag = False
for line in f2:
    line_string = line.decode("utf-8")
    line_string = line_string.strip()
    if line_string:
        data_list = line_string.split(",")
        if data_list[0] == user and data_list[1] == pwd:
            print("登录成功！！！")
            break
        else:
            print("登陆失败")
            break

f2.close()
