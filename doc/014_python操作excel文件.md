# excel

这个就不需要过多介绍了，大家都常用

python内部并没有提高对excel文件操作的函数库，需要我们引入第三方模块

``` python
pip3 install openpyxl
```

此模块中集成了Python操作Excel的相关功能，接下来我们就需要去学习该模块提供的相关功能即可

# 读Excel

## 读取sheet

``` python
from openpyxl import load_workbook

# 倒入Excel
wordbook = load_workbook("p2.xlsx")

# sheet相关操作 -> 很多时候excel不止一个sheet，所以需要先选中sheet
## 1.获取文件中对所有sheet名称
print(wordbook.sheetnames) # ['数据导出', '用户列表', 'Sheet1', 'Sheet2']
## 2.选择sheet
### 通过名称
sheet_1 = wordbook['数据导出']
cell = sheet_1.cell(1,1) # 读取'数据导出'sheet的第一行第一列单元格
print(cell.value) # 打印数据 开始
### 基于索引位置
sheet_2 = wordbook.worksheets[0] # 取第0个索引第sheet
cell = sheet_2.cell(2,1)
print(cell.value) # 287
### 循环所有的sheet
#### 方案1 -> 循环得到所有sheet名字取值
for name in wordbook.sheetnames:
    sheet = wordbook[name]
    cell = sheet.cell(1,2)
    print(cell.value)
#### 方案2 -> 直接循环所有的sheet取值
for name in wordbook.worksheets:
    cell = name.cell(1,2)
    print(cell.value)
#### 方案3 方案2简写版
for name in wordbook:
    cell = name.cell(1,2)
    print(cell.value)
```

## 获取单元格中的数据

### 获取某一个位置的单元格

``` python
from openpyxl import load_workbook

wb = load_workbook('p2.xlsx')
sheet = wb['数据导出']
# sheet = wb.worksheets[0]

# 1.cell读取单元格 -> 上文提到过
## 值得注意的是，位置是从1开始的，而不像序列是从0开始
cell = sheet.cell(3,4) # 第三行第四列
print(cell.value) # 值
print(cell.style) # 样式
print(cell.font) # 字体 -> 其实是个对象，下文回介绍
print(cell.alignment) # 排列情况

# 2.直接获取单元格
c1 = sheet['D2'] # 直接输入单元格序号
print(c1.value)
```

### 获取某行某列的单元格信息

``` python
from openpyxl import load_workbook

wb = load_workbook('p2.xlsx')
sheet = wb.worksheets[0]

# 获取行所有的单元格
c1 = sheet[1]
print(c1)
# 获取列所有的单元格
c2 = sheet['A']
print(c2)

# 打印所有的单元格内容 -> for循环
for cell in c1:
    print(cell.value)
```

### 获取整个表格全部单元格信息

``` python
from openpyxl import load_workbook

wb = load_workbook('p2.xlsx')
sheet = wb.worksheets[0]

# 获取所有的单元格信息需要用 sheet.rows
## 循环打印每一排的信息
for row in sheet.rows:
    # print(row.value) # 获取所有的数据
    # 可以获取所有列，不过这里由于是使用转换成元组的模式进行获取，所以需要遵循序列从0开始
    print(row[0].value) # 获取第1列的数据
```

### 获取合并单元格信息

![image-20211214163940334](https://skystarry-1251157247.cos.ap-chengdu.myqcloud.com/img/image-20211214163940334.png){loading="lazy"}

以上图单元格为例，获取用户信息这个合并了A1和B1的单元格

``` python
from openpyxl import load_workbook

wb = load_workbook('p2.xlsx')
sheet = wb.worksheets[2]
# 获取合并单元格
c1 = sheet.cell(1,1)
print(c1) # <Cell 'Sheet1'.A1>
print(c1.value) # 用户信息
c2 = sheet.cell(1,2)
print(c2) # <MergedCell 'Sheet1'.B1>
print(c2.value) # None
```

合并单元格其实是将值存放于最左上的那个各自里，我们打印信息可以看到Cell和MergedCell，分别值得就是单元格和合并单元格，而值则是存放于单元格中，合并单元格为None

垂直方向合并也相同

``` python
from openpyxl import load_workbook

wb = load_workbook('p2.xlsx')
sheet = wb.worksheets[2]
# 获取合并单元格
c1 = sheet.cell(3,1)
print(c1) # <Cell 'Sheet1'.A3>
print(c1.value) # 我害怕
c2 = sheet.cell(4,1)
print(c2) # <MergedCell 'Sheet1'.A4>
print(c2.value) # None
```

# 写内容

## 原Excel中写内容和新Excel中写内容

### 原excel中写内容

``` python
from openpyxl import load_workbook
wb = load_workbook('p2.xlsx')
sheet = wb['数据导出']

# 找到单元格，并修改内容
cell = sheet['c2']
cell.value = '课程2'
# 保存文件
wb.save('p2.xlsx')
```

### 新excel中写内容

``` python
# 写文件需要导入workbook
from openpyxl import workbook

# 创建excel且默认创建一个sheet(默认取名为sheet)
wb = workbook.Workbook()
sheet = wb.worksheets[0]
# 写入数据
cell = sheet.cell(1,1)
cell.value = "新的excel"
# 将文件存储到硬盘中
wb.save("p3.xlsx")
```

## 对Sheet操作

无论是读取、写入新文件还是旧文件命令都相同，操作对于后续的sheet和cell都相同

``` python
from openpyxl import workbook

# 1.创建文件的同时会创建一个默认名为sheet的sheet
wb = workbook.Workbook()

# 2.修改sheet的名称
sheet = wb.worksheets[0]
sheet.title = "数据集"
wb.save("xlsx/p5.xlsx")

# 3.创建sheet：工作计划,并把索引设置为0
sheet = wb.create_sheet("工作计划",0)
wb.save("xlsx/p5.xlsx")

# 4.将sheet数据集的名称改为红色
sheet = wb.worksheets[1] # 工作计划索引为0了，数据集就为1了
## 颜色参照RGB颜色对照表 -> 需要将RGB数字转为16进制
sheet.sheet_properties.tabColor = "1072BA" # 将数据集的sheet名称框改为红色
wb.save("xlsx/p5.xlsx")

# 5.设置打开文档时默认的sheet
wb.active = 1 # 默认文档设置为数据集
wb.save("xlsx/p5.xlsx")

# 6.拷贝sheet
new_sheet = wb.copy_worksheet(wb['工作计划'])
new_sheet.title = "计划2.0"
wb.save("xlsx/p6.xlsx")

# 7.删除sheet
del wb['工作计划']
wb.save('xlsx/p6.xlsx')
```

## 对单元格操作

``` python
from openpyxl import load_workbook
# 操作单元格需要的模块
from openpyxl.styles import Alignment, Border, Side, Font, PatternFill, GradientFill
wb = load_workbook('xlsx/p2.xlsx')
sheet = wb.worksheets[0]

# 1.获取单元格并修改值
## 方式1
cell = sheet.cell(1,1)
cell.value = '学号'
wb.save('xlsx/p7.xlsx')
## 方式2
sheet['c2'] = '最后一章'
wb.save('xlsx/p7.xlsx')

# 2.获取某些单元格并修改值
cell_list = sheet['b2':'c3']
for row in cell_list:
    for cell in row:
        cell.value = "测试"
wb.save('xlsx/p7.xlsx')
'''注意
sheet['b2':'c3'] 取值结果是
(
    (B2,B3),
    (C2,C3),
)
所以使用嵌套循环进行打印
'''

# 3.表格对齐方式
cell = sheet.cell(1,1)
## 这里需要倒入模块 -> Alignment
cell.alignment = Alignment(horizontal='center', vertical='distributed', text_rotation=45, wrap_text=True)
wb.save('xlsx/p7.xlsx')
'''注意
# alignment(对齐方式，下方为他的参数)
# horizontal -> 水平方向对齐方式："general", "left", "center", "right", "fill", "justify", "centerContinuous", "distributed"
# vertical -> 垂直方向对齐方式："top", "center", "bottom", "justify", "distributed"
# text_rotation ->旋转角度。
# wrap_text -> 是否自动换行。
'''

# 4.表格边框
cell = sheet.cell(1,2)
## 这里需要倒入参数Border和side
cell.border = Border(
   # top、bottom、left、right指的是上下左右的边框
   ## style是边框的样式 color是颜色
    top=Side(style="thin", color="FFB6C1"),
    bottom=Side(style="dashed", color="FFB6C1"),
    left=Side(style="dashed", color="FFB6C1"),
    right=Side(style="dashed", color="9932CC"),
    # 对角线
    diagonal=Side(style="dashed", color="483D8B"),
    diagonalUp=True,  # 左下 ~ 右上
    diagonalDown=True  # 左上 ~ 右下
)
wb.save('xlsx/p7.xlsx')

# 5.字体
cell = sheet.cell(1,3)
## 这里需要倒入参数Font
cell.font = Font(name="微软雅黑", size=45, color="ff0000", underline="single")
wb.save('xlsx/p7.xlsx')

# 6.背景颜色
cell = sheet.cell(1,4)
## 这里需要倒入参数PatternFill
cell.fill = PatternFill("solid", fgColor="99ccff")
wb.save('xlsx/p7.xlsx')

# 7.渐变背景色
cell = sheet.cell(1,5)
   # stop = ('左边颜色','中间颜色','右边颜色')
cell.fill = GradientFill("linear", stop=("FFFFFF", "99ccff", "000000"))
wb.save('xlsx/p7.xlsx')

# 8.设置单元格高宽 -> 表格也不允许设置单个
sheet.row_dimensions[1].height = 50 # 第一行高50
sheet.column_dimensions["E"].width = 100 # 第E列宽100
wb.save('xlsx/p7.xlsx')

# 9.合并单元格
# 方案1
##  start_row、start_column开始位置，end_row、end_column结束位置
sheet.merge_cells(start_row=14, start_column=3, end_row=18, end_column=8) # 其实合并的位置是第14行3列到第18行8列
# 方案2
sheet.merge_cells("B1:D7")
wb.save('xlsx/p7.xlsx')
# 10.解除合并单元格
sheet.unmerge_cells("B1:D7")
wb.save('xlsx/p7.xlsx')

# 11.在excel表中写入公式 -> 就像写入数据一样即可
sheet = wb.worksheets[3]
sheet["D1"] = "合计"
sheet["D2"] = "=B2*C2"
## 也可以写入excel的公式
sheet = wb.worksheets[3]
sheet["D3"] = "=SUM(B3,C3)"
wb.save('xlsx/p7.xlsx')

# 12.删除表格 -> 数据会向前补齐
sheet = wb.worksheets[0]
sheet.delete_rows(idx=10, amount=20) # 删除从第一行开始往后数第20行
sheet.delete_cols(idx=5, amount=3) # 删除从第一列开始往后的三列
wb.save('xlsx/p7.xlsx')

# 13.插入表格
sheet.insert_rows(idx=10, amount=20)
sheet.insert_cols(idx=5, amount=3)
wb.save('xlsx/p7.xlsx')

# 14.循环写内容
sheet = wb["Sheet2"]
## 方案1：使用sheet选中区域A1:C2获取对应元组，使用循环
cell_range = sheet['A1:C2']
for row in cell_range:
    for cell in row:
        cell.value = "xx"
## 使用iter_rows直接获取对应区域
for row in sheet.iter_rows(min_row=5, min_col=1, max_col=7, max_row=10):
    for cell in row:
        cell.value = "oo"
wb.save('xlsx/p7.xlsx')

# 15.移动表格位置
sheet.move_range("B1:D3",cols=10, translate=True) # 自动翻译公式
wb.save('xlsx/p7.xlsx')
'''自动翻译公式含义解释：
例如 D2=(sum(B2,C2)) 如果D2移动到D3自动翻译就会是=(sum(B3,C3))
'''

# 16.打印区域
## 打印时会被打印的区域
sheet.print_area = "A1:D200"
wb.save('xlsx/p7.xlsx')

# 17.打印时，每个页面的固定表头
## 打印时，每一页都会出现的固定表格内容，通常表头需要设置
sheet.print_title_cols = "A:D"
sheet.print_title_rows = "1:3"
wb.save('xlsx/p7.xlsx')
```

# 案例

读取ini文件内容，按照规则写入到Excel中。

-   ini文件内容如下：

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

-   读取ini格式的文件，并创建一个excel文件，且为每个节点创建一个sheet，然后将节点下的键值写入到excel中，按照如下格式。

    ![image-20201218204922898](https://skystarry-1251157247.cos.ap-chengdu.myqcloud.com/img/image-20201218204922898.png){style="zoom: 33%"}

    -   首行，字体白色 & 单元格背景色蓝色。
    -   内容均居中。
    -   边框

    ``` python
    import configparser,os
    from openpyxl import load_workbook,workbook
    from openpyxl.styles import Alignment,PatternFill,Font,Side,Border

    # 获取文件路径
    abs_path = os.path.abspath(__file__)
    dir_path = os.path.dirname(abs_path)
    ## ini文件路径
    ini_path = os.path.join(dir_path , "file", "配置.ini")
    ## excel文件路径
    excel_path = os.path.join(dir_path , "file", "配置.xlsx")

    # 检查excel是否存在，不存在则创建
    if not os.path.exists(excel_path):
        wb = workbook.Workbook()
        del wb['Sheet']
    else:
        wb = load_workbook(excel_path)

    # 读取ini文件
    # 获取ini文件的文件句柄
    config = configparser.ConfigParser()
    config.read(ini_path,encoding='utf-8')

    ## 获取所有的节点名称
    res = config.sections()
    Node_name = res
    print(Node_name)

    # 表格的边框和居中
    # style = 线的风格 color = 线的颜色
    side = Side(style='thin',color='000000')
    # top 上 bottom 下 left 左 right 右
    border = Border(top=side,bottom=side,left=side,right=side)
    # horizontal = 水平 vertical = 垂直
    align = Alignment(horizontal='center',vertical='center')

    # 创建所有节点的sheet并且创建每一个的表头
    for name in Node_name:
        sheet = wb.create_sheet(name)
        # 创建表头
        meter_header_words = {'A1':'键','B1':'值'}
        for key,text in meter_header_words.items():
            # 设置值
            cell = sheet[key]
            cell.value = text
            # 设置居中
            cell.alignment = align # 直接引用之前的设置
            # 设置背景色
            cell.fill = PatternFill("solid",fgColor='6495ED')
            # 设置字体颜色
            cell.font = Font(name = "微软雅黑",color="ffffff")
            # 设置边框
            cell.border = border

            # 读取节点中的键值
            row_index = 2 # 起始行序号
            # name 是上层循环中输出的节点名字
            for group in config.items(name):
                # 此循环 group 将会得到元祖 => ('datadir', '/var/lib/mysql')
                for col,text in enumerate(group,1):
                    cell = sheet.cell(row_index,col)
                    cell.value = text # 设置值
                    cell.border = border # 设置边框
                    cell.alignment = align # 设置居中
                # 别忘了row_index的行要+1
                row_index += 1
    wb.save(excel_path)
    ```