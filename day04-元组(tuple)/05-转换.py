"""
其他类型转换成元组
`tuple(其他类型)`

目前只有字符串和列表可以转换为元组
"""

# data = tuple(其他)
# str / list

name = "武沛齐"
data = tuple(name)
print(data)  # 输出 ("武","沛","齐")

name = ["武沛齐", 18, "pythonav"]
data = tuple(name)
print(data)  # 输出 ("武沛齐",18,"pythonav")
