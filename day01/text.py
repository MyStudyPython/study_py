import csv
import json
import os

# 读取CSV文件
with open("excel_file.csv", encoding="utf-8") as csv_file:
    csv_data = csv.DictReader(csv_file)

# 将CSV数据转换成JSON对象
json_data = []
for row in csv_data:
    json_data.append(row)

# 将JSON数据写入文件
with open("output_file.json", "w", encoding="utf-8") as json_file:
    json.dump(json_data, json_file, ensure_ascii=False)
