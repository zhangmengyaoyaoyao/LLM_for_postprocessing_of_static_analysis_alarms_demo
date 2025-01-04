import pandas as pd
import os

from src.response2excel import process_txt_files, process_txt_files_with_2history, process_txt_files_with_3history, link_excel
from src.judge_consistent import update_consistent_column

link_excel_path = "report/spotbugs_linked"

# 将txt回答转存到excel
# model = "llama3.1-70b-instruct"
model = "glm-4-flash"
tool = "spotbugs"
prompts_techniques = ["zero_shot", "one_shot", "few_shot", "general_info", "expertise", "chain_of_thought", "critique", "self_heuristic"]
projects = ["collections"]
for project in projects:
    for prompts_technique in prompts_techniques:
        print(prompts_technique)
        folder_path = f"response/{model}/{tool}/{prompts_technique}/{project}"  # 替换为你的文件夹路径
        output_excel = f"response/{model}/{tool}/{prompts_technique}_{project}.xlsx"  # 替换为保存Excel的路径
        if prompts_technique == "critique":
            process_txt_files_with_3history(folder_path, output_excel)
        elif prompts_technique == "self_heuristic":
            process_txt_files_with_2history(folder_path, output_excel)
        else:
            process_txt_files(folder_path, output_excel)

        # 将人工标记导入
        link_excel(os.path.join(link_excel_path, f"{project}_linked.csv"), output_excel)

        # 比较一致性
        update_consistent_column(output_excel)