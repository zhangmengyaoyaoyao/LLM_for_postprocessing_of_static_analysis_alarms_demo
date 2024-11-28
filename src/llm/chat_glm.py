from openai import OpenAI 
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



def call_with_message(messages):
    client = OpenAI(
        api_key="18f2c750fd94cf998cd783992f97c819.5LiF231eFl2uYNQs",
        base_url="https://open.bigmodel.cn/api/paas/v4/"
    ) 
    response = client.chat.completions.create(
        model="glm-4-flash",  
        messages=messages,
        top_p=0.1,
        temperature=0.1,
        max_tokens=4095,
    ) 
    print("messages----", messages)
    print("response---",response.choices[0].message)
    return response


def call_with_3messages(messages):
    # return "", ""
    history_response = []
    # 如果是多轮对话
    # 展开元组为单个列表
    messages = [msg for sublist in messages for msg in sublist]
    # 保存所有轮次的消息
    message_with_historys = []
    print("Processing multiple rounds of messages")

    for message in messages:
        print("Processing message----", message)
        message_with_historys.append(message)
        # print("complete-----", message_with_historys)
        seccuss = False
        while not seccuss:
            client = OpenAI(
                api_key="18f2c750fd94cf998cd783992f97c819.5LiF231eFl2uYNQs",
                base_url="https://open.bigmodel.cn/api/paas/v4/"
            ) 
            response = client.chat.completions.create(
                model="glm-4-flash",  
                messages=message_with_historys,
                top_p=0.1,
                temperature=0.1,
                max_tokens=4095,
            ) 
            if response is None:
                print("generated_message is None")
            else:
                generated_message = {'role': 'assistant', 'content': response.choices[0].message.content}
                print("generated_message" , generated_message)
                message_with_historys.append(generated_message)  # 将模型生成的回复加入历史
                history_response.append(generated_message)
                seccuss = True

    return response, history_response

def call_with_2messages(messages):
    history_response = []
    # 如果是多轮对话
    # 展开元组为单个列表
    messages = [msg for sublist in messages for msg in sublist]
    # 保存所有轮次的消息
    message_with_historys = []
    print("Processing multiple rounds of 3messages")
    count = 0

    for message in messages:
        print("Processing message----", message)
        if count == 0:
            message_with_historys.append(message)
            count += 1
            continue
        message_with_historys.append(message)
        print("complete-----", message_with_historys)
        seccuss = False
        while not seccuss:
            client = OpenAI(
                api_key="18f2c750fd94cf998cd783992f97c819.5LiF231eFl2uYNQs",
                base_url="https://open.bigmodel.cn/api/paas/v4/"
            ) 
            response = client.chat.completions.create(
                model="glm-4-flash",  
                messages=message_with_historys,
                top_p=0.1,
                temperature=0.1,
                max_tokens=4095,
            )

            if response is None:
                print("generated_message is None")
            else:
                generated_message = {'role': 'assistant', 'content': response.choices[0].message.content}
                message_with_historys.append(generated_message)  # 将模型生成的回复加入历史
                history_response.append(generated_message)
                seccuss = True
        count += 1
    print("/////////////////historyhere////////////////////", history_response) 
    return response, history_response


def process_spotbugs_project_files(model, tool, prompts_technique, project_name):
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
    if prompts_technique == "general_info":
        json_files = json_files[578:]

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
        history_response = []
        while flag_noResponse:
            if prompts_technique == "zero_shot":
                response = call_with_message(constructor.construct_zero_shot())
            elif prompts_technique == "one_shot":
                response = call_with_message(constructor.construct_one_shot())
            elif prompts_technique == "few_shot":
                response = call_with_message(constructor.construct_few_shot())
            elif prompts_technique == "general_info":
                response = call_with_message(constructor.construct_general_info())
            elif prompts_technique == "expertise":
                response = call_with_message(constructor.construct_expertise())
            elif prompts_technique == "chain_of_thought":
                response = call_with_message(constructor.construct_chain())
            elif prompts_technique == "critique":
                response, history_response = call_with_3messages(constructor.construct_critique())
            elif prompts_technique == "self_heuristic":
                response, history_response = call_with_2messages(constructor.construct_heuristic())
            else:
                print("fail to find this prompts_technique:" + prompts_technique)
                return

            if response is not None:
                flag_noResponse = False
            else:
                print(f"response is none")
                time.sleep(3) 
        
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
            print(f"history store to: {output_dir}/{base_name}_history.txt")
            

        print(f"store to: {output_dir}/{base_name}.txt")


if __name__ == '__main__':
    # 项目列表
    #projects = ["bcel", "codec", "collections", "configuration", "dbcp", "digester", "fileupload", "mavendp", "net", "pool"]
    projects = ["bcel"]
    #prompts_techniques = ["zero_shot", "one_shot", "few_shot", "general_info", "expertise", "chain_of_thought", "critique", "self_heuristic"]
    prompts_techniques = ["critique"]
    # prompts_techniques = ["self_heuristic"]


    tool = "spotbugs"
    model='glm-4-flash'

    # 依次处理所有项目
    for project in projects:
        for prompts_technique in prompts_techniques:
            print(f"Processing project {project} with {prompts_technique}")
            process_spotbugs_project_files(model, tool, prompts_technique, project)