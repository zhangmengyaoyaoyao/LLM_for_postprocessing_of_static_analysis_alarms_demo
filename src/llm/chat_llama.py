import glob
from http import HTTPStatus
import json
import os
import time
import dashscope
import sys

# 获取项目根目录
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 添加项目根目录到 sys.path
sys.path.append(project_root)
import construct_prompts as constructor


def call_with_messages(messages):

    # messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
    #             {'role': 'user', 'content': '介绍一下自己'}]
    response = dashscope.Generation.call(
        #api_key=os.getenv('DASHSCOPE_API_KEY'),
        api_key = 'sk-127b61202c714dcca246d6802542ae62',
        model='llama3.1-70b-instruct',
        messages=messages,
        result_format='message',  # set the result to be "message" format.
    )
    if response.status_code == HTTPStatus.OK:
        return response
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))


def process_spotbugs_project_files(model, tool, prompts_technique, project_name):
    # 调用限流
    count = 0
    
    # 构建项目路径
    project_path = os.path.join("report", tool, project_name)

    # 获取该项目下的所有 JSON 文件路径
    json_files = sorted(glob.glob(os.path.join(project_path, "*.json")))

    if not json_files:
        print(f"No JSON files found for project {project_name} in {project_path}.")
        return
    
    # 存储输出的路径
    output_dir = os.path.join("response", model, tool, prompts_technique, project_name)
    os.makedirs(output_dir, exist_ok=True)

    #temp
    # if(prompts_technique == 'general_info'):
    #     json_files = json_files[517:]

    # 依次处理每个 JSON 文件
    for i, json_file in enumerate(json_files):
        print(f"Processing file: {json_file}")
        with open(json_file, 'r') as f:
            data = json.load(f)

        # 转换 JSON 为字符串
        json_content = json.dumps(data, indent=2)
        
        # 设置工具和项目名
        if(tool != 'spotbugs'):
            tool = json_content["Tool"]
            project_name = json_content["Project"]
        constructor.setGeneralInfo(tool, project_name)
        constructor.setWarning(json_content)

        flag_noResponse = True
        while flag_noResponse:
            if prompts_technique == "one_shot":
                response = call_with_messages(constructor.construct_one_shot())
            elif prompts_technique == "few_shot":
                response = call_with_messages(constructor.construct_few_shot())
            elif prompts_technique == "general_info":
                response = call_with_messages(constructor.construct_general_info())
            elif prompts_technique == "expertise":
                response = call_with_messages(constructor.construct_expertise())
            elif prompts_technique == "chain_of_thought":
                response = call_with_messages(constructor.construct_chain)
            elif prompts_technique == "critique":
                response = call_with_messages(constructor.construct_critique())
            elif prompts_technique == "self_heuristic":
                response = call_with_messages(constructor.construct_heuristic())
            else:
                print("fail to find this prompts_technique:" + prompts_technique)

            if response is not None:
                flag_noResponse = False
            else:
                print(f"Rate limit exceeded or no response. Retrying in 3 seconds...")
                time.sleep(3) 
        

        content = response["output"]["choices"][0]["message"]["content"]

        # Write to output file
        # 提取文件名（去掉路径和扩展名）
        base_name = os.path.splitext(os.path.basename(json_file))[0]

        # 构造 .txt 文件路径
        txt_file = os.path.join(output_dir, f"{base_name}.txt")
        with open(txt_file, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"store to: {output_dir}/{base_name}.txt")

        # print("Pausing for 30 seconds...")
        # time.sleep(30) 
        # count += 1
        # if count == 4:
        #     print("Pausing for 35 seconds...")
        #     time.sleep(35)
        #     count = 0

if __name__ == '__main__':
    # 项目列表
    projects = ["bcel", "codec", "collections", "configuration", "dbcp", "digester", "fileupload", "mavendp", "net", "pool"]
    #prompts_techniques = ["zero_shot", "one_shot", "few_shot", "general_info", "expertise", "chain_of_thought", "critique", "self_heuristic"]
    prompts_techniques = ["few_shot"]

    tool = "spotbugs"
    model='llama3-70b-instruct'

    # 依次处理所有项目
    for project in projects:
        for prompts_technique in prompts_techniques:
            print(f"Processing project {project} with {prompts_technique}")
            process_spotbugs_project_files(model, tool, prompts_technique, project)