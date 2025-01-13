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
    # 将数据保存到Excel文件
    df = pd.DataFrame(data)
    df.to_excel(output_excel, index=False)
    print(f"数据已保存到 {output_excel}")


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



def link_excel(file1, file2):
    """
    将 file1 中的所有列粘贴到 file2 中的最后，并保存为新的 Excel 文件。
    """
    # 根据文件扩展名判断读取方式
    if file1.endswith('.csv'):
        df1 = pd.read_csv(file1)
    elif file1.endswith('.xlsx'):
        df1 = pd.read_excel(file1)
    else:
        raise ValueError("file1 必须是 CSV 或 Excel 文件")
    if file2.endswith('.csv'):
        df2 = pd.read_csv(file2)
    elif file2.endswith('.xlsx'):
        df2 = pd.read_excel(file2)
    else:
        raise ValueError("file2 必须是 CSV 或 Excel 文件")

    # 按照 'no' 列升序排序 file1
    df1_sorted = df1.sort_values(by='no', ascending=True)

    # 按照 'File Name' 列升序排序 file2
    df2_sorted = df2.sort_values(by='File Name', ascending=True)

    # 将 file1 中的所有列添加到 file2 中的最后
    # merged_df = pd.concat([df2_sorted, df1_sorted], axis=1)


    # 一行一行地粘贴 file1 的数据到 file2
    for index, row in df1_sorted.iterrows():
        # 将每一行添加到 file2 的最后
        df2_sorted.loc[index, df1_sorted.columns] = row

    # 保存到 file2 中
    df2_sorted.to_excel(file2, index=False)
