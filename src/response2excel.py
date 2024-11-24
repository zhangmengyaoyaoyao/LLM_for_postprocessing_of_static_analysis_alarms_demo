import os
import re
import pandas as pd

def process_txt_files(folder_path, output_excel):
    data = []  # 用于存储文件名、完整内容和提取的信息

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):  # 只处理 .txt 文件
            file_path = os.path.join(folder_path, filename)
            
            # 打开文件并读取内容
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
                full_content = "".join(lines).strip()  # 获取完整内容
                status = "error"  # 初始化状态为 'error'
                
                # 先匹配最后一行
                if lines:  # 确保文件不为空
                    last_line = lines[-1].strip()
                    match = re.search(r"@@ (.*?) @@", last_line)
                    if match:
                        status = match.group(1)
                    else:
                        # 如果最后一行无匹配，再匹配第一行
                        first_line = lines[0].strip()
                        match = re.search(r"@@ (.*?) @@", first_line)
                        if match:
                            status = match.group(1)
                
                # 提取文件名去除扩展名
                file_name_without_ext = os.path.splitext(filename)[0]
                # 将文件名、完整内容和状态加入数据
                data.append({
                    "File Name": file_name_without_ext,
                    "Content": full_content,
                    "Status": status
                })
    
    # 将数据保存到Excel文件
    df = pd.DataFrame(data)
    df.to_excel(output_excel, index=False)
    print(f"数据已保存到 {output_excel}")

# 使用示例
folder_path = "response/llama3-70b-instruct/spotbugs/expertise/bcel"  # 替换为你的文件夹路径
output_excel = "response/llama3-70b-instruct/spotbugs/expertise_bcel.xlsx"  # 替换为保存Excel的路径
process_txt_files(folder_path, output_excel)
