"""
其他

元素查找速度特别快
因存储原理特殊，集合的查找效率非常高(数据量大了才明显)


对比和嵌套
嵌套同样遵循是否可哈希的原则，可哈希就可以被嵌套

  类型    是否可变   是否有序   容器元素要求   是否可哈希   转换          定义空
  ------- ---------- ---------- -------------- ------------ ------------- -------------------
  list    是         是         无             否           list(其他)    `v=[]或v=list()`
  tuple   否         是         无             是           tuple(其他)   `v=()或v=tuple()`
  set     是         否         可哈希         否           set(其他)     `v=set()`


  

None类型
Python的数据类型中有一个特殊的值None，意味着这个值啥都不是 或 表示空。
相当于其他语言中 `null`作用一样。

在做预定义变量的时候，使用None可以在一定程度上可以帮助我们去节省内存(注意：暂不要考虑Python内部的缓存和驻留机制，具体情况后文介绍)


"""

"list/tuple查找速度慢，需要一个一个检索值的索引，然后再查询值"
user_list = ["kinght", "aym", "ayi"]
if "kinght" in user_list:
    print("在")
else:
    print("不在")

user_tuple = ("kinght", "aym", "ayi")
if "aym" in user_tuple:
    print("在")
else:
    print("不在")

"查找速度快，直接查询值"
user_set = {"kinght", "aym", "ayi"}
if "kkk" in user_set:
    print("在")
else:
    print("不在")


"对比和嵌套"
data_list = [
    "alex",
    11,
    (11, 22, 33, {"alex", "eric"}, 22),
    [11, 22, 33, 22],
    {11, 22, (True, ["中国", "北京"], "沙河"), 33},  # 列表不能哈希，所以报错
]

"""
注意：
由于True和False本质上存储的是 1 和 0，而集合又不允许重复，
所以在整数0、1和False、True出现在集合中会有如下现象：
"""
v1 = {True, 1}
print(v1)  # {True} True和False在计算机中是1和0表示的，所以集合会只有一个True
v2 = {1, True}
print(v2)  # {1}
v3 = {0, False}
print(v3)  # {0}
v4 = {False, 0}
print(v4)  # {False}

"None类型"
v1 = None
v2 = None

v1 = [11, 22, 33, 44]
v2 = [111, 22, 43]

v3 = []  # 创建空列表，内存会开辟列表所需要的空间
v4 = []

v3 = [11, 22, 33, 44]
v4 = [111, 22, 43]
