import csv
import json
import os

projects = ["bcel", "codec", "collections", "configuration", "dbcp", "digester", "fileupload", "mavendp", "net", "pool"]
columns_to_exclude = ['final_label', 'no']  # 需要剔除的人工标记
for project in projects:
    # 设定输入CSV文件路径和输出文件夹路径
    input_csv = f'report/spotbugs_linked/{project}_linked.csv'
    output_folder = f'report/spotbugs/{project}/'

    # 创建输出文件夹，如果文件夹不存在
    os.makedirs(output_folder, exist_ok=True)

    # 读取CSV文件并逐行处理
    with open(input_csv, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        index = 1  # 用于文件命名的索引
        for row in csv_reader:
            # 移除指定列
            for col in columns_to_exclude:
                row.pop(col, None)  # 如果列存在则删除，不存在则忽略
            # 将索引格式化为四位字符串
            filename = f'bug_{index:04d}_{project}.json'
            
            # 设置JSON文件路径
            output_path = os.path.join(output_folder, filename)
            
            # 将行数据写入JSON文件，确保各行分开
            with open(output_path, mode='w', encoding='utf-8') as json_file:
                json.dump(row, json_file, ensure_ascii=False, indent=4)
            
            index += 1