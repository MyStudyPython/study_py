# 处理 Excel文件
import xlrd

# 获取Excel对象
data = xlrd.open_workbook("test.xlsx")
print("该文档一共有%d张表" % data.nsheets)

# 获取表对象
table = data.sheets()[0]
print(
    "第一张表的名称为：{0}\n具有的行数：{1}\n 具有的列数：{2}".format(table.name, table.nrows, table.ncols)
)
for i in range(table.nrows):
    print(table.row(i))
