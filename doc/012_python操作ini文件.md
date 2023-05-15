# ini文件

ini文件是Initialization
File的缩写，平时用于存储软件的的配置文件。例如：MySQL数据库的配置文件。

``` ini
[mysqld]
datadir=/var/lib/mysql
socket=/var/lib/mysql/mysql.sock
log-bin=py-mysql-bin
character-set-server=utf8
collation-server=utf8_general_ci
log-error=/var/log/mysqld.log
# Disabling symbolic-links is recommended to prevent assorted security risks
symbolic-links=0

[mysqld_safe]
log-error=/var/log/mariadb/mariadb.log
pid-file=/var/run/mariadb/mariadb.pid

[client]
default-character-set=utf8
```

这种格式是可以直接使用open来出来，考虑到自己处理比较麻烦，所以Python为我们提供了更为方便的方式。

# 文件操作方式

``` python
import configparser # 操作ini文件的模块

# configparser.ConfigParser() 固定搭配
config = configparser.ConfigParser()
config.read('my.ini',encoding='utf-8')

# 1.获取所有的节点
res = config.sections()
print(res) # ['mysqld', 'mysqld_safe', 'client']

# 2.获取节点的内容
result = config.items('mysqld')
print(result)
'''
输出结果为元组
[('datadir', '/var/lib/mysql'), ('socket', '/var/lib/mysql/mysql.sock'), ('log-bin', 'py-mysql-bin'), ('character-set-server', 'utf8'), ('collation-server', 'utf8_general_ci'), ('log-error', '/var/log/mysqld.log'), ('symbolic-links', '0')]
'''
## 因为输出为元组，所以可以使用字典进行接收
for key,value in config.items('mysqld'):
    print(key,value)
'''
datadir /var/lib/mysql
socket /var/lib/mysql/mysql.sock
log-bin py-mysql-bin
character-set-server utf8
collation-server utf8_general_ci
log-error /var/log/mysqld.log
symbolic-links 0
'''

# 3.获取某个节点下的键对应的值
result = config.get('mysqld','collation-server')
print(result)

# 4.判断文件里是否有某个节点
v1 = config.has_section("demo")
print(v1)

# 5.添加节点
## 只是添加到内存，没有写入文件
config.add_section("group")
config.set("group","name","kinght") # 添加节点内容
config.set("group","passwd","12345")
# 也可以添加其他节点的内容
config.set("mysqld","user","kinght")
## 写入文件new
config.write(open('new.ini',mode='w',encoding='utf-8'))

# 6.删除
## 同样也是在内存中操作，需要专门写入文件
config.remove_section("client")
config.remove_option('group','name') # 需要写节点名和键名
## 写入文件
config.write(open('new.ini',mode='w',encoding='utf-8'))

# 7.修改 -> 其实就是写入，进行了覆盖
config.set('group','passwd','aym')
config.write(open('new.ini',mode='w',encoding='utf-8'))
```