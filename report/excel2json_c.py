import pandas as pd
import json
import os

def excel_to_json(excel_file, output_dir, columns):
    """
    将 Excel 文件的每一行转换为一个 JSON 文件。
    
    参数:
        excel_file (str): 输入的 Excel 文件路径。
        output_dir (str): 输出 JSON 文件存储目录。
        columns (list): 要保留的列的列表。
    """
    # 检查输出目录是否存在，不存在则创建
    os.makedirs(output_dir, exist_ok=True)

    # 读取 Excel 文件
    try:
        data = pd.read_excel(excel_file, usecols=columns)
    except ValueError as e:
        print(f"错误: 确保 Excel 文件中包含以下列: {columns}. 异常信息: {e}")
        return

    # 遍历每一行，将其转换为 JSON 文件
    index = 1
    for idx, row in data.iterrows():
        row_data = row.to_dict()  # 转为字典
        project = row_data.get("Project", "Unknown").replace(" ", "_")
        filename = f'bug_{index:04d}_{project}.json'
        output_path = os.path.join(output_dir, filename)
        
        with open(output_path, 'w', encoding='utf-8') as json_file:
            json.dump(row_data, json_file, ensure_ascii=False, indent=4)  # 写入 JSON 文件

        index += 1

    print(f"转换完成！JSON 文件已保存到: {output_dir}")

# 使用示例
excel_file = "report/c_raw/c.xlsx"  # 替换为你的 Excel 文件路径
output_dir = "report/c_json"  # 输出 JSON 文件的目录
columns = ["Project", "Tool", "category", "file", "message", "warning_function_name","warning_line", "warning_context"]  # 需要保留的列

excel_to_json(excel_file, output_dir, columns)
