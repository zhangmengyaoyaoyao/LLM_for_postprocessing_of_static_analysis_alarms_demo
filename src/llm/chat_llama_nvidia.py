# from openai import OpenAI
import json
import os
import sys
import time
import glob
from . import openai_client


# 获取项目根目录
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)
import construct_prompts as Constructor

# your api key
key = "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"
url = "https://integrate.api.nvidia.com/v1"
model_fullname="meta/llama-3.1-70b-instruct"
model = "llama3.1-70b-instruct"
# model_fullname="meta/llama-3.1-405b-instruct"
# model = "llama3.1-405b-instruct"

def process_spotbugs_project_files(key, url, model, tool, prompts_technique, project_name, project_path, model_fullname=model):
    # 获取该项目下的所有 JSON 文件路径
    json_files = sorted(glob.glob(os.path.join(project_path, "*.json")))

    if not json_files:
        print(f"No JSON files found for project {project_name} in {project_path}.")
        return
    
    # 存储输出的路径
    if project_name == "unknown":
        constructor = Constructor.C_Constructor()
        output_dir = os.path.join("response", model, "C_project", prompts_technique)
    else:
        constructor = Constructor.Java_Constructor()
        output_dir = os.path.join("response", model, tool, prompts_technique, project_name)
    os.makedirs(output_dir, exist_ok=True)

    #temp
    if prompts_technique == "self_heuristic":
        json_files = json_files[1810:]

    # 依次处理每个 JSON 文件
    for i, json_file in enumerate(json_files):
        print(f"Processing file: {json_file}")
        with open(json_file, 'r') as f:
            data = json.load(f)

        # 转换 JSON 为字符串
        json_content = json.dumps(data, indent=2)
        
        # 设置工具和项目名
        if(tool != 'spotbugs'):
            tool = data["Tool"]
            project_name = data["Project"]
        constructor.setGeneralInfo(tool, project_name)
        constructor.setWarning(json_content)

        flag_noResponse = True
        history_response = []
        while flag_noResponse:
            if prompts_technique == "zero_shot":
                response = openai_client.call_with_message(key, url, model_fullname, constructor.construct_zero_shot())
            elif prompts_technique == "one_shot":
                response = openai_client.call_with_message(key, url, model_fullname, constructor.construct_one_shot())
            elif prompts_technique == "few_shot":
                response = openai_client.call_with_message(key, url, model_fullname, constructor.construct_few_shot())
            elif prompts_technique == "general_info":
                response = openai_client.call_with_message(key, url, model_fullname, constructor.construct_general_info())
            elif prompts_technique == "expertise":
                response = openai_client.call_with_message(key, url, model_fullname, constructor.construct_expertise())
            elif prompts_technique == "chain_of_thought":
                response = openai_client.call_with_message(key, url, model_fullname, constructor.construct_chain())
            elif prompts_technique == "critique":
                response, history_response = openai_client.call_with_3messages(key, url, model_fullname, constructor.construct_critique())
            elif prompts_technique == "self_heuristic":
                response, history_response = openai_client.call_with_2messages(key, url, model_fullname, constructor.construct_heuristic())
            else:
                print("fail to find this prompts_technique:" + prompts_technique)
                return

            if response and response.choices and len(response.choices) > 0 and response.choices[0].message:
                flag_noResponse = False
            else:
                print("Error: The response or its expected structure is invalid.")
                time.sleep(1) 

        content = response.choices[0].message.content


        # Write to output file
        # 提取文件名（去掉路径和扩展名）
        base_name = os.path.splitext(os.path.basename(json_file))[0]

        # 构造 .txt 文件路径
        txt_file = os.path.join(output_dir, f"{base_name}.txt")
        with open(txt_file, "w", encoding="utf-8") as f:
            f.write(content)
        
        if prompts_technique == "critique" or prompts_technique == "self_heuristic":
            print("///////historyresponse///////", history_response)
            txt_file = os.path.join(output_dir, f"{base_name}_history.txt")
            # Open the file in append mode ("a") instead of write mode ("w")
            with open(txt_file, "a", encoding="utf-8") as f:
                count = 1
                for history in history_response:
                    f.write(f'response{count}:\n{history["content"]}\n\n\n')
                    count += 1
            # with open(txt_file, "a", encoding="utf-8") as f:
            #     for history in history_response:
            #         f.write(history.content + "\n\n\n")
            print(f"history store to: {output_dir}/{base_name}_history.txt")
            

        print(f"store to: {output_dir}/{base_name}.txt")



if __name__ == '__main__':
#java
    # # 项目列表
    # #projects = ["bcel", "codec", "collections", "configuration", "dbcp", "digester", "fileupload", "mavendp", "net", "pool"]
    # projects = ["dbcp"]
    # # 提示词技术列表
    # prompts_techniques = ["zero_shot", "one_shot", "few_shot", "general_info", "expertise", "chain_of_thought", "critique", "self_heuristic"]
    # # prompts_techniques = ["self_heuristic"]

    # tool = "spotbugs"

    # # 依次处理所有项目
    # for project in projects:
    #     for prompts_technique in prompts_techniques:
    #         print(f"Processing project {project} with {prompts_technique}")
    #         process_spotbugs_project_files( key, url, model, tool, prompts_technique, project, model_fullname)


#C
    prompts_techniques = ["self_heuristic"]
    tool = "unknown"
    project = "unknown"
    project_path = os.path.join("report", "c_json")
    for prompts_technique in prompts_techniques:
        process_spotbugs_project_files( key, url, model, tool, prompts_technique, project, project_path, model_fullname)
