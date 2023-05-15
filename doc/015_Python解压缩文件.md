# 压缩文件

``` python
import shutil

"""
# base_name，压缩后的压缩包文件
# format，压缩的格式，例如："zip", "tar", "gztar", "bztar", or "xztar".
# root_dir，要压缩的文件夹路径
"""
# 将上一级文件夹的19_excel文件夹打包成zip格式存放于file/20(原本没有是程序新建的)
shutil.make_archive(base_name=r'file/20',format='zip',root_dir=r'../19_excel')
```

# 解压文件

``` python
"""
# filename，要解压的压缩包文件
# extract_dir，解压的路径
# format，压缩文件格式
"""
# 将file文件夹的压缩文件20.zip解压到new_file文件夹(新建)，压缩格式为zip
shutil.unpack_archive(filename=r'file/20.zip',extract_dir='new_file',format='zip')
```

# 案例

``` python
import os,shutil,requests

# 1.下载文件
file_url = 'https://files.cnblogs.com/files/wupeiqi/HtmlStore.zip'
res = requests.get(url=file_url)
print(res.content)
# 2.将下载的文件保存到当前执行脚本同级目录下 /files/package/ 目录下（且文件名为HtmlStore.zip）
## 获取文件路径
abs_path = os.path.abspath(__file__)
dir_path = os.path.dirname(abs_path)
## 保存路径
file_path = os.path.join(dir_path,'files','package')
## 保存的文件完整路径
### 获取文件名
file_name = file_url.split('/')[-1] # 获取文件名
### 构成路径
down_file = os.path.join(file_path,file_name)
### 检查保存文件夹是否存在，不存在则创建
if not os.path.exists(file_path):
    os.makedirs(file_path)
## 解压到的目录
unzip_path = os.path.join(dir_path,'files','html')
## 下载文件
with open(down_file,mode='wb') as f:
    f.write(res.content)
# 3.在将下载下来的文件解压到 /files/html/ 目录下
shutil.unpack_archive(filename=down_file,extract_dir=unzip_path,format='zip')
```