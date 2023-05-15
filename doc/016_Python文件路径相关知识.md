# 转义

我们知道windows用的是`\`，而linux用的是`/`，这会存在着一些问题隐患

``` bash
# windows系统文件路径
C:\tools\nmap
```

这有可能让程序以为换行符，让编译器无法区分

``` bash
C:\tools
map
```

所以我们在编写windows的路径时，一般采用两种方式：ß

-   加转义符号，例如`"C:\\tools\\nmap"`
-   路径前加r，例如`r"C:\tools\nmap"`

# 程序的当前路径

如果程序中使用了相对路径，那么一定要注意当前所在的位置

例如：在`/Users/kinght/PycharmProjects/Code/`路径下编写 `demo.py`文件

``` python
with open("a1.txt", mode='w', encoding='utf-8') as f:
    f.write("你好呀")
```

-   如果当前路径在`/Users/kinght/PycharmProjects/Code/`，运行程序可以直接使用

    ``` python
    python demo.py
    ```

-   如果当前路径在`/Users/kinght`，需要指向文件夹加文件名使用

        python PycharmProjects/Code/demo.py

# Python对文件路径的操作

在很多程序里面，其实很少使用相对路径，而绝对路径又不支持移动，在做框架和做项目开发的时候，会使用python的内置功能获取到路径

``` python
# 1.运行获得当前文件所在的路径
abs = os.path.abspath(__file__) # __file__指的是当前运行的python文件
print(abs) # /Users/kinght/code/python/lufe/day9/1/文件路径.py
# 2.获取当前文件所在文件夹的路径
path = os.path.dirname(abs)
print(path) # /Users/kinght/code/python/lufe/day9/1

## 1+2 的简写
base_dir = os.path.dirname(os.path.abspath(__file__))
print(base_dir) # /Users/kinght/code/python/lufe/day9/1

# 3.使用获得的路径
file_object = open('{}/file/info.txt'.format(path),mode='rt',encoding='utf-8')
print(file_object.read())
file_object.close()

# 4.路径拼接
## 步骤3有一个缺陷，windows和linux一个使用/一个使用\，互不兼容，所以这里直接使用路径拼接 -> base_dir=上面获取的路径，'file'=文件夹名,'info.txt'=文件名
file_path = os.path.join(base_dir,'file','info.txt')
print(file_path) # /Users/kinght/code/python/lufe/day9/1/file/info.txt
file_object = open(file_path,mode='rt',encoding='utf-8')
print(file_object.read())
file_object.close()

# 5.判断文件路径不存在
## os.path.exists(路径名) 存在返回True 不存在返回False
if os.path.exists(file_path):
    file_object = open(file_path, mode='rt', encoding='utf-8')
    print(file_object.read())
    file_object.close()
else:
    print("文件路径不存在")

# 6.创建文件夹 -> 文件夹存在会报错
mkfile_path = os.path.join(base_dir,'file','demo')
if not os.path.exists(mkfile_path):
    os.makedirs(mkfile_path) # 文件夹不存在就创立

# 7.判断是否为文件夹 True为文件夹 False为文件
print(os.path.isdir(mkfile_path)) # True
print(os.path.isdir(file_path)) # False

# 8.删除文件
os.remove(file_path)
# 9.删除文件夹 -> 需要倒入shutil
shutil.rmtree(mkfile_path)

# 10.拷贝文件夹
abs_path = os.path.abspath(__file__) # 获取文件路径
path = os.path.dirname(abs_path) # 获取文件所属文件夹的路径
copy_path = os.path.join(path,"file") # 被拷贝的文件夹路径
paste_path = os.path.join(path,'paste_file') # 粘贴文件夹路径
## 拷贝文件的命令(被拷贝，拷贝到)
shutil.copytree(copy_path,paste_path)

# 11.拷贝文件
abs_path = os.path.abspath(__file__) # 获取文件路径
path = os.path.dirname(abs_path) # 获取文件所属文件夹的路径
copy = os.path.join(path,'file','info.txt')
paste = os.path.join(path,'file','info2.txt')
shutil.copy(copy,paste)
```