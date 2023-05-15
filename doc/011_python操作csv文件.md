# csv文件

**逗号分隔值**（Comma-Separated
Values，**CSV**，有时也称为**字符分隔值**，因为分隔字符也可以不是逗号），其文件以纯文本形式存储表格数据（数字和文本）。纯文本意味着该文件是一个[字符](https://baike.baidu.com/item/%E5%AD%97%E7%AC%A6/4768913){target="_blank"
rel="noopener"}序列，不含必须像[二进制数字](https://baike.baidu.com/item/%E4%BA%8C%E8%BF%9B%E5%88%B6%E6%95%B0%E5%AD%97/5920908){target="_blank"
rel="noopener"}那样被解读的数据。CSV文件由任意数目的记录组成，记录间以某种换行符分隔；每条记录由[字段](https://baike.baidu.com/item/%E5%AD%97%E6%AE%B5/2885972){target="_blank"
rel="noopener"}组成，字段间的分隔符是其它字符或字符串，最常见的是逗号或[制表符](https://baike.baidu.com/item/%E5%88%B6%E8%A1%A8%E7%AC%A6/7337607){target="_blank"
rel="noopener"}。通常，所有记录都有完全相同的字段序列。通常都是[纯文本文件](https://baike.baidu.com/item/%E7%BA%AF%E6%96%87%E6%9C%AC%E6%96%87%E4%BB%B6/4865229){target="_blank"
rel="noopener"}。建议使用WORDPAD或是记事本来开启，再则先另存新档后用EXCEL开启，也是方法之一

CSV文件格式的通用标准并不存在，但是在RFC
4180中有基础性的描述。使用的字符编码同样没有被指定，但是bit[ASCII](https://baike.baidu.com/item/ASCII){target="_blank"
rel="noopener"}是最基本的通用编码

# 文件操作方式

对于这种格式的数据，我们需要利用open函数来读取文件并根据逗号分隔的特点来进行处理

``` csv
股票代码,股票名称,当前价,涨跌额,涨跌幅,年初至今
SH601778,N晶科,6.29,+1.92,-43.94%,+43.94%
SH688566,吉贝尔,52.66,+6.96,+15.23%,+122.29%
...
```

# 案例1

下载文档中的所有图片且以用户名为图片名称存储

``` python
ID,用户名,头像
26044585,Hush,https://hbimg.huabanimg.com/51d46dc32abe7ac7f83b94c67bb88cacc46869954f478-aP4Q3V
19318369,柒十一,https://hbimg.huabanimg.com/703fdb063bdc37b11033ef794f9b3a7adfa01fd21a6d1-wTFbnO
15529690,Law344,https://hbimg.huabanimg.com/b438d8c61ed2abf50ca94e00f257ca7a223e3b364b471-xrzoQd
18311394,Jennah·,https://hbimg.huabanimg.com/4edba1ed6a71797f52355aa1de5af961b85bf824cb71-px1nZz
18009711,可洛爱画画,https://hbimg.huabanimg.com/03331ef39b5c7687f5cc47dbcbafd974403c962ae88ce-Co8AUI
30574436,花姑凉~,https://hbimg.huabanimg.com/2f5b657edb9497ff8c41132e18000edb082d158c2404-8rYHbw
17740339,小巫師,https://hbimg.huabanimg.com/dbc6fd49f1915545cc42c1a1492a418dbaebd2c21bb9-9aDqgl
18741964,桐末tonmo,https://hbimg.huabanimg.com/b60cee303f62aaa592292f45a1ed8d5be9873b2ed5c-gAJehO
30535005,TANGZHIQI,https://hbimg.huabanimg.com/bbd08ee168d54665bf9b07899a5c4a4d6bc1eb8af77a4-8Gz3K1
31078743,你的老杨,https://hbimg.huabanimg.com/c46fbc3c9a01db37b8e786cbd7174bbd475e4cda220f4-F1u7MX
25519376,尺尺寸,https://hbimg.huabanimg.com/ee29ee198efb98f970e3dc2b24c40d89bfb6f911126b6-KGvKes
21113978,C-CLong,https://hbimg.huabanimg.com/7fa6b2a0d570e67246b34840a87d57c16a875dba9100-SXsSeY
24674102,szaa,https://hbimg.huabanimg.com/0716687b0df93e8c3a8e0925b6d2e4135449cd27597c4-gWdv24
30508507,爱起床的小灰灰,https://hbimg.huabanimg.com/4eafdbfa21b2f300a7becd8863f948e5e92ef789b5a5-1ozTKq
12593664,yokozen,https://hbimg.huabanimg.com/cd07bbaf052b752ed5c287602404ea719d7dd8161321b-cJtHss
16899164,一阵疯,https://hbimg.huabanimg.com/0940b557b28892658c3bcaf52f5ba8dc8402100e130b2-G966Uz
847937,卩丬My㊊伴er彎,https://hbimg.huabanimg.com/e2d6bb5bc8498c6f607492a8f96164aa2366b104e7a-kWaH68
31010628,慢慢即漫漫,https://hbimg.huabanimg.com/c4fb6718907a22f202e8dd14d52f0c369685e59cfea7-82FdsK
13438168,海贼玩跑跑,https://hbimg.huabanimg.com/1edae3ce6fe0f6e95b67b4f8b57c4cebf19c501b397e-BXwiW6
28593155,源稚生,https://hbimg.huabanimg.com/626cfd89ca4c10e6f875f3dfe1005331e4c0fd7fd429-9SeJeQ
28201821,合伙哼哼,https://hbimg.huabanimg.com/f59d4780531aa1892b80e0ec94d4ec78dcba08ff18c416-769X6a
28255146,漫步AAA,https://hbimg.huabanimg.com/3c034c520594e38353a039d7e7a5fd5e74fb53eb1086-KnpLaL
30537613,配䦹,https://hbimg.huabanimg.com/efd81d22c1b1a2de77a0e0d8e853282b83b6bbc590fd-y3d4GJ
22665880,日后必火,https://hbimg.huabanimg.com/69f0f959979a4fada9e9e55f565989544be88164d2b-INWbaF
16748980,keer521521,https://hbimg.huabanimg.com/654953460733026a7ef6e101404055627ad51784a95c-B6OFs4
30536510,“西辞”,https://hbimg.huabanimg.com/61cfffca6b2507bf51a507e8319d68a8b8c3a96968f-6IvMSk
30986577,艺成背锅王,https://hbimg.huabanimg.com/c381ecc43d6c69758a86a30ebf72976906ae6c53291f9-9zroHF
26409800,CsysADk7,https://hbimg.huabanimg.com/bf1d22092c2070d68ade012c588f2e410caaab1f58051-ahlgLm
30469116,18啊全阿,https://hbimg.huabanimg.com/654953460733026a7ef6e101404055627ad51784a95c-B6OFs4
17473505,椿の花,https://hbimg.huabanimg.com/0e38d810e5a24f91ebb251fd3aaaed8bb37655b14844c-pgNJBP
19165177,っ思忆゜♪,https://hbimg.huabanimg.com/4815ea0e4905d0f3bb82a654b481811dadbfe5ce2673-vMVr0B
16059616,格林熊丶,https://hbimg.huabanimg.com/8760a2b08d87e6ed4b7a9715b1a668176dbf84fec5b-jx14tZ
30734152,sCWVkJDG,https://hbimg.huabanimg.com/f31a5305d1b8717bbfb897723f267d316e58e7b7dc40-GD3e22
24019677,虚无本心,https://hbimg.huabanimg.com/6fdfa9834abe362e978b517275b06e7f0d5926aa650-N1xCXE
16670283,Y-雨后天空,https://hbimg.huabanimg.com/a3bbb0045b536fc27a6d2effa64a0d43f9f5193c177f-I2vHaI
21512483,汤姆2,https://hbimg.huabanimg.com/98cc50a61a7cc9b49a8af754ffb26bd15764a82f1133-AkiU7D
16441049,笑潇啸逍小鱼,https://hbimg.huabanimg.com/ae8a70cd85aff3a8587ff6578d5cf7620f3691df13e46-lmrIi9
24795603,⁢⁢⁢⁢⁢v,https://hbimg.huabanimg.com/a7183cc3a933aa129d7b3230bf1378fd8f5857846cc5-3tDtx3
29819152,妮玛士珍多,https://hbimg.huabanimg.com/ca4ecb573bf1ff0415c7a873d64470dedc465ea1213c6-RAkArS
19101282,陈勇敢❤,https://hbimg.huabanimg.com/ab6d04ebaff3176e3570139a65155856871241b58bc6-Qklj2E
28337572,爱意随风散,https://hbimg.huabanimg.com/117ad8b6eeda57a562ac6ab2861111a793ca3d1d5543-SjWlk2
17342758,幸运instant,https://hbimg.huabanimg.com/72b5f9042ec297ae57b83431123bc1c066cca90fa23-3MoJNj
18483372,Beau染,https://hbimg.huabanimg.com/077115cb622b1ff3907ec6932e1b575393d5aae720487-d1cdT9
22127102,栽花的小蜻蜓,https://hbimg.huabanimg.com/6c3cbf9f27e17898083186fc51985e43269018cc1e1df-QfOIBG
13802024,LoveHsu,https://hbimg.huabanimg.com/f720a15f8b49b86a7c1ee4951263a8dbecfe3e43d2d-GPEauV
22558931,白驹过隙丶梨花泪う,https://hbimg.huabanimg.com/e49e1341dfe5144da5c71bd15f1052ef07ba7a0e1296b-jfyfDJ
11762339,cojoy,https://hbimg.huabanimg.com/5b27f876d5d391e7c4889bc5e8ba214419eb72b56822-83gYmB
30711623,雪碧学长呀,https://hbimg.huabanimg.com/2c288a1535048b05537ba523b3fc9eacc1e81273212d1-nr8M4t
18906718,西霸王,https://hbimg.huabanimg.com/7b02ad5e01bd8c0a29817e362814666a7800831c154a6-AvBDaG
31037856,邵阳的小哥哥,https://hbimg.huabanimg.com/654953460733026a7ef6e101404055627ad51784a95c-B6OFs4
26830711,稳健谭,https://hbimg.huabanimg.com/51547ade3f0aef134e8d268cfd4ad61110925aefec8a-NKPEYX
```

代码演示：

``` python
import requests
import os
with open('mv.csv',mode='rt',encoding='utf-8') as mv:
    mv.readline() # 跳过第一行
    # 读取 mv.csv
    for line in mv:
        user_id,file_name,file_url = line.strip().split(",") # 需要注意的是，每一行结尾有\n
        # 从网络中获取图片内容
        res = requests.get(
            url = file_url,
            headers={
                "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36"
            }
        )
        # 写文件 -> 将文件写在images文件夹下
        ## 检查images目录是否存在，不存在则创建
        if not os.path.exists("images"):
            ## 创建images目录
            os.makedirs("images")
        ## 写入文件
        with open("images/{}.png".format(file_name),mode='wb') as png_file:
            png_file.write(res.content)
            png_file.close()
```

![image-20211210021931141](https://skystarry-1251157247.cos.ap-chengdu.myqcloud.com/img/image-20211210021931141.png){loading="lazy"}

# 案例2

基于csv格式实现 用户的注册 & 登录认证。详细需求如下：

-   用户注册时，新注册用户要写入文件csv文件中，输入Q或q则退出。
-   用户登录时，逐行读取csv文件中的用户信息并进行校验。
-   提示：文件路径须使用os模块构造的绝对路径的方式。

``` python
'''
基于csv格式实现 用户的注册 & 登录认证。详细需求如下：

- 用户注册时，新注册用户要写入文件csv文件中，输入Q或q则退出。
- 用户登录时，逐行读取csv文件中的用户信息并进行校验。
- 提示：文件路径须使用os模块构造的绝对路径的方式。
'''
import hashlib
import os

def path():
    abs = os.path.abspath(__file__)
    path = os.path.dirname(abs)
    file_path = os.path.join(path, 'file', 'user.csv')
    # 判断文件是否存在，不存在则创建
    if not os.path.exists(file_path):
        mk_file = open(file_path,mode='xt',encoding='utf-8')
        mk_file.close()
    return file_path

def user_rg():
    '''
    注册模块，将账号和md5加密后的密码放入file/user.csv文件
    input: None
    return: None
    '''
    while True:
        username = input('请输入用户名(Q退出):').strip()
        if username == 'Q' or username == 'q':
            break
        passwd = input('请输入密码:')
        passwd = hashlib.md5(passwd.encode('utf-8')).hexdigest() # md5加密
        user = '{},{}\n'.format(username,passwd)
        file_path = path()
        with open(file_path,mode='at',encoding='utf-8') as user_file:
            user_file.write(user)

def user_login(username,password):
    username = username
    passwd = password
    passwd = hashlib.md5(passwd.encode('utf-8')).hexdigest()  # md5加密

    file_path = path()
    with open(file_path,mode='rt',encoding='utf-8') as user_file:
        for user in user_file:
            user_name,password = user.strip().split(",")
            if username == user_name and passwd == password:
                print("登录成功")
                break
        else:
            print("登录失败")

while True:
    print("欢迎来到用户系统，请登录您的账户")
    username = input("请输入您的账户名(输入Z注册用户)：")
    if username.upper() == "Z":
        user_rg()
        continue
    password = input("请输入您的密码：")
    user_login(username,password)
```