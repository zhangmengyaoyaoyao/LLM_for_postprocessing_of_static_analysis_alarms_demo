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


def process_txt_files_with_3history(folder_path, output_excel):
    data = []  # 用于存储文件名、完整内容和提取的信息

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt") and ("_history" not in filename):  # 只处理 .txt 文件
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
                try:
                    history_file_path=os.path.join(folder_path, file_name_without_ext+"_history.txt")
                    with open(history_file_path, "r", encoding="utf-8") as history_file:
                        history_lines = history_file.readlines()
                        history_full_content = "".join(history_lines)
                        # 分割文件内容，按三个换行符分成三部分
                        history_parts = history_full_content.split("\n\n\n")
                        response1 = history_parts[0].strip() if len(history_parts) > 0 else ""
                        response2 = history_parts[1].strip() if len(history_parts) > 1 else ""
                        response3 = history_parts[2].strip() if len(history_parts) > 2 else ""
                        # 将这三部分数据保存到没有 '_history' 的文件对应的 Excel 行
                        data.append({
                            "File Name": file_name_without_ext,
                            "Response 1": response1,
                            "Response 2": response2,
                            "Response 3": response3,
                            "Content": full_content,
                            "Status": status
                        })
                except FileNotFoundError:
                    print("FileNotFoundError:" + file_name_without_ext+"_history.txt")
                    response1 = ""
                    response2 = ""
                    response3 = ""
                    data.append({
                        "File Name": file_name_without_ext,
                        "Response 1": response1,
                        "Response 2": response2,
                        "Response 3": response3,
                        "Content": full_content,
                        "Status": status
                    })



def process_txt_files_with_2history(folder_path, output_excel):
    data = []  # 用于存储文件名、完整内容和提取的信息

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt") and ("_history" not in filename):  # 只处理 .txt 文件
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
                try:
                    history_file_path=os.path.join(folder_path, file_name_without_ext+"_history.txt")
                    with open(history_file_path, "r", encoding="utf-8") as history_file:
                        history_lines = history_file.readlines()
                        history_full_content = "".join(history_lines)
                        # 分割文件内容，按三个换行符分成2部分
                        history_parts = history_full_content.split("\n\n\n")
                        response1 = history_parts[0].strip() if len(history_parts) > 0 else ""
                        response2 = history_parts[1].strip() if len(history_parts) > 1 else ""
                        # 将这2部分数据保存到没有 '_history' 的文件对应的 Excel 行
                        data.append({
                            "File Name": file_name_without_ext,
                            "Response 1": response1,
                            "Response 2": response2,
                            "Content": full_content,
                            "Status": status
                        })
                except FileNotFoundError:
                    print("FileNotFoundError:" + file_name_without_ext+"_history.txt")
                    response1 = ""
                    response2 = ""
                    data.append({
                        "File Name": file_name_without_ext,
                        "Response 1": response1,
                        "Response 2": response2,
                        "Content": full_content,
                        "Status": status
                    })



    
    # 将数据保存到Excel文件
    df = pd.DataFrame(data)
    df.to_excel(output_excel, index=False)
    print(f"数据已保存到 {output_excel}")




# 使用示例
# prompts_techniques = ["zero_shot", "one_shot", "few_shot", "general_info", "expertise", "chain_of_thought"]

# for prompts_technique in prompts_techniques:
#     print(prompts_technique)
#     folder_path = f"response/llama3.1-70b-instruct/spotbugs/{prompts_technique}/bcel"  # 替换为你的文件夹路径
#     output_excel = f"response/llama3.1-70b-instruct/spotbugs/{prompts_technique}_bcel.xlsx"  # 替换为保存Excel的路径
#     process_txt_files(folder_path, output_excel)

prompts_technique = "self_heuristic"
folder_path = f"response/llama3.1-70b-instruct/spotbugs/{prompts_technique}/bcel"  # 替换为你的文件夹路径
output_excel = f"response/llama3.1-70b-instruct/spotbugs/{prompts_technique}_bcel.xlsx"  # 替换为保存Excel的路径
if prompts_technique == "critique":
    process_txt_files_with_3history(folder_path, output_excel)
elif prompts_technique == "self_heuristic":
    process_txt_files_with_2history(folder_path, output_excel)

