"""
判断字符串以xx开头或者结尾
"""
name = "中国人民共和国"
v1 = name.startswith("中国")  # True
v2 = name.endswith("中国")  # False

address = input("请输入你的家庭住址：")
if address.startswith("四川省"):
    print("川户")
else:
    print("非川户")

file_name = "xxxxxx.png"
if file_name.endswith(".png"):
    print("这是一张图片")
else:
    print("这不是一张图片")
