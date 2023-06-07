"""
Python中为所有的列表类型的数据提供了一批独有的功能。

追加            append      批量追加 extend
插入            insert
根据值删除       remove     如果元素不存在则会报错
剔除某个元素     pop
清空原列表       clear()   
根据值获取索引   index      如果元素不存在则会报错
列表元素排序     sort()
反转原列表       reverse()
"""

# 1.追加 append
## 案例 --- 输入你的爱好，并输出出来，输出Q退出
hobby_list = []
while True:
    hobby = input('请输入你的爱好：')
    if hobby.upper() == 'Q':
       break
    hobby_list.append(hobby)

# 批量追加
## 将一个列表中的元素逐一添加另外一个列表
tools = ["搬砖","菜刀","榔头"]
tools.extend( [11,22,33] ) # ["搬砖","菜刀","榔头",11,22,33]

# 相当于
tools = ["搬砖","菜刀","榔头"]
num = [11,22,33]
for i in num:
    tools.append(i)

# 2. 插入，在原列表的指定索引位置插入值
user_list = ["苍老师","有坂深雪","大桥未久"]
user_list.insert(0,"xxx") # ["xxx","苍老师","有坂深雪","大桥未久"]

# 当索引值小于0的时候，会永远将数据放在最前面，
# 如果索引大于长度，会将数据放在最后面->不会报错

# 案例 --- 排队买票,把姓李的放到最前面，输入Q退出
user_list = []
while True:
    name = input("请输入购买火车票用户姓名（Q/q退出）：")
    if name.upper() == 'Q':
        break
    if name.startswith('李'):
        user_list.insert(0,name)
    else:
        user_list.append(name)

# 3.根据值删除 remove
user_list = ["王宝强","陈羽凡","amber","贾乃亮","amber"]
user_list.remove("amber")

"""
如果元素不存在则会报错
"""

# 如果要避免报错，可以提前判断是否存在这个值
user_list = ["王宝强","陈羽凡","amber","贾乃亮","amber"]
if "amber" in user_list: # 判断user_list是否包含"amber"
	user_list.remove("amber")
        
"""
一次只删除一个值，如果需要把列表当中的多个值删除需要循环
"""

# 案例 --- 自动抽奖程序工号1到工号200 -> 由于员工工号只有一个，所以抽中需要删除工号避免再次抽中
import random

user_list =[]
for i in range(1,201):
    id = "工号-{}".format(i)
    user_list.append(id)

# 随机从data_list抽取一个值出来
data = random.choice(user_list)
print("获得三等奖的是：",data)

user_list.remove(data)
data = random.choice(user_list)
print("获得二等奖的是：",data)

user_list.remove(data)
data = random.choice(user_list)
print("获得一等奖的是：",data)


# 4.根据索引剔除某个元素 pop
user_list = ["王宝强","陈羽凡","Alex","贾乃亮","Alex"]
#               0       1      2      3       4
user_list.pop(1) #  ["王宝强","Alex","贾乃亮","Alex"]

# 如果不写序号，默认删除最后一个
user_list.pop() # ["王宝强","Alex","贾乃亮"]

# 案例 --- 购票系统
# 1.获取购买票的人员
# 2.但是余票只有三张 ----> 前三个人有票
# 3.通知其他人，无票，选择其他的出行方式
user_list = []
while True:
    name = input("成都 --> 深圳  请输入购票人姓名，按Q结束：").strip()
    if name.upper() == 'Q':
        break
    user_list.append(name)

# 余票三张
ticket_count = 3
# for count in range(ticket_count):
#   choice_name = user_list.pop(0) # 列表中取出序号为0的元素，然后从列表中删除
#   print("尊敬的旅客{},您的票已出".format(choice_name))

success_list = user_list[:ticket_count]
for name in success_list:
    print(f"尊敬的旅客{name}，您的票已出")

others_list = user_list[ticket_count:]
# # 未购票成功
# others = ",".join(user_list)
# print("尊敬的旅客朋友{}，非常抱歉的通知您，由于余票不足，请您使用其他的交通方式".format(others))
if others_list:
    others = ", ".join(others_list)
    print(f"尊敬的{len(others_list)}位旅客，很抱歉由于余票不足，无法购票，请您使用其他的交通方式。")

# 5. 清空列表
user_list = ["王宝强","陈羽凡","Alex","贾乃亮","Alex"]
user_list.clear() # []

# 6.根据值获取索引
"""
如果元素不存在则会报错
"""
user_list = ["王宝强","陈羽凡","Alex","贾乃亮","Alex"]
#               0       1      2       3      4
if "Alex" in user_list: # 先检查元素是否在列表
	index = user_list.index("Alex") # 2
else:
    print("不存在")

# 7.列表元素排序
num_list = [11, 22, 4, 5, 11, 99, 88]
num_list.sort()  # 让num_list从小到大排序
"""
反转
"""
num_list.sort(reverse=True)  # # 让num_list从大到小排序 reverse=True

"""
中文排序  根据Unicode
"""
user_list = ["叶子","青青","牛"]
user_list.sort() # ['叶子', '牛', '青青']

