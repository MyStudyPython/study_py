"""
公共功能

长度 len
for循环
是否包含 in
"""
"长度 len"
v = {"刘能", "赵四", "尼古拉斯"}
data = len(v)  # 3

"for 循环"
v = {"刘能", "赵四", "尼古拉斯"}
for i in v:
    print(v)

"是否包含 in"
v = {"刘能", "赵四", "尼古拉斯"}
if "赵四" in v:
    print("存在")
else:
    print("不存在")
