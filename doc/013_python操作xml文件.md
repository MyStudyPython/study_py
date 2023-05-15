# XML格式文件

[可扩展标记语言](https://baike.baidu.com/item/%E5%8F%AF%E6%89%A9%E5%B1%95%E6%A0%87%E8%AE%B0%E8%AF%AD%E8%A8%80/2885849){target="_blank"
rel="noopener"}，是一种简单的数据存储语言，XML 被设计用来传输和存储数据

-   存储，可用来存放配置文件，例如：java的配置文件
-   传输，网络传输时以这种格式存在，例如：早期ajax传输的数据、soap协议等

``` python
<data>
    <country name="Liechtenstein">
        <rank updated="yes">2</rank>
        <year>2023</year>
        <gdppc>141100</gdppc>
        <neighbor direction="E" name="Austria" />
        <neighbor direction="W" name="Switzerland" />
    </country>
    <country name="Singapore">
        <rank updated="yes">5</rank>
        <year>2026</year>
        <gdppc>59900</gdppc>
        <neighbor direction="N" name="Malaysia" />
    </country>
    <country name="Panama">
        <rank updated="yes">69</rank>
        <year>2026</year>
        <gdppc>13600</gdppc>
        <neighbor direction="W" name="Costa Rica" />
        <neighbor direction="E" name="Colombia" />
    </country>
</data>
```

例如：[https://developers.weixin.qq.com/doc/offiaccount/Message_Management/Receiving_standard_messages.html](https://developers.weixin.qq.com/doc/offiaccount/Message_Management/Receiving_standard_messages.html){target="_blank"
rel="noopener"}

# xml文件操作

## 读取文件和内容

### 打开xml文件

python提供操作`xml`格式文件的函数是`xml.etree库中的ElementTree模块`

``` python
from xml.etree import ElementTree as ET
# 给ElementTree取个别名ET

# 读取解析xml文件
tree = ET.parse("xo.xml") # ET打开xml文件

# 获取根标签
root = tree.getroot()
print(root) # 获取到data <Element 'data' at 0x7ff39020c590>
```

而网络或内存中存在的`xml`文件可以直接通过`ET.XML(res.content)`读取根标签

``` python
from xml.etree import ElementTree as ET
import requests

# 通过requests抓取rss数据
res = requests.get(
    url='https://www.kinghtxg.com/atom.xml',
    headers={
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
    }
)

# 获取根标签
root = ET.XML(res.content)
print(root) # <Element '{http://www.w3.org/2005/Atom}feed' at 0x7f8b784e36d0>
```

### 读取节点数据

只需要将根标签进行循环，即可获得根标签的子标签

#### 循环取标签

以读取`xo.xml`为例

``` python
from xml.etree import ElementTree as ET
# 给ElementTree取个别名ET

# 读取解析xml文件
tree = ET.parse("xo.xml") # ET打开xml文件

# 获取根标签
root = tree.getroot()
print(root) # 获取到data <Element 'data' at 0x7ff39020c590>

# 获取根标签的子标签
for child in root:
    print(child.tag)
'''<country name="Liechtenstein"> 获取 country
country
country
country
'''
for child in root:
    print(child.attrib)
'''<country name="Liechtenstein"> 获取 {'name':'Liechtenstein'}
{'name': 'Liechtenstein'}
{'name': 'Singapore'}
{'name': 'Panama'}
'''

# 获取子标签内部信息
for child in root:
  # 循环取子标签中的信息
    for node in child:
        print(node.tag,node.attrib,node.text)
        # node.tag == 标签名
        # node.attrib == 标签属性
        # node.text == 标签中间的文本内容
'''
rank {'updated': 'yes'} 2
year {} 2023
gdppc {} 141100
neighbor {'direction': 'E', 'name': 'Austria'} None
neighbor {'direction': 'W', 'name': 'Switzerland'} None
rank {'updated': 'yes'} 5
year {} 2026
gdppc {} 59900
neighbor {'direction': 'N', 'name': 'Malaysia'} None
rank {'updated': 'yes'} 69
year {} 2026
gdppc {} 13600
neighbor {'direction': 'W', 'name': 'Costa Rica'} None
neighbor {'direction': 'E', 'name': 'Colombia'} None
'''
```

#### 取具体的标签

``` python
from xml.etree import ElementTree as ET

content = """
<data>
    <country name="Liechtenstein" id="999" >
        <rank>2</rank>
        <year>2023</year>
        <gdppc>141100</gdppc>
        <neighbor direction="E" name="Austria" />
        <neighbor direction="W" name="Switzerland" />
    </country>
     <country name="Panama">
        <rank>69</rank>
        <year>2026</year>
        <gdppc>13600</gdppc>
        <neighbor direction="W" name="Costa Rica" />
        <neighbor direction="E" name="Colombia" />
    </country>
    <cou name="Panama">
        <rank>69</rank>
        <year>2026</year>
        <gdppc>13600</gdppc>
        <neighbor direction="W" name="Costa Rica" />
        <neighbor direction="E" name="Colombia" />
    </cou>
</data>
"""

# 获取根标签 data
root = ET.XML(content)

# 获取data根标签中的子标签cou
country_object = root.find('cou')
print(country_object.tag)
# 读取cou子标签中的信息
gdppc_object = country_object.find('gdppc')
print(gdppc_object.tag,gdppc_object.attrib,gdppc_object.text)

# 读取root中所有的year标签
for child in root.iter('year'):
    print(child.tag,child.text)
'''
year 2023
year 2026
year 2026
'''

# find选择第一个country子标签
country_1 = root.find('country')
print(country_1) # <Element 'country' at 0x7fb42008c630>
country_11 = country_1.find('rank')
print(country_11.text) # 2

# findall 找到所有的country子标签
country_2 = root.findall('country')
print(country_2)
```

### 修改和删除节点

``` python
from xml.etree import ElementTree as ET

content = """
<data>
    <country name="Liechtenstein">
        <rank>2</rank>
        <year>2023</year>
        <gdppc>141100</gdppc>
        <neighbor direction="E" name="Austria" />
        <neighbor direction="W" name="Switzerland" />
    </country>
     <country name="Panama">
        <rank>69</rank>
        <year>2026</year>
        <gdppc>13600</gdppc>
        <neighbor direction="W" name="Costa Rica" />
        <neighbor direction="E" name="Colombia" />
    </country>
</data>
"""

# 获取根节点
root = ET.XML(content)
# 读取第一个country下的第一个rank信息
rank = root.find('country').find('rank')
print(rank.text)

# 修改rank信息
rank.text = '999'
print(root.find('country').find('rank').text) # 已被修改
# 添加节点信息 -> 在rank下
rank.set('update','2021-12-12')
print(rank.text,rank.attrib)

# 删除节点
root.remove( root.find('country') )
print(root.findall('country'))

# 写入硬盘保存文件
tree = ET.ElementTree(root)
tree.write("aaa.xml", encoding='utf-8')
```

### 构建文档

构建文档我们可以使用`ElementTree.Element`和`根节点.makeelement`以及`ElementTree.SubElement`两种方式进行创建

#### ElementTree.Element {#elementtreeelement}

``` python
from xml.etree import ElementTree as ET

# 创建根节点
root = ET.Element('home')

# 创建只是创建，要添加后才会和根节点参生关系
# 创建根节点 -> 儿子1
son1 = ET.Element('son',{'name':'儿子1'})
# 创建根节点 -> 儿子2
son2 = ET.Element('son',{'name':'儿子2'})

# 在大儿子中创建两个孙子
grandson1 = ET.Element('grandson',{'name':'儿11'})
grandson2 = ET.Element('grandson',{'name':'儿12'})
son1.append(grandson1)
son1.append(grandson2)

# 把儿子放入根节点中
root.append(son1)
root.append(son2)

# 写入文档
tree = ET.ElementTree(root)
tree.write("zzss.xml",encoding='utf-8',short_empty_elements=False)

'''
hort_empty_elements=False 是否使用短标签
含义：对于内部没有值的标签，例如：<grandson name="儿12"></grandson> 其实可以简写为<grandson name="儿12"/>
'''
```

效果

``` xml
<home>
    <son name="儿子1">
        <grandson name="儿11"></grandson>
        <grandson name="儿12"></grandson>
    </son>
    <son name="儿子2"></son>
</home>
```

#### 根节点.makeelement {#根节点makeelement}

``` python
from xml.etree import ElementTree as ET

# 创建根节点
root = ET.Element("famliy")


# 创建大儿子
son1 = root.makeelement('son', {'name': '儿1'})
# 创建小儿子
son2 = root.makeelement('son', {"name": '儿2'})

# 在大儿子中创建两个孙子
grandson1 = son1.makeelement('grandson', {'name': '儿11'})
grandson2 = son1.makeelement('grandson', {'name': '儿12'})

son1.append(grandson1)
son1.append(grandson2)


# 把儿子添加到根节点中
root.append(son1)
root.append(son2)

tree = ET.ElementTree(root)
tree.write('oooo.xml',encoding='utf-8')
```

效果

``` xml
<famliy>
    <son name="儿1">
        <grandson name="儿11" />
        <grandson name="儿12" /></son>
    <son name="儿2" />
</famliy>
```

#### ElementTree.SubElement {#elementtreesubelement}

这种方式是直接添加到节点中的

``` python
from xml.etree import ElementTree as ET

# 创建根节点
root = ET.Element('family')

# 创建子节点 -> 直接写入根节点中
son1 = ET.SubElement(root,'son',attrib={'name':'儿子1'})
son2 = ET.SubElement(root,'son',attrib={'name':'儿子2'})

# 创建子节点的子节点
grandson1 = ET.SubElement(son1,'grandson',attrib={'name':'孙1'})
grandson1.text = '孙子'
grandson2 = ET.SubElement(son1,'grandson',attrib={'name':'孙2'})

et = ET.ElementTree(root)
et.write('test.xml',encoding='utf-8')
```

效果

``` xml
<family>
    <son name="儿子1">
        <grandson name="孙1">孙子</grandson>
        <grandson name="孙2" />
    </son>
    <son name="儿子2" />
</family>
```

# 案例 1: 读取rss.xml {#案例-1-读取rssxml}

www.kinghtxg.com的rss信息：

![](https://skystarry-1251157247.cos.ap-chengdu.myqcloud.com/img/image-20211212133957463.png){loading="lazy"}

从rss文件中获取网站的目录标题版权等信息

``` python
from xml.etree import ElementTree as ET
import requests

res = requests.get(
    url='https://www.kinghtxg.com/atom.xml',
    headers={
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
    }
)

root = ET.XML(res.content)
dict = dict{}
for node in root:
    print(node.tag,node.text)
```

首先先尝试一下打印看看效果

![image-20211213141704976](https://skystarry-1251157247.cos.ap-chengdu.myqcloud.com/img/image-20211213141704976.png){loading="lazy"}

需要进行一下字符串处理，把tag前面的格式给去掉，然后把结果放入字典中

``` python
from xml.etree import ElementTree as ET
import requests

res = requests.get(
    url='https://www.kinghtxg.com/atom.xml',
    headers={
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
    }
)

root = ET.XML(res.content)
info = {}
for node in root:
    tag = node.tag.replace("{http://www.w3.org/2005/Atom}","")
    info[tag] = node.text
print(info)

'''输出结果
{'title': 'kinghtxg', 'subtitle': '某大厂打杂，又菜又爱玩', 'updated': '2021-12-10T16:20:02+08:00', 'id': 'http://www.kinghtxg.com', 'link': None, 'rights': 'Copyright © 2021, kinghtxg', 'generator': 'Halo', 'entry': '\n                '}
'''
```

# 案例2：天气获取

实现去网上获取指定地区的天气信息，并写入到Excel中。

``` python
import requests
import os
from xml.etree import ElementTree as ET
from openpyxl import load_workbook,workbook

def mk_excel():
    '''
    查询是否拥有天气的excel表
    :return: wb -> 天气.excel文件句柄设置为全局
    '''
    abs = os.path.abspath(__file__)
    path = os.path.dirname(abs)
    global file_path
    file_path = os.path.join(path,'file','天气.xlsx')
    global wb
    if not os.path.exists(file_path):
        # 创建excel并默认创建一个sheet
        wb = workbook.Workbook()
        del wb['Sheet'] # 删除默认sheet
    else:
        wb = load_workbook(file_path)

def city(city):
    # 给城市创建sheet
    sheet = wb.create_sheet(city)
    url = "http://ws.webxml.com.cn//WebServices/WeatherWebService.asmx/getWeatherbyCityName?theCityName={}".format(city)
    res = requests.get(url=url)
    # 1.提取XML格式中的数据
    root = ET.XML(res.content)
    ## for 序号,循环输出的值 in enumerate(被循环的变量,序号初始)
    for lie , child in enumerate(root,1):
        cell = sheet.cell(1,lie)
        cell.value = child.text


while True:
    city_name = input("请输入城市（Q/q退出）：")
    if city_name == "Q" or city_name == "q":
        wb.save(file_path)
        break
    mk_excel()
    city(city_name)
```