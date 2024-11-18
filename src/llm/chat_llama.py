import glob
from http import HTTPStatus
import json
import os
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
        api_key=os.getenv('DASHSCOPE_API_KEY'),
        model='llama3-70b-instruct',
        messages=messages,
        result_format='message',  # set the result to be "message" format.
    )
    if response.status_code == HTTPStatus.OK:
        print(response)
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))


def process_spotbugs_project_files(project_name, base_dir="report/spotbugs_json"):
    # 构建项目路径
    project_path = os.path.join(base_dir, project_name)

    # 获取该项目下的所有 JSON 文件路径
    json_files = sorted(glob.glob(os.path.join(project_path, "*.json")))

    if not json_files:
        print(f"No JSON files found for project {project_name} in {project_path}.")
        return

    # 依次处理每个 JSON 文件
    for json_file in json_files:
        print(f"Processing file: {json_file}")
        with open(json_file, 'r') as f:
            data = json.load(f)

        # 转换 JSON 为字符串
        json_content = json.dumps(data, indent=2)

        # 设置提示词内容
        constructor.setWarning(json_content)
        constructor.setGeneralInfo('SpotBugs', project_name)

        # 调用模型
        response = call_with_messages(constructor.construct_zero_shot())

        #print(f"Response for {json_file}: {response}")


if __name__ == '__main__':
    # 项目列表
    projects = ["bcel", "codec", "collections", "configuration", "dbcp", "digester", "fileupload", "mavendp", "net", "pool"]

    # 依次处理所有项目
    for project in projects:
        print(f"Processing project: {project}")
        process_spotbugs_project_files(project)