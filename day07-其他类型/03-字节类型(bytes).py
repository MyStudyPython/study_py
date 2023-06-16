name = "黄天宇"  # str字符串，底层是Unicode编码
# bytes字节，底层是UTF-8编码
data = name.encode("utf-8")  # b'\xe9\xbb\x84\xe5\xa4\xa9\xe5\xae\x87'

name = "黄天宇"  # str字符串，底层是Unicode编码
# bytes字节，底层是gbk编码
data = name.encode("gbk")  # b'\xbb\xc6\xcc\xec\xd3\xee'

"如果我们以后获取到一个字节，字节.decode()转化为字符串"
name = "黄天宇"
data = name.encode("utf-8")
old = data.decode("utf-8")  # "黄天宇"
