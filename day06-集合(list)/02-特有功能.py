"""
特有功能

添加元素 v1.add(元素)  只能提供一个一个添加，不能添加多个,添加多个压迫写多次
删除元素 v2.discard(元素)
交集 s1.intersection(s2)
并集
差集
"""

"添加元素"
data = set()
# 只能提供一个一个添加，不能添加多个,添加多个压迫写多次
# data.add("谢尔顿", "米西", "珍妮")
data.add("谢尔顿")  # {'谢尔顿'}
data.add("米西")  # {'米西', '谢尔顿'}
data.add("珍妮")  # {'米西', '谢尔顿', '珍妮'}

"删除元素"
v1 = {11, 22}
v1.discard(11)  # {22}
v1.discard(33)  # 没有不会报错,与列表的remove不同

"交集"
s1 = {"刘能", "赵四", "⽪⻓⼭"}
s2 = {"刘科⻓", "冯乡⻓", "⽪⻓⼭"}
# 取两个集合的交集
# 方案1
s3 = s1.intersection(s2)  # {"⽪⻓⼭"}
# 方案2
s4 = s1 & s2  # {"⽪⻓⼭"}

"并集"
s1 = {"刘能", "赵四", "⽪⻓⼭"}
s2 = {"刘科⻓", "冯乡⻓", "⽪⻓⼭"}
# 取两个集合的并集
# 方案1
s3 = s1.union(s2)  # {"刘能", "赵四", "⽪⻓⼭","刘科⻓", "冯乡⻓", }
# 方案二
s3 = s1 | s2  # {"刘能", "赵四", "⽪⻓⼭","刘科⻓", "冯乡⻓", }

"差集"
s1 = {"刘能", "赵四", "⽪⻓⼭"}
s2 = {"刘科⻓", "冯乡⻓", "⽪⻓⼭"}
# 取两个集合的差距 -> 顺序决定谁取谁
# 方案1
s3 = s1.difference(s2)  # 差集，s1中有且s2中没有的值 {'赵四', '刘能'}
s4 = s2.difference(s1)  # 差集，s2中有且s1中没有的值 {'冯乡⻓', '刘科⻓'}
# 方案二
s5 = s1 - s2  # 差集，s1中有且s2中没有的值
s6 = s2 - s1  # 差集，s2中有且s1中没有的值
