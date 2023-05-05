name = "xxx"                      # 字符串类型：unicode来存储（ucs4）
data = name.encode('utf-8')       # 字节类型：  utf-8编码来存储
print(data)   # b'xxx

"""
在Python开发中，以后再去做文件存储或网络传输时，不能直接用字符串，
而是需要将字符串压缩成utf-8编码的字节，
然后再来传输和存储。
"""
# 在文件中写一个字符串
name = "xxx"

# 1. 打开文件
file_object = open('./vip.txt', mode="ab")

# 2.写入内容
file_object.write(name.encode('utf-8'))

# 3.关闭文件
file_object.close()
